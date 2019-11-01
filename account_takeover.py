r = 0x69a726edfb4b802cbf267d5fd1dabcea39d3d7b4bf62b9eeaeba387606167166

# signature 1
s1 = 0x2bbd9c2a6285c2b43e728b17bda36a81653dd5f4612a2e0aefdb48043c5108de
# msg hash 1
z1 = 0x4f6a8370a435a27724bbc163419042d71b6dcbeb61c060cc6816cda93f57860c

# signature 2
s2 = 0x7724cedeb923f374bef4e05c97426a918123cc4fec7b07903839f12517e1b3c8
# msg hash 2
z2 = 0x350f3ee8007d817fbd7349c477507f923c4682b3e69bd1df5fbb93b39beb1e04

# prime order
p = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

def inverse_mod(a, n):
    return pow(a, n - 2, n)

k = (z1 - z2) * inverse_mod(s1 - s2, p) % p
privkey = (s1 * k - z1) * inverse_mod(r, p) % p
privkey_neg = (-s1 * (-k % p) - z1) * inverse_mod(r, p) % p

print("k:{:x}".format(k))
print("-k:{:x}".format(-k%p))
if privkey == privkey_neg:
    print("privkey:{:x}".format(privkey))
