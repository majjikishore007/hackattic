import base64
import binascii
import hashlib
import hmac
import json

import requests
import scrypt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

base_url = 'https://hackattic.com/challenges/password_hashing'
key='ab17bddaef9e90e4'

def get_data():
    res = requests.get(f'{base_url}/problem?access_token={key}')
    return json.loads(res.text)


def decode_base64(salt):
    # Decode the string
    decoded_string = base64.b64decode(salt)

    return decoded_string


def calculate_SHA256(password):
    hashed_string = hashlib.sha256(password).hexdigest()
    return hashed_string


def calculate_HMAC_SHA256(password, salt):
    digest = hmac.new(salt,password, hashlib.sha256).hexdigest()
    return digest


def calculate_pbkdf2(password, salt, rounds,has):
    hashed=binascii.hexlify(hashlib.pbkdf2_hmac(has, password, salt, rounds)).decode('utf-8')
    return hashed

def calculate_scrypt(password, salt, N, r, p, buflen):
    hashed = binascii.hexlify(scrypt.hash(password, salt, N, r, p, buflen)).decode('utf-8')
    return hashed

def post_data(data):
    res=requests.post(f"https://hackattic.com/challenges/password_hashing/solve?access_token={key}", json = data)
    print(res.text)

if __name__ == "__main__":
    data = get_data()
    print("data:::", data)

    password = data['password']
    salt = data['salt']
    p_data = data['pbkdf2']
    s_data = data['scrypt']

    password = bytes(password, 'utf-8')
    salt = bytes(salt, 'utf-8')
    # decoding the salt
    decodedSalt = decode_base64(salt)
    

    res = {}   
    # getting all the hashes
    res['sha256'] = calculate_SHA256(password)
    res['hmac'] = calculate_HMAC_SHA256(password, decodedSalt)
    res['pbkdf2'] = calculate_pbkdf2(password, decodedSalt, p_data['rounds'],p_data['hash']);
    res['scrypt'] = calculate_scrypt(password, decodedSalt, s_data['N'], s_data['r'], s_data['p'], s_data['buflen'])

    print("all the hash", res)
    
    # submitting the solution 
    post_data(res)    
