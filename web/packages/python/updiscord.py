# Welcome! Discord Update
# This is licensed under GPL-3.0. Not affliated with Discord or any affilates!
# WARNING: THIS REMOVES ANY CLIENT MODIFICATIONS YOU HAVE (ex: vencord, betterdiscord)
import urllib.request
import os
print("Welcome to Discord Update.")
print("This is licensed under GPL-3.0. Not affliated with Discord or any affilates!")
print("WARNING: THIS REMOVES ANY CLIENT MODIFICATIONS YOU HAVE (ex: vencord, betterdiscord)")
print("------")
print("This tool downloads the latest Discord .deb file to this directory!")
print("Ths uses https://discord.com/api/download?platform=linux&format=deb and can be broken at any time.")
print("Then it will install the deb file using dpkg.")
print("THIS ONLY WORKS ON DEBIAN BASED LINUX. Depending on your distro, this may not work. Only tested on Linux Mint 22.1 Xia and a beta version of 22.2 Zara.")
print("If you wouldn't like to continue, please exit the script using ctrl + c or closing your terminal.")
print("------------")
input("Waiting for input.. If you would like to exit, run ctrl+c or close console. If you'd like to continue, press enter.")
headers = {"User-Agent": "Mozilla/5.0"}
print("Downloading with User-Agent as Mozilla/5.0")
req = urllib.request.Request("https://discord.com/api/download?platform=linux&format=deb", headers=headers)

with urllib.request.urlopen(req) as response, open("discord.deb", "wb") as out_file:
    print("Writing file...")
    out_file.write(response.read())
try:
    os.system("sudo dpkg -i discord.deb")
except Exception as e:
    print("Issue installing! The download was successful, but we couldn't install it. If this continues to not work, run discord.deb that was downloaded yourself.")
    print("Error: " + str(e))
print("Great! Want Vencord?")
input("If you don't want Vencord (which is a Client Modification and is bannable!), exit the script or run ctrl+c.")
os.system('sh -c "$(curl -sS https://raw.githubusercontent.com/Vendicated/VencordInstaller/main/install.sh)"')