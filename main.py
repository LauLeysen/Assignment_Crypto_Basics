from homorphic_encryption import initialize_context, encrypt_number, add_ciphertexts, decrypt_ciphertext, print_ciphertext
from shamir_secret import shamir_encrypt, shamir_decrypt
from sslib import shamir
import sys


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

def shamir():
    choice = int(input("Encrypt or decrypt sentence? (1,2): "))
    
    if choice == 1:
        print("encrypt")
        sentence = input("Write your sentence: ")
        
        encrypted_text = shamir_encrypt(sentence)
        print(encrypted_text)

    elif choice == 2:
        print("decrypt")
        # example secret {'required_shares': 2, 'prime_mod': 'AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhQ==', 'shares': ['1-Swwdr0O19NSMsoG4DXxvTeB9WTykw9+a', '2-lhg7XodrvzSw+5BPsYW+LkfaPxPmFVnA']}
        data = input("Write your shares in the right format: ")
        decrypted_text = shamir_decrypt(data)
        print(decrypted_text)
    else:
        print("wrong input")

def main():
    homorphic()
    shamir()

if __name__ == "__main__":
    main()