Caesar Cipher

This Python script implements a simple Caesar cipher for both encryption and decryption. The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted by a certain number of positions down or up the alphabet.

Features

- **Encryption**: Encrypts a message by shifting each letter by a specified number of positions.
- **Decryption**: Decrypts a message by reversing the shift.
- **User Interaction**: Provides a simple command-line interface for users to choose between encryption, decryption, or exiting the program.

Usage

1. **Clone the Repository**:
    bash
    git clone https://github.com/Badalkathayat/caesar-cipher.git
    
2. **Navigate to the Project Directory**:
    bash
    cd caesar-cipher
    
3. **Run the Script**:
    bash
    python3 task1.py
    

4. **Choose an Option**:
    - **1. Encrypt**: Enter a message and a shift value to encrypt the message.
    - **2. Decrypt**: Enter an encrypted message and the shift value used for encryption to decrypt it.
    - **3. Exit**: Exit the program.

Example

**Encrypting a message**:

Enter your choice (1-3): 1
Enter the message to encrypt: HELLO
Enter the shift value: 3
Encrypted message: KHOOR


**Decrypting a message**:

Enter your choice (1-3): 2
Enter the message to decrypt: KHOOR
Enter the shift value: 3
Decrypted message: HELLO

Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

License

This project is open-source and available under the [MIT License](LICENSE).
