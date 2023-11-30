# Zipper is stuck

## Description
As an elite cyber investigator, you receive an anonymous tip about a suspicious network activity . Unravel the encrypted messages, follow the digital trail, and work with your team to retrieve the confidential information. The message has a 3 digit lock.

## Solution
* We are provided with a pcap file
* Open the pcap file in wireshark
* Save the `flag.zip` from http objects from the capture  
```File > Export Objects > HTTP > Select flag.zip > Save```
* Crack password using john
	* `zip2john flag.zip > zip.hash`
	* `john zip.hash`
* Password: `451`
* Extract the zip file using the password `451`
* We get a file named `flag.txt`  
`cat flag.txt`
* Flag:   
`KPMG_CTF{P@$$w0rd_i$_KPMG}`


### Alternative ways to crack the password
1. https://www.lostmypass.com/file-types/zip/
2. Write a script which will try all the 3 digit combinations

