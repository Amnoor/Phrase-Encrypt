# **Phrase Encrypt**
A simple educational tool for encrypting and decrypting phrases using a substitution cipher implementation.
### **Overview**
This Python program demonstrates basic cryptographic concepts by implementing a substitution cipher that:
- Generates a unique random character mapping key on each execution
- Supports encryption and decryption of text phrases
- Handles letters (uppercase and lowercase), digits, punctuation, and spaces
### **Usage**
Run the script and follow the interactive prompts:
- Input in terminal: python "Phrase Encryption.py"
  1. Encryption: Enter text to encrypt when prompted
  2. Decryption: Enter encrypted text to decrypt when prompted
### **Important Notes**
- This implementation is for **educational purposes only**
- Not suitable for real-world security applications
- Each run generates a new random key (same input produces different output across sessions)
- Key is not preserved between sessions (encrypted text can only be decrypted in the same session)
### **Technical Details**
The cipher uses a character set containing:
- Space character
- Punctuation marks (!"#$%&'()*+,-./:;<=>?@[]^_`{|}~)
- Digits (0-9)
- ASCII letters (both uppercase and lowercase)
The program creates a shuffled version of this character set as the encryption key, then performs character-by-character substitution based on position mapping.
### **License**
This project is licensed under the GNU General Public License v3.0 - see the [**LICENSE**](./LICENSE) file for details.