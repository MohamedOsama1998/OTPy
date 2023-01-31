#!/usr/bin/env python3

class File:
	def __init__(self, filename):
		self.filename = filename
		self.data = []

	def read(self):
		try:
			with open(self.filename, 'r') as ifile:
				lines = ifile.readlines()
		except:
			print(f"[-] Error openning file '{self.filename}'")
			exit()

		for line in lines:
			line = line.strip()
			if not line:
				continue
			print(f"[+] Reading line: {line}")
			self.data.append(line)
		print(f"[+] Reading file '{self.filename}' Done\n")
		return self.data

	def isHex(self):
		if self.data:
			for line in self.data:
				try:
					int(line, 16)
				except:
					return False
			return True
		else:
			print("[-] No files is read yet")
			return False

#############################################################################

class operation:
	def xor(s1, s2):
		res = ""
		for i in range(len(s1)):
			res += format(int(s1[i], 16) ^ int(s2[i % len(s2)], 16), '01x')
		return res

	def str2hex(text):
		return text.encode('utf-8').hex()

	def hex2str(text):
		return bytes.fromhex(text).decode("ASCII")

#############################################################################

class Encryption:
	def __init__(self, plaintext, key):
		self.plaintext = plaintext
		self.ciphertext = []
		self.key = key

	def encrypt(self):
		print("Encrypt with key")
		# TODO

#############################################################################

class Decryption:
	def __init__(self, ciphertext, key=[]):
		self.ciphertext = ciphertext
		self.plaintext = []
		self.key = key

	def decryptWithKey(self):
		# TODO
		print("Decrypt with key")

	def decryptWithoutKey(self, pattern):
		# TODO: Fix a bug where symbols can cause issues
		ciphertext = self.ciphertext
		if len(ciphertext) < 1:
			print("[-] Not enough ciphertext, please provide at least 2") 
			exit()
		pattern = operation.str2hex(pattern)
		for k in range(len(ciphertext)):
			for j in range(len(ciphertext)):
				if k >= j:
					continue
				XOR_C = operation.xor(ciphertext[k], ciphertext[j])
				for i in range(len(XOR_C) - len(pattern) + 1):
					chr_ = operation.xor(pattern, XOR_C[i:len(pattern) + i])
					try:
						chr_ = operation.hex2str(chr_)
						if " " in chr_:
							chr_tmp = chr_.split(" ")
							for chr_tmp2 in chr_tmp:
								if not chr_tmp2.isalpha():
									raise Exception()
						else:
							if not chr_.isalpha():
								continue
					except:
						continue
					print(f'Found pattern at position {i}: {chr_} between ciphers {k+1} and {j+1}')

	def startDecrypting(self):
		print("[+] Start guessing...")
		while True:
			try:
				pattern = input("\n> ")
				self.decryptWithoutKey(pattern)
			except KeyboardInterrupt:
				print("\nExiting...\n")
				exit()

	def decryptWithOneKey(self):
		ciphertext = self.ciphertext
		key = self.key[0]
		if not ciphertext:
			print('[-] Cipher text was not provided')
			exit()
		if not key:
			print('[-] Key was not provided')
			exit()
		for cipher in ciphertext:
			plain = operation.hex2str(operation.xor(cipher, operation.str2hex(key)))
			self.plaintext.append(plain)
		return self.plaintext
