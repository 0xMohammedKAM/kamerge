# Kamerge

Kamerge is a command-line tool designed to simplify the process of injecting Metasploit payloads into Android APK files and automating the setup of a Metasploit handler. It is intended for educational and research purposes only.

## Features
- Injects a Metasploit reverse_https payload into an existing APK.
- Automates the launch of a Metasploit handler for your payload.
- Interactive, user-friendly terminal interface.

## Installation

1. **Clone or Download** this repository to your Linux machine.
2. **Install Dependencies:**
   - Python 3.x
   - [rich](https://pypi.org/project/rich/) (for colored terminal output)
   - Metasploit Framework
   - apktool, apksigner, zipalign (for APK manipulation)

   You can install Python dependencies with:
   ```sh
   pip install -r requirements.txt
   ```

   Make sure `msfvenom`, `msfconsole`, `apktool`, `apksigner`, and `zipalign` are in your PATH.

## Usage

Run the tool from your terminal:

```sh
python3 kamerge.py
```

Follow the on-screen prompts to:
- Enter your local IP address, port, APK path, and output name.
- Optionally launch the Metasploit handler automatically.

## Troubleshooting
- **Permission Denied:** Ensure you have execute permissions for all required tools and the APK file.
- **Command Not Found:** Make sure all dependencies (msfvenom, msfconsole, apktool, etc.) are installed and in your PATH.
- **APK Not Working:** Some APKs may not be compatible with payload injection. Try with a different APK.
- **Metasploit Handler Not Connecting:** Double-check your IP address and port, and ensure your firewall allows incoming connections.

## Roadmap
While Kamerge currently focuses on payload injection, a full APK merging tool is planned for the future. Development is paused for now due to school commitments, but stay tuned for updates!

## Disclaimer
This tool is for educational and research purposes only. Use it responsibly and only on devices you own or have explicit permission to test.(AI wrote this I'm just lazy af)

---

Feel free to contribute or suggest features. Thanks for checking out Kamerge!

---
YES i used AI to write this readME file
