# Python Secure Password Generator

A flexible and interactive command-line utility made with Python for generating strong, customizable passwords in Python. This is the original Password Generator made in the Password Generator Series.

## Features

- **Alphanumeric Passwords:** Combine random words, numbers, and punctuation for strong, memorable passwords.
- **Word-Only Passwords:** Create passphrases using multiple random words (default 4+).
- **Numeric Passwords:** Generate secure numeric codes (default 8+ digits).
- **Random ASCII Passwords:** Fully random combinations of letters, numbers, and symbols.
- **Customizable Lengths:** Choose password or passphrase length based on type.
- **Uses Secure Randomization:** Relies on Python's `secrets` and `random` modules for robust entropy.
- **Easy to Use:** Interactive command-line interface guides you through options.

## Requirements

- Python 3.x (if you don't have it please install it using this link [https://www.python.org/downloads/](https://www.python.org/downloads/) and select the latest stable version for your operating system)
- `words_alpha.txt` (included in the repository for word-based passwords)

## Why Strong Passwords Matter

Using strong, unique passwords is essential to protect your accounts from hackers and cybercriminals. Weak or reused passwords are vulnerable to attacks like brute force and credential stuffing, putting your data and identity at risk.

- **Longer passwords are stronger:** Using more characters makes passwords much harder to crack.
- **Randomness matters:** A mix of words, numbers, and symbols increases security.
- **Unique passwords for every account:** Don’t reuse passwords across sites.

For a simple explanation and tips, see this guide from the [Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov/secure-our-world/use-strong-passwords) ([watch the short video](https://www.youtube.com/watch?v=U0nQe8cQ9n8)).

**_Why these defaults?_**
- **Alphanumeric passwords** combine words, numbers, and symbols for complexity.
- **Word-based passphrases** use at least 4 random words for memorability and strength.
- **Numeric codes** require 8+ digits to defend against guessing.
- **Random ASCII passwords** defaults to 16 characters for high entropy.

These choices are based on security best practices and recommendations from organizations like CISA and NIST.

## Quick Start (Recommended for Most Users)

**Download the latest version:**

1. Go to the [Releases page](https://github.com/Bloomy52/secure-password-generator/releases).
2. Download the latest release zip file.
3. Extract the zip file to a folder on your computer.

**Run the password generator:**
```bash
python secure_pwgen.py
```

**Follow the prompts:**
- Select your password type:
  - Alphanumeric
  - Alphabetic (words only)
  - Numeric
  - Completely random (ASCII)
- Enter your desired length or number of words/digits as prompted.

## For Developers or Advanced Users

If you prefer, you can clone the repository:
```bash
git clone https://github.com/Bloomy52/secure-password-generator.git
cd secure-password-generator
python secure_pwgen.py
```

## Example

```
Welcome to the Secure Password Generator!
To begin, please select the type of password you would like using a num-pad/num-row on your keyboard.
Alphanumeric Password: 1
Alphabetic Password: 2
Numeric Password: 3
Completely Random Password: 4
1
This password will contain words, numbers, and punctuation.
<Your generated password will appear here>
```

## Latest Changes

- Passcode generation function now uses `secrets` module for cryptographic randomization.
- Alphanumeric and Alphabetic passwords now capitalize the first letter of each word.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.
