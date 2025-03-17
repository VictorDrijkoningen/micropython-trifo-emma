import requests


def check_version_file():
    try:
        with open("VERSION", 'r') as f:
            print("found VERSION file")
    except:
        with open("VERSION", 'w') as f:
            f.write("created")
    


def update(force_update = False):
    check_version_file()
    env = ("https://raw.githubusercontent.com/VictorDrijkoningen/micropython-trifo-emma/refs/heads/main/VERSION",
           "https://raw.githubusercontent.com/VictorDrijkoningen/micropython-trifo-emma/refs/heads/main/boot.py",
           "https://raw.githubusercontent.com/VictorDrijkoningen/micropython-trifo-emma/refs/heads/main/main.py",
           "https://raw.githubusercontent.com/VictorDrijkoningen/micropython-trifo-emma/refs/heads/main/systemfunctions.py")
    
    with open("VERSION") as file:
        emma_version = file.read()
        githubversion = requests.get(env[0]).text

        if emma_version != githubversion or force_update:
            print(emma_version.split("-")[0]+" / "+ str(githubversion).split("-")[0])
            with open('VERSION', 'w') as f:
                f.write(githubversion)
            with open('boot.py', 'w') as f:
                f.write(requests.get(env[1]).text)
            with open('main.py', 'w') as f:
                f.write(requests.get(env[2]).text)
            with open('systemfunctions.py', 'w') as f:
                f.write(requests.get(env[3]).text)
            print('done updating')
        else:
            print("Already up to date")
    return emma_version

