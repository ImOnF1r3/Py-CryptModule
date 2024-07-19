import piexif
from PIL import Image
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import codecs

def decrypt_code(iv_ct, key):
    iv = binascii.unhexlify(iv_ct[:32])
    ct = binascii.unhexlify(iv_ct[32:])
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
    return pt

def rot13_decrypt(text):
    return codecs.decode(text, 'rot_13')

def execute_code_from_image(image_path, key_hex, additional_encryption=False, additional_key_hex=None):
    key = binascii.unhexlify(key_hex)  # Convert the hexadecimal key to bytes here within the function
    img = Image.open(image_path)  # Load the image and read the EXIF metadata
    exif_data = piexif.load(img.info['exif'])
    hex_code = exif_data["0th"][piexif.ImageIFD.ImageDescription]  # Read the encrypted code in hex from the metadata
    hex_code = hex_code[::-1]
    obfuscated_code = binascii.unhexlify(hex_code).decode()
    
    if additional_encryption:
        # Apply ROT13 decryption
        obfuscated_code = rot13_decrypt(obfuscated_code)
        # Decrypt the second layer of AES encryption
        additional_key = binascii.unhexlify(additional_key_hex)
        obfuscated_code = decrypt_code(obfuscated_code, additional_key)

    code = decrypt_code(obfuscated_code, key)  # Convert from hex to string and decrypt the code
    exec(code)  # Execute the code

image_path = input("Enter the image to read: ")
key_hex = input("Enter the key code: ")
add_encryption = input("Is there another layer of encryption? (yes/no): ").strip().lower() == 'yes'

if add_encryption:
    additional_key_hex = input("Enter the additional AES key: ")
    execute_code_from_image(image_path, key_hex, additional_encryption=True, additional_key_hex=additional_key_hex)
else:
    execute_code_from_image(image_path, key_hex)
