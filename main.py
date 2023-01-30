#!env python3

import helpers

# TODO: Add args for options

def decryptWithoutKey(filename):
	file = helpers.File(filename)
	file.read()
	if not file.isHex():
		print("[-] The proivded format is not HEX")
		exit()
	if len(file.data) < 1:
		print("[-] Not enough ciphertext, please provide at least 2") 
		exit()
	proc = helpers.Decryption(file.data)
	proc.startDecrypting()

def main():
	decryptWithoutKey('cipher2')

if __name__ == "__main__":
	main()

