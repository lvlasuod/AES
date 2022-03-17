# AES
###### Advanced Encryption Standard
```
 This project is for Couresework 1.
 subject: Implementation of ADVANCED ENCRYPTION STANDARD (AES) algorithm.  
```

Advanced Encryption Standard or AES, a full algebraic encryption standard, is also known as the successor of DES.
It divides the plaintext into 128-bit blocks and takes 128, 192 or 256-bit key to encrypt the plaintext.

Let’s have a look at the advantages and disadvantages of AES:



###### Advantages:
- It can be implemented in both hardware and software.
- Long key sizes (128, 192 and 256 bits) makes AES more robust against hacking.
- Three keys give the users a choice as per their requirement based upon speed and security.
- It is ubiquitous. That is, being defined as a standard by US government; it is supported by most vendors. Most systems used today support AES.
- No known crypt-analytical attack against AES has been found till date.

###### Disadvantages:
- Though it can be implemented in both hardware and software, it is complex to implement in software.
- It uses very simple encryption operations and simple key schedule which makes it vulnerable to attack.


### Specifications:
- Block size (in bits):128
- Key size (in bits) (one to be chosen): 128, 192, 256
| AES divides plaintext into 128-bit (16 bytes) block each and treats each block as a 4×4 array. The block is then encrypted using one of the three different key lengths, 128, 192 and 256 bits.
- Number of rounds: 10 for 128-bit key | 12 for 192-bit key | 14 for 256-bit key
- AES was designed by Vincent Rijmen and Joan Daemen.
- AES is comparatively faster.
- AES has large secret key comparatively, hence, more secure.
- Steps: SubBytes, ShiftRows, MixColumns, AddRoundKey















```
 Contributors: Masoud, Diego, Lukas
```
:+1: :shipit:
