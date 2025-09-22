#!/usr/bin/env python3
import os
import subprocess
import time

# Colores
RESET = "\033[0m"

# Banner de presentación en lolcat
def banner():
    banner_text = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                  ┃
┃        ⚡🔥  ST-BF TOOL SETUP  🔥⚡              ┃
┃                                                  ┃
┃        🌐 Install dependencies and wordlists 🌐  ┃
┃                                                  ┃
┃  Created by: satan                               ┃
┃  Version: 1.0                                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
    try:
        subprocess.run(f"echo '{banner_text}' | lolcat", shell=True)
    except:
        print(banner_text)

# Instalación de dependencias
def install_dependencies():
    print("\nInstalling dependencies...\n")
    os.system("pkg update && pkg upgrade")
    os.system("pkg install python")
    os.system("pkg install python3-pip")
    os.system("pip install --upgrade pip")
    os.system("pip install requests")
    os.system("gem install lolcat || pkg install lolcat")
    os.system("pkg install git")
    os.system("pkg install nano")
    os.system("pkg install curl")
    os.system("pkg install wget")
    os.system("pkg install unzip")
    os.system("pkg install tar")
    os.system("pkg install gzip")
    print("\nDependencies installed successfully!\n")

# Instalación de wordlists (solo rockyou)
def install_wordlists():
    wordlists_dir = "wordlists"
    if not os.path.exists(wordlists_dir):
        os.makedirs(wordlists_dir)

    rockyou_gz = os.path.join(wordlists_dir, "rockyou.txt.gz")
    rockyou_txt = os.path.join(wordlists_dir, "rockyou.txt")

    # Comprobar si ya existe
    if os.path.isfile(rockyou_txt):
        print(f"\n[INFO] rockyou.txt already exists in {wordlists_dir}.\n")
        return

    # Descargar rockyou
    print("\nDownloading rockyou wordlist...\n")
    os.system(f"wget -O {rockyou_gz} https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt")

    # Descomprimir rockyou
    print("Decompressing rockyou...\n")
    os.system(f"gzip -d -f {rockyou_gz}")

    print(f"\n[INFO] rockyou.txt is ready in {wordlists_dir} ✅\n")

# Main
def main():
    os.system("clear")
    banner()

    # Preguntar si instalar dependencias
    choice = input("Do you want to install dependencies? (y/n): ").strip().lower()
    if choice == "y":
        install_dependencies()
    else:
        print("Skipping dependencies installation...\n")

    # Instalar wordlists (rockyou)
    install_wordlists()

    print("Setup finished! 🎉")
    print("You can now run your brute force script.")

if __name__ == "__main__":
    main()
