#!env python3

import sys

ciphertext = []

def readFile(fname):
	try:
		with open(fname, "r") as ifile:
			lines = ifile.readlines()
			for line in lines:
				line = line.strip()
				try:
					int(line, 16)
				except:
					raise Exception()
				if not line:
					continue
				print(f'Reading: {line}')
				ciphertext.append(line)
		print("\nReading Done!\n\nIf you want to exit the program simply hit Ctrl + C\nHappy Hacking!\n")
	except:
		print("\nCould not open file\n\n-> Double check the file name\n-> Make sure the file is in the same directory as the python file\n-> Consider file extension i.e. cipher.txt\n-> Make sure that the ciphertext is in hexadecimal format\n\nExiting...\n")
		exit(2)

def Xor(s1, s2):
	res = ""
	for i in range(len(s1)):
		res += format(int(s1[i], 16) ^ int(s2[i], 16), '01x')
	return res

def main(pattern):
	for k in range(len(ciphertext)):
		for j in range(len(ciphertext)):
			if j == k or k > j:
				continue
			XOR_C = Xor(ciphertext[k], ciphertext[j])
			for i in range(len(XOR_C) - len(pattern) + 1):
				chr_ = Xor(pattern, XOR_C[i:len(pattern) + i])
				try:
					chr_ = bytes.fromhex(chr_).decode("ASCII")
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

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print(f"\nUsage: python {sys.argv[0]} <filename>\n\n-> This file should contain the ciphertexts separated by a new line each\n-> Consider file extension i.e. cipher.txt\n\nExiting...\n")
		exit(1)
	readFile(sys.argv[1])
	while True:
		try:
			print("\nEnter a common word:")
			pattern = input("> ").encode("utf-8").hex()
			main(pattern)
		except KeyboardInterrupt:
			print("\n\nExiting...\n")
			exit(0)