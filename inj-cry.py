from PIL import Image
import piexif
import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import datetime
import codecs

# Functions for encryption and decryption
def encrypt_code(code, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(code.encode(), AES.block_size))
    iv = binascii.hexlify(cipher.iv).decode('utf-8')
    ct = binascii.hexlify(ct_bytes).decode('utf-8')
    return iv + ct

def rot13_encrypt(text):
    return codecs.encode(text, 'rot_13')

def obfuscate_code_and_write_to_image(image_path, code, output_image_path, additional_encryption=False):
    key = get_random_bytes(16)  # Generate a random AES encryption key
    obfuscated_code = encrypt_code(code, key)  # Encrypt the code

    if additional_encryption:
        # Add a second layer of AES encryption
        additional_key = get_random_bytes(16)
        obfuscated_code = encrypt_code(obfuscated_code, additional_key)
        print("Additional AES encryption key (keep it secure!):", binascii.hexlify(additional_key).decode())
        
        # Apply ROT13 encryption
        obfuscated_code = rot13_encrypt(obfuscated_code)

    hex_code = binascii.hexlify(obfuscated_code.encode())  # Convert the encrypted code to hex
    hex_code = hex_code[::-1]  # Reverse the encrypted code
    exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None, "Interop": {}}  # Prepare EXIF metadata with the hex code
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = hex_code
    
    exif_bytes = piexif.dump(exif_dict)

    img = Image.open(image_path)  # Load the image and add the EXIF metadata
    img.save(output_image_path, "jpeg", exif=exif_bytes)
    
    return key  # Return the encryption key for future decryption

# Example payload
code_to_obfuscate = """
import datetime
print("Current time:", datetime.datetime.now())
"""

image_path = input("Enter the input image path: ")
output_image_path = input("Enter the output image path: ")
add_encryption = input("Do you want to add another layer of encryption? (yes/no): ").strip().lower() == 'yes'

key = obfuscate_code_and_write_to_image(image_path, code_to_obfuscate, output_image_path, additional_encryption=add_encryption)

print("AES encryption key (keep it secure!):", binascii.hexlify(key).decode())
