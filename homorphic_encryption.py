# my_homorphic_project/homorphic.py

import tenseal as ts
import base64

def initialize_context():
    """
    Initializes and returns a CKKS context for homomorphic encryption.
    
    :return: TenSEAL CKKSContext
    """
    context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60, 40, 40, 60]
    )
    context.global_scale = 2**40
    context.generate_galois_keys()
    return context

def encrypt_number(context, number):
    """
    Encrypts a single number using the provided context.
    
    :param context: TenSEAL CKKSContext
    :param number: The number to encrypt
    :return: Encrypted CKKSVector
    """
    return ts.ckks_vector(context, [number])

def add_ciphertexts(cipher1, cipher2):
    """
    Adds two ciphertexts.
    
    :param cipher1: First encrypted CKKSVector
    :param cipher2: Second encrypted CKKSVector
    :return: Sum of the two ciphertexts as a CKKSVector
    """
    return cipher1 + cipher2

def decrypt_ciphertext(cipher):
    """
    Decrypts a ciphertext.
    
    :param cipher: Encrypted CKKSVector
    :return: Decrypted list of numbers
    """
    return cipher.decrypt()

def serialize_ciphertext(cipher):
    """
    Serializes and encodes a ciphertext to base64 for readable representation.
    
    :param cipher: Encrypted CKKSVector
    :return: Base64 encoded string of the serialized ciphertext
    """
    serialized = cipher.serialize()
    encoded = base64.b64encode(serialized).decode('utf-8')
    return encoded

def print_ciphertext(cipher):
    """
    Prints the base64 encoded ciphertext.
    
    :param cipher: Encrypted CKKSVector
    """
    encoded = serialize_ciphertext(cipher)
    print(encoded)
