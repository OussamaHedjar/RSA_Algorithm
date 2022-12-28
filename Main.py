from RSA import RSA

print("--------------------- RSA Algorithm ---------------------")
print("choose the values of p and q, MAKE SURE BOTH ARE PRIME!")
p = input("enter value of p:")
q = input("enter value of p:")
rsa = RSA(int(p), int(q))

print("choose to either let e be a random value or a value of your choice, PRESS 0 FOR RANDOM NUMBER")
print(rsa.ComputeE())
n = input("the value of choice is:")
print("your public key is: ", rsa.KeyGeneration(int(n)))
# print the table so user can do the map to write a text.
print()
print("a = 0, b = 1, c = 2, d = 3, e = 4, f = 5, g = 6, h = 7, i = 8, j = 9, k = 10, l = 11, m =12")
print("n = 13, o = 14, p = 15, q = 16, r = 17, s = 18, t = 19, u = 20, v = 21, w = 22, x = 23, y = 24, z = 25")
print("A = 26, B = 27, C = 28, D = 29, E = 30, F = 31, G = 32, H = 33, I = 34, J = 35, K = 36, L = 37, M = 38")
print("N = 39, O = 40, P = 41, Q = 42, R = 43, S = 44, T = 45, U = 46, V = 47, W = 48, X = 49, Y = 50, Z = 51, "
      "Space = 52")
print()
print("For example, if user wished to encrypt Hello World, the user must enter: 3304111114524814171103")
text = input("to enter text use table above, Note: before a single digit, 0 must get added.: ")
numbers = [item_1 + item_2 for item_1,
                               item_2 in zip(text[::2], text[1::2])]

# convert each item to int type
for i in range(len(numbers)):
    # convert each item to int type
    numbers[i] = int(numbers[i])

# encrypt in rsa:
encrypted_data = rsa.Encryption(numbers)
print("Encrypted text: ", "".join([str(x) for x in encrypted_data]))

# decrypt in rsa:
decrypted_data = rsa.Decryption()
print("Decrypted text: ", "".join([str(x) for x in decrypted_data]))
