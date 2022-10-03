ifile = open("level2_data", "rb")
ifile = ifile.read()
ifile1 = ifile
ifile = ifile.hex()
ifile = str(ifile)
ifile = ifile[::-1]
length = len(ifile)

str1 = (bytes.fromhex(ifile[0:96]).decode('utf-8'))
str2 = (bytes.fromhex(ifile[100:length-4]).decode('utf-8'))

print(str1)
print(str2[::-1] + str1[::-1])
print(ifile1)

