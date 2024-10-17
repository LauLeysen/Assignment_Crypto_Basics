import oqs

def DILITHIUM():
    signer = oqs.Signature('Dilithium2')
    public_key = signer.generate_keypair()
    private_key = signer.export_secret_key()

    message = b"hihi huhuCRYSTALS-DILITHIUM"

    signature = signer.sign(message)

    print(f"Message: {message}")
    print(f"Signature: {signature}")

    is_valid = signer.verify(message, signature, public_key)

    if is_valid:
        print("The signature is valid!")
    else:
        print("The signature is NOT valid!")
