from hashlib import sha256
import math
import requests
import json 

base_url='https://hackattic.com/challenges'

def get_data():
    res = requests.get(f'{base_url}/mini_miner/problem?access_token=ab17bddaef9e90e4')
    response = json.loads(res.text)
    return response

def get_the_hash(block):
    digest = sha256(block.encode()).hexdigest()
    return digest
    

def make_data_jsons(block,nonce):
    block['nonce']=nonce
    s_data=json.dumps(block,sort_keys=True,separators=(',', ':'))
    return s_data    

def countZeros(x):     
    # Keep shifting x by one until
    # leftmost bit does not become 1.
    count=0
    for i in x:
        if i!='0':
           break 
        else:
            count+=1
    return count

def get_check(block,difficulty,nonce):
    os='0'* math.ceil(difficulty/4)
    while True:
        json_s=make_data_jsons(block,nonce)
        hash_val=get_the_hash(json_s)
        if hash_val.startswith(os):
            return nonce
        else :
            nonce=nonce+1
def send_ans(nonce):
    payload={"nonce":nonce}
    response=requests.post(f'{base_url}/mini_miner/solve?access_token=ab17bddaef9e90e4',json=payload)
    return response.json()
    
if __name__ =='__main__':
    data=get_data()

    difficulty=data['difficulty']
    block =data['block']
    nonce=block['nonce']
    ans=get_check(block,difficulty,0)
    print(send_ans(ans))
 