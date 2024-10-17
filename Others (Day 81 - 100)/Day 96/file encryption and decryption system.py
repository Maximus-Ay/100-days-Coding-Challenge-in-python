'''
    - Write a Python program to create a class that represents a simple file encryption and decryption system.
'''

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

class FileEncryptionSystem:
    def __init__(self, key):
        self.key = key.encode()
        self.backend = default_backend()

    def encrypt_file(self, input_file, output_file):
        # Generate random 128-bit IV.
        iv = os.urandom(16)
        
        # Create a new AES-CBC cipher object.
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        
        # Read input file.
        with open(input_file, 'rb') as f:
            data = f.read()
        
        # Pad data to multiple of block size.
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        
        # Encrypt data.
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        
        # Write IV and encrypted data to output file.
        with open(output_file, 'wb') as f:
            f.write(iv + encrypted_data)
        
        print(f"File encrypted: {input_file}")

    def decrypt_file(self, input_file, output_file):
        # Read IV and encrypted data from input file.
        with open(input_file, 'rb') as f:
            iv = f.read(16)
            encrypted_data = f.read()
        
        # Create a new AES-CBC cipher object.
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        
        # Decrypt data.
        decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        
        # Unpad decrypted data.
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
        
        # Write decrypted data to output file.
        with open(output_file, 'wb') as f:
            f.write(data)
        
        print(f"File decrypted: {input_file}")

# Example usage
key = "mysecretkey1234"  # 16-byte key
file_system = FileEncryptionSystem(key)

input_file = "original.txt"
encrypted_file = "encrypted.txt"
decrypted_file = "decrypted.txt"

# Encrypt file
file_system.encrypt_file(input_file, encrypted_file)

# Decrypt file
file_system.decrypt_file(encrypted_file, decrypted_file)
