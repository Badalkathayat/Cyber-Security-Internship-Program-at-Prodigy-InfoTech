Pixel Manipulation for Image Encryption

A Python tool for encrypting and decrypting images using pixel manipulation techniques. This tool allows users to encrypt images by modifying pixel values with a simple encryption key and then decrypt them using the same key.

## Features

- **Image Encryption**: Encrypt images by altering pixel values with a specified key.
- **Image Decryption**: Restore encrypted images to their original form by applying the inverse operation.
- **Supports Various Image Formats**: Compatible with common image formats such as PNG, JPEG, BMP, etc.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/BadalKathayat/pixel-image-encryption.git
   cd pixel-image-encryption
   

2. Install the required dependencies:
   bash
   pip install pillow
   

 Usage

1. Run the Python script:
   ```bash
   python image_encryption.py
   ```

2. Follow the on-screen prompts:
   - Choose whether to **Encrypt** or **Decrypt** an image.
   - Enter the path of the image file you want to process.
   - Provide an integer key for encryption or decryption.
   - Specify the output path where the processed image should be saved.

Example

To encrypt an image:
```
Pixel Manipulation for Image Encryption
1. Encrypt Image
2. Decrypt Image
3. Exit
Enter your choice (1-3): 1
Enter the path of the image to encrypt: sample_image.png
Enter the encryption key (integer): 123
Enter the output path for the encrypted image: encrypted_image.png
Image encrypted and saved as encrypted_image.png


To decrypt an image:

Pixel Manipulation for Image Encryption
1. Encrypt Image
2. Decrypt Image
3. Exit
Enter your choice (1-3): 2
Enter the path of the image to decrypt: encrypted_image.png
Enter the decryption key (integer): 123
Enter the output path for the decrypted image: decrypted_image.png
Image decrypted and saved as decrypted_image.png

Contributing

If you would like to contribute to this project, you can:
- Open an issue to report bugs or suggest new features.
- Fork the repository and submit a pull request with your enhancements.

License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
