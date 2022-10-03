# Schedule

## *File Format RE: 7/5/22 - 7/7/22*
* Finished Level 1 by figuring out that the decryption cipher was XOR. This was because many of the phrases in the hex editor file was repeating
* Then, after noticing the JFIF at the beginning of the decoded file, I saved the file as a JPG and put it into a paint to get the picture
* Created a python script that encrypts using the XOR cipher

## *File Format RE: 7/8/22 - 7/11/22*
* Working on Level 2 of Reverse Engineering
* Due to the small size of the payload, I realized that it was a text file format
* I also realized that the characters are spaced out, which I interpreted as the separation of words
* *-7* repeated a few times, leading me to think that it was words like *is*, *at*, *of*
* To decrypt the data, you have to reverse the bytes, which I did in CyberChef
* Created a python script to read in the *level2_data* and decode to text

## *File Format RE: 7/12/22 - 7/14/22*
* Working on Level 3 of Reverse Engineering
* Due to the very large payload size, I am thinking that this is an mp3 or mp4 video
* The file has many repeating phrases, such as *Fè’*, *XöŒ*, and others
* XORed the file with the key as *XöŒ* and extracted files (.zlib files)
* Figured out the 3 files that have been obfuscated: doctor.jpg, happy.jpg, and dance.mp4
* Found the JPG file signature and decoded the doctor.jpg

## *Automated APK Analysis: 7/20/22 - 7/21/22*
* Using OpenSSL to examine the RSA Certification
* Working on converting the AndroidManifest.xml file to text file

## *Group Project: 7/25/22 - 7/26/22*
* Recognized that the byte *1a* was repeated in the beginning and a lot at the end of the hex editor file
* Used XOR cipher *1a* to discover the first layer of the Tesseract Infinity Stone using CyberChef
* Gnu Privacy Guard (GPG) uses AES Encryption, and I have tried that decryption in CyberChef
* Tried Hex to a PEM certificate and tried swapping endianness
* Used autopsy to find deleted files in the DFEND_2020 disc image file
* With autopsy, I was able to extract files and databases such as “gratefuluniverse.db”, “$RR1YJK2.db”, etc

## *Group Project: 7/27/22 - 7/28/22*
* Converted the Game of Stones from base 64 to jpg and it is several rocks
* Found a .fat file in the Carved Files folder  
* Learned that *xxd* command creates a hex dump in Linux
* Traversed through the TCP streams of the Wireshark of the packet
* Found that Stream 112 started with ELF, so I realized that this should be a possible file
* Converted it to raw text and copied into a hex editor
* Moved the file into a Kali Linux machine and executed the ELF File
* Outputted *We Are Groot*, but produced a text file with the stone 2 text in it

## *Presentations: 8/01/22 - 8/08/22*
* Worked on presentations
* Presented on 8/08/2022

## *Writeups: 8/09/22 - 8/10/22*
* Worked and completed the writeups for File Format Reverse Engineering and Wireshark projects
* Completed Reflection and Schedule




