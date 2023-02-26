# OTP Key Reuse Exploit

---

## Usage

This tool can be used in different ways to encrypt/decrypt One-Time-Pads, the following are examples:

1. Decrypt one or more cipher text(s) with one key:

```shell
$ python3 main.py -m 1 -c ciphertext.txt -k key.txt
```

2. Decrypt multiple cipher texts with multiple keys:

```shell
$ python3 main.py -m 2 -c ciphertext.txt -k key.txt
```

3. Decrypt without a key, Key reuse vulnerability exploit, must provide at least 2 cipher texts:

```shell
$ python3 main.py -m 3 -c ciphertext.txt
```

4. Encrypt with one key (INSECURE):

```shell
$ python3 main.py -m 4 -p plaintext.txt -k key.txt
```

5. Encrypt with multiple keys (RECOMMENDED):

```shell
$ python3 main.py -m 5 -p plaintext.txt -k key.txt
```

---
 
## How does it work? 

The one time pad (OTP) is a type of stream cipher that is a perfectly secure method of encryption. It's very simple to implement and is perfectly secure as long as the length of the key is greater than or equal to the length of the message. That's it's major downfall. However, it also requires that the key never be used more than once. This tutorial shows what happens when you re-use a key to encrypt more than one message.

Let's begin with a brief description of OTP and how it works. Let's take the following message and key:

message = `Hello World`
key = `supersecret`

If we convert both the message and key to hex strings, we get the following:

message = `48656c6c6f20576f726c64`
key = `7375706572736563726574`

If we do a simple XOR of the two hex strings we get the following cipher-text:

cipher-text = `3b101c091d53320c000910`

If we XOR the cipher-text with the key, we can recover the plain-text. That's how OTP works. Without the key, you have no way of uncovering the plain-text.

Let's consider what happens when you have two messages encrypted with the same key. Take the following two messages and key:

message1 = `Hello World`
message2 = `the program`
key = `supersecret`

If we convert each message and the key to hex strings, and then encrypt each message using a simple XOR with the key, we'll get the following cipher-texts:

cipher-text1: `3b101c091d53320c000910`
cipher-text2: `071d154502010a04000419`

Let's say that all we have is the two cipher-texts and the knowledge that they were encrypted with a supposed OTP; however, they were both encrypted with the same key. To attack this encryption and uncover the plain-text, follow the steps below.

1. Guess a word that might appear in one of the messages
2. Encode the word from step 1 to a hex string
3. XOR the two cipher-text messages
4. XOR the hex string from step 2 at each position of the XOR of the two cipher-texts (from step 3)
5. When the result from step 4 is readable text, we guess the English word and expand our crib search. If the result is not readable text, we try an XOR of the crib word at the next position.

Step 1 seems difficult (guessing a word that might appear in one of the messages), but when you think about it, the word "the" is the most commonly used English word. So, we'll start with assuming "the" is in one of the messages. After encoding "the" as a hex string, we'll get "746865". That takes care of steps 1 and 2. If we XOR the two cipher-texts, we'll get the following result:

cipher-text1 XOR cipher-text2 = `3c0d094c1f523808000d09`

The next step is to XOR our crib word `746865` at each position of the XOR of the cipher-texts. What we'll do is slide `746865` along each position of `3c0d094c1f523808000d09` and analyze the result. After the first XOR, we get the following result:
`485656`

When we convert the hex string `48656c` to ASCII, we get the following text, `Hel`. This takes us to step 5 from above. Because this looks like readable text, we can assume that the word `the` is in the first position of one message. If we didn't get readable text, we would slide `746865 (the)` one position to the right and try again (and keep repeating until the end of `3c0d094c1f523808000d09`).

Note that we don't know which message contains the word "the". It could be in either message1 or message2. Next, we need to guess what the word "Hel" is when fully expanded. It could be "Help", "Hello", etc. If we guess "Hello", we can convert "Hello" to a hex string, we get "". We then XOR it with the XOR of the two cipher-texts (just like we did with "the"). Here's the result:
"7468652070"

`7468652070`  when converted to ASCII, is "the p". We then repeat the process, guessing what "the p" might be when expanded and then XOR that result with the XOR of the cipher-texts. Granted, guessing what "the p" might expand to is not super easy, but you get the idea. If we were to guess "the program", convert it to a hex string, and XOR it with the XOR of the cipher-texts, we'll get "Hello World".

This is called crib dragging.

Source : 
[Travis Dazell Blog](http://travisdazell.blogspot.com/2012/11/many-time-pad-attack-crib-drag.html)

---

Happy Hacking!
