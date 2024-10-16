import os
import random
import string

def generate_random_key(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)).encode()


def kyber():
    # Generate "keys" kan ook advanced library gebruiken in praktijk veel beter
    private_key = generate_random_key(32)
    public_key = generate_random_key(32)

    message = "Wazaaaa hallo wereld"

    # Encrypt het bericht door XOR te gebruiken
    if len(public_key) < len(message):
        raise ValueError("key moet minstens zo lang zijn als het bericht")

    encrypted_message = bytes(a ^ b for a, b in zip(message.encode(), public_key[:len(message)]))

    decrypted_message = bytes(a ^ b for a, b in zip(encrypted_message, public_key[:len(message)]))

    print("Private key:", private_key.decode())
    print("Public key:", public_key.decode())
    print("Encrypted boodschap:", encrypted_message.hex())
    print("Decrypted message:", decrypted_message.decode())
