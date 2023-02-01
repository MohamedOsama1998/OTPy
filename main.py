#!/usr/bin/env python3

import helpers, argparse


parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-m',
					dest='mode',
					choices=['1', '2', '3', '4', '5'],
					help='1: Decrypt with one key\n2: Decrypt multiple cipher text with multiple keys\n3: Decrypt without key (multiple cipher text required)\n4: Encrypt multiple text with the same key (INSECURE)\n5: Encrypt multiple text with multiple keys (Number of keys = number of plain text)',
					required=True
					)
parser.add_argument('-c',
					dest='cipherfile',
					help='File containing ciphertext separated with a new line each (IN HEX FORMAT)'
					)
parser.add_argument('-p',
					dest='plainfile',
					help='File containing plain text, separated by a new line each if multiple (IN ASCII FORMAT)'
					)
parser.add_argument('-k',
					dest='keyfile',
					help='File containing key to encrypt/decrypt (IN ASCII FORMAT)'
					)
parser.add_argument('-o',
					dest='writeToFile',
					help='Write output to file'
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


def decryptWithMultipleKeys(cipher, key):
	# TODO
	cipherfile = helpers.File(cipher)
	cipherfile.read()
	keyfile = helpers.File(key)
	keyfile.read()
	proc = helpers.Decryption(cipherfile.data, keyfile.data)
	return proc.decryptWithMultipleKeys()


def decryptWithOneKey(cipher, key):
	cipherfile = helpers.File(cipher)
	cipherfile.read()
	if not cipherfile.isHex():
		print("[-] The proivded format is not HEX")
	keyfile = helpers.File(key)
	keyfile.read()
	proc = helpers.Decryption(cipherfile.data, keyfile.data)
	return proc.decryptWithOneKey()


def encryptWithOneKey(plain, key):
	plainfile = helpers.File(plain)
	plainfile.read()
	keyfile = helpers.File(key)
	keyfile.read()
	proc = helpers.Encryption(plainfile.data, keyfile.data)
	return proc.encryptWithOneKey()


def encryptWithMultipleKeys(plain, key):
	plainfile = helpers.File(plain)
	plainfile.read()
	keyfile = helpers.File(key)
	keyfile.read()
	proc = helpers.Encryption(plainfile.data, keyfile.data)
	return proc.encryptWithMultipleKeys()


def main():
	result = []
	mode = args.mode
	# Decrypt with one key
	if mode == '1':
		if not args.cipherfile:
			print('[-] Please provide a file containing cipher text')
			exit()
		if not args.keyfile:
			print('[-] Please provide a file containing key')
			exit()
		result = decryptWithOneKey(args.cipherfile, args.keyfile)

	# Decrypt with multiple keys
	elif mode == '2':
		if not args.cipherfile:
			print('[-] Please provide a file containing cipher text')
			exit()
		if not args.keyfile:
			print('[-] Please provide a file containing keys')
			exit()
		result = decryptWithMultipleKeys(args.cipherfile, args.keyfile	)

	# Decrypt without key
	elif mode == '3':
		if not args.cipherfile:
			print('[-] Please provide a file containing cipher text')
			exit()
		decryptWithoutKey(args.cipherfile)

	# Encrypt with one key
	elif mode == '4':
		if not args.plainfile:
			print(f"[-] Please provide a file containing plan text to encrypt")
			exit()
		if not args.keyfile:
			print(f"[-] Please provide a file containing a key")
			exit()
		result = encryptWithOneKey(args.plainfile, args.keyfile)

	# Encrypt multiple with multiple keys
	elif mode == '5':
		if not args.plainfile:
			print(f"[-] Please provide a file containing plan text to encrypt")
			exit()
		if not args.keyfile:
			print(f"[-] Please provide a file containing keys")
			exit()
		result = encryptWithMultipleKeys(args.plainfile, args.keyfile)

	if result:
		for res in result:
			print(res)
		if args.writeToFile:
			with open(args.writeToFile, 'w') as out:
				for res in result:
					out.write(res + '\n')
	else:
		print("[-] Nothing to show.")
		exit()


if __name__ == "__main__":
	main()
