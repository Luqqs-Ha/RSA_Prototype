import math
import random


def miller_rabin(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def binary_digits_to_Integer(B):
    n = 0
    pow2 = 1
    for i in reversed(range(len(B))):
        n += pow2 * B[i]
        pow2 *= 2
    return n


def random_odd_value(bits):
    B = [0] * bits
    B[0] = 1
    B[-1] = 1
    for i in range(1, bits - 1):
        B[i] = random.randint(0, 1)
    return binary_digits_to_Integer(B)


def generate_probable_prime(bits):
    while True:
        n = random_odd_value(bits)
        if miller_rabin(n, 40):
            print(n)
            return n


def ggT(a, b):
    if a == 0:
        return b
    else:
        return ggT(b % a, b)


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def encrypt(a):
    return pow(a, e, n) # a hoch e mod n


def decrypt(a):
    return pow(a, d, n) # a hoch d mod n


print("p and q : ")
prim_1 = generate_probable_prime(1500)
prim_2 = generate_probable_prime(1500)

n = prim_1 * prim_2
phi = (prim_1 - 1) * (prim_2 - 1)

e = 2 ** 16 + 1

d = modinv(e, phi)  # decryption

print("n     = " + str(n))
print("phi  = " + str(phi))
print("e     = " + str(e))
print("d     = " + str(d))

plain = int(input("number to encrypt : "))
encrypted = encrypt(plain)
decrypted = decrypt(encrypted)
print(encrypted)
print("encrypted and decrypted test :" + str(decrypted))



