from itertools import cycle
def encrypt_decrypt(plain_text, key):
    # returns plain text by repeatedly xoring it with key
    data = plain_text
    xored = ''.join([chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key))])
    return xored

def hex_to_text(hex):
    return bytes.fromhex(hex).decode('utf-8')

question = input("Hex or Text?")
text = input("Enter input: ")
if question == "Hex":
    text = hex_to_text(text)

print(text)
key = input("Enter key: ")

print("Input: ", input)
print(encrypt_decrypt(text, key).hex())


