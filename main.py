#!/usr/bin/env python3

import helpers, argparse


parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-m',
					dest='mode',
					choices=['1', '2', '3', '4'],
					help='1: Decrypt with one key\n2: Decrypt multiple cipher text with multiple keys\n3: Decrypt without key (multiple cipher text required)\n4: Encrypt multiple text with the same key (INSECURE)\n5: Encrypt multiple text with multiple keys (Number of keys = number of plain text)',
					required=True
					)
parser.add_argument('-c',
					dest='cipherfile',
					help='File containing ciphertext separated with a new line each'
					)
parser.add_argument('-p',
					dest='plainfile',
					help='File containing plain text, separated by a new line each if multiple'
					)
parser.add_argument('-k',
					dest='keyfile',
					help='File containing key to encrypt/decrypt'
					)
args = parser.parse_args()


def decryptWithoutKey(cipher):
	file = helpers.File(cipher)
	file.read()
	if not file.isHex():
		print("[-] The proivded format is not HEX")
		exit()
	proc = helpers.Decryption(file.data)
	proc.startDecrypting()


def decryptWithOneKey(cipher, key):
	cipherfile = helpers.File(cipher)
	cipherfile.read()
	if not cipherfile.isHex():
		print("[-] The proivded format is not HEX")
	keyfile = helpers.File(key)
	keyfile.read()
	proc = helpers.Decryption(cipherfile.data, keyfile.data)
	proc.decryptWithOneKey()
	for i, plain in enumerate(proc.plaintext):
		print(f"{i+1}: {plain}")


def main():
	mode = args.mode
	# Decrypt with one key
	if mode == '1':
		if not args.cipherfile:
			print('[-] Please provide a file containing cipher text')
			exit()
		if not args.keyfile:
			print('[-] Please provide a file containing key')
			exit()
		decryptWithOneKey(args.cipherfile, args.keyfile)

	# Decrypt with multiple keys
	elif mode == '2':
		print("Decrypt with multiple keys: TODO")

	# Decrypt without key
	elif mode == '3':
		if not args.cipherfile:
			print('[-] Please provide a file containing cipher text')
			exit()
		decryptWithoutKey(args.cipherfile)

	# Encrypt with one key
	elif mode == '4':
		print('Encrypt with one key: TODO')

	# Encrypt multiple with multiple keys
	elif mode == '5':
		print('Encrypt multiple with multiple keys: TODO')

if __name__ == "__main__":
	main()
