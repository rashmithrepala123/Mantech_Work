def encrypt_decrypt(plain_text, key):
    
    # returns plain text by repeatedly xoring it with key
    data = plain_text
    xored = ''.join([chr(ord(x)^ord(y)) for (x,y) in zip(data, key)])
  
    return xored


    
question = input("Encrypt or Decrypt?")

      
plain_text = b'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
key = input("Enter key: ")
  
print("Plain text: ", plain_text)

if question == "E":
    print("Encrypted as: ", encrypt_decrypt(plain_text, key))
else:
    print("Decrypted as: ", encrypt_decrypt(plain_text, key))
  
