ST-BF Tool

ST-BF is a brute-force login testing tool for websites, designed for educational purposes only. It allows you to test password security using wordlists and provides a simple, colorful interface in Termux.

⚠️ WARNING: Use this tool only on your own websites or with explicit permission. Unauthorized use is illegal.
Features
	•	Colored banners and messages using lolcat
	•	Custom wordlist support
	•	Real-time progress display (x/total passwords)
	•	Only shows password if it’s successfully found
	•	Optional automatic installation of dependencies and wordlists
	•	Fast brute-force attempts with adjustable sleep

⸻

Requirements
	•	Termux (Android)
	•	Python 3
	•	Pip
	•	requests Python module
	•	lolcat for colored output
  3.	Follow the instructions in the setup:

	•	Install all dependencies? (y/n)
	•	Install rockyou wordlist or optional wordlists?

⸻

Installation
	1.	Clone the repository:
     git clone https://k1itllx1killx/ST-BF.git

2.	Run the setup script to install dependencies and download wordlists:
python3 setup.py


3.	Follow the instructions in the setup:

	•	Install all dependencies? (y/n)
	•	Install rockyou wordlist or optional wordlists?

⸻

Usage
	1.	Start the brute-force tool:
    python3 bruteforce.py
    
    Notes
	•	Ensure your wordlists are inside the wordlists/ folder.
	•	Only use this tool on your own systems or for authorized penetration testing.
	•	The brute-force speed can be adjusted by modifying the sleep time in the script.

Contributing

Pull requests and issues are welcome. Please ensure your contributions follow ethical guidelines.

⸻

License

This project is for educational purposes only. Misuse for illegal activities is strictly prohibited.
