from sslib import shamir
import ast

def shamir_encrypt(sentence):
    required_shares = 2
    distributed_shares = 2

    data = shamir.to_base64(shamir.split_secret(sentence.encode('ascii'), required_shares, distributed_shares))

    return data

def shamir_decrypt(sharesdata):
    data = ast.literal_eval(sharesdata) # need to use ast to get correct formatting for the library strings dont work

    data = shamir.recover_secret(shamir.from_base64(data)).decode('ascii')

    return data