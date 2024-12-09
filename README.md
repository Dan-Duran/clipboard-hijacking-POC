# Clipboard Hijacking PoC

This repository contains a **Proof of Concept (PoC)** script that demonstrates how clipboard hijacking attacks work. It is meant strictly for **educational purposes** to raise awareness about this type of attack and how to defend against it.

- **👉 Checkout some more awesome tools at [GetCyber](https://getcyber.me/tools)**
- **👉 Subscribe to my YouTube Channel [GetCyber - YouTube](https://youtube.com/getCyber)**
- **👉 Discord Server [GetCyber - Discord](https://discord.gg/YUf3VpDeNH)**

> **Disclaimer**: This PoC is intended for educational purposes only. Misuse of this code to harm individuals or organizations is strictly prohibited and may violate ethical, legal, or regulatory requirements.

## How Clipboard Hijacking Works
Clipboard hijacking is a type of attack where malicious software monitors the clipboard for sensitive information such as cryptocurrency wallet addresses. When such data is detected, the malware replaces it with the attacker's address, tricking the victim into sending funds to the attacker.

## About This Script
The provided Python script:
- Monitors the clipboard for cryptocurrency wallet addresses.
- Replaces detected wallet addresses with a fake wallet address.
- Simulates how clipboard hijackers manipulate clipboard data.

**Note**: Real-world malware is far more complex and stealthy. This script is a simplified demonstration.

## Setup Instructions
To run this PoC, follow the steps below:

### 1. Clone the Repository
```bash
git clone https://github.com/Dan-Duran/clipboard-hijacking-POC.git
cd clipboard-hijacking-poc
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Required Libraries
Install the necessary Python libraries using `pip`:
```bash
pip install pyperclip
```

### 4. Run the Script
```bash
python clipboard_hijacker.py
```
The script will start monitoring the clipboard for cryptocurrency wallet addresses. If it detects one, it will replace it with the fake wallet address defined in the script.

## Example Fake Wallet Address
The script uses the following fake wallet address:
```
3J98t1-FAKE-WpEZ73CNmQviecrnyiWrnqRhWNLy
```

## How to Stay Safe
1. Always verify clipboard contents before pasting sensitive data.
2. Use security tools or clipboard managers that warn of unexpected changes.
3. Keep your systems updated and use trusted antivirus software.

## Educational Focus
This PoC is designed to teach cybersecurity enthusiasts and developers about clipboard hijacking attacks. It emphasizes the importance of input validation and user awareness.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
