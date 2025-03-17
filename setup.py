import requests
import network
import time


def download():
    env = ("https://raw.githubusercontent.com/VictorDrijkoningen/micropython-trifo-emma/refs/heads/main/VERSION",
        "https://raw.githubusercontent.com/VictorDrijkoningen/micropython-trifo-emma/refs/heads/main/boot.py",
        "https://raw.githubusercontent.com/VictorDrijkoningen/micropython-trifo-emma/refs/heads/main/main.py",
        "https://raw.githubusercontent.com/VictorDrijkoningen/micropython-trifo-emma/refs/heads/main/systemfunctions.py")
    try:
        print("Downloading latest software")
        with open('VERSION', 'w') as f:
            f.write(requests.get(env[0]).text)
        with open('boot.py', 'w') as f:
            f.write(requests.get(env[1]).text)
        with open('main.py', 'w') as f:
            f.write(requests.get(env[2]).text)
        with open('systemfunctions.py', 'w') as f:
            f.write(requests.get(env[3]).text)
    except:
        print("Could not download latest files")

def run():
    print("entering webrepl setup")
    import webrepl_setup
    print("done webrepl setup")

    with open("wifisecret.txt", "w") as f:
        do = True
        while do:
            print("Do you want to connect to LAN wifi or create an AP?")
            choice = input("AP/LAN:")
            if choice == "AP":
                do = False
                f.write(f"AP,ssid,pass")
                print("You should manually download all files to this device, as there is no connection for download when using AP mode")
            elif choice == "LAN":
                do = False
                ssid = input("ssid:")
                password = input("password:")
                f.write(f"{choice},{ssid},{password}")
                lan = network.WLAN(network.STA_IF)
                lan.active(True)
                lan.connect(ssid, password)
                start = time.time()
                while not lan.isconnected():
                    time.sleep(0.1)
                    if (time.time() - start) > 10:
                        raise TimeoutError
                download()
            else:
                print("wrong option")
    print("Setup done")
run()