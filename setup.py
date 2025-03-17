import requests

def run():
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

    with open("wifisecret.txt", "w") as f:
        do = True
        while do:
            choice = input("Do you want to connect to LAN wifi or create an AP?")
            if choice == "AP":
                f.write(f"AP,ssid,pass")
            elif choice == "LAN":
                do = False
                ssid = input("ssid:")
                password = input("password:")
                f.write(f"{choice},{ssid},{password}")
            else:
                print("wrong option")
    print("Setup done")
run()