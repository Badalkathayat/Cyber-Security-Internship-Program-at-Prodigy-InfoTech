import cv2
import numpy as np

def encrypt_image(image, key):
    encrypted_image = image.copy()
    rows, cols, channels = encrypted_image.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                encrypted_image[i, j, k] = (encrypted_image[i, j, k] + key) % 256
    return encrypted_image

def decrypt_image(encrypted_image, key):
    decrypted_image = encrypted_image.copy()
    rows, cols, channels = decrypted_image.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                decrypted_image[i, j, k] = (decrypted_image[i, j, k] - key) % 256
    return decrypted_image

def main():
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption key (integer): "))

    image = cv2.imread(image_path)
    encrypted_image = encrypt_image(image, key)
    cv2.imshow("Encrypted Image", encrypted_image)
    cv2.waitKey(0)

    decrypted_image = decrypt_image(encrypted_image, key)
    cv2.imshow("Decrypted Image", decrypted_image)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()