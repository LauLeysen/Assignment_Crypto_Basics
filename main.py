from homorphic_encryption import (
    initialize_context,
    encrypt_number,
    add_ciphertexts,
    decrypt_ciphertext,
    print_ciphertext
)

def homorphic():
    context = initialize_context()
    
    getal1 = 75
    getal2 = 326
    
    cipher1 = encrypt_number(context, getal1)
    cipher2 = encrypt_number(context, getal2)
    
    cipher_sum = add_ciphertexts(cipher1, cipher2)
    
    decrypted_sum = decrypt_ciphertext(cipher_sum)
    
    print("Ciphertext van de som:")
    print_ciphertext(cipher_sum)

    print("De som decrypted is:", decrypted_sum[0])

def main():
    homorphic()

if __name__ == "__main__":
    main()