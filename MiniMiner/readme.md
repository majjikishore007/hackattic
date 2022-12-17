# Mini miner


Algo

1 Get the data request.get(url)

```
    Response JSON will be in the following format:
    difficulty: how many bits (high order) need to be 0 in the SHA256 hash
    block:
    nonce: the nonce you will need to find so that the hash meets the criteria, None
    data: some dummy data that makes up the block

```
2. Sort the block in alphabetical order.
3. Seralize the block with out any white spaces
4. Start with 0 as nonce and update the block with the nonce and get the hash256
5. Check if difficulty is equal to the number of leading 0s of the hash 
6  If not increament the nonce value and repeat the process 
7 Else return the nonce value 


