# AQA CS AS Notes

## 3.5 Fundamentals of data representation

### 3.5.1 Number systems
+ natural numbers

**definition**: those are numbers used for counting.

**examples**: 0,1,2,3,4
``` 
this is an area for code or examples etc

Counting uses natural number
A set of natural number can expressed as:
N={0,1,2,3...}

```

+ Integer numbers: Whole numbers (e.g. 1, 7, 145)
+ Rational numbers: Numbers that can be expressed as fractions (e.g. 0.5, 0.4, 0.125, 3.6, 1.333333...)
+ Irrational numbers: Can't be expressed in fractions (e.g. π, √2, √8)
+ Real numbers: Numbers that are rational, irrational or natural. Numbers that aren't imaginary in other words.
+ Ordinal numbers: Numbers used to indicate the position of a value in a sequence. (e.g. 1st, 3rd, 7th, 32nd)

### 3.5.2 Number bases
+ Base 2: those are binary numbers. example: 1010<sub>2</sub>. See [this site](https://bournetocode.com/projects/AQA_AS_Theory/pages/3-5.html) for more infomation
+ Base 10
+ Base 16
+ Conversion between denary, binary and hex

### 3.5.3 Units of information
+ Bit and bytes
+ Units of kilo, kilbi, mega, mebi, giga, gebi, tera, tebi

### 3.5.4 Binary number system

+ The rightmost value represents whether or not the number is negative. 0 = Positive, 1 = Negative
+ Unsigned binary: 100010 (34)
+ Binary arithemtics is comparable to decimal, with the fact that only 2 different values exist kept in mind.
+ Unsigned arithmetics: 100010+011001=111011
+ Signed arithemetics: (to be understood)
+ Signed binary in 2's compliment: 11011110 (-34)
+ Fixed point fractional numbers: 1110.0010 (14.125 in 8bit)

### 3.5.5 Information encoding system

#### Character form of a decimal digit
+ Basically, in ASCII and Unicode, numbers are coded as characters by default. As result, without the proper programming, 5+34=534.

#### ASCII
+ Stands for American Standard Code of Information Interchange.
+ Originally used 7 bits, but updated to use 8 bits in 1980.
+ Values were assigned to both uppercase and lowercase letters as well as non-printing control characters and more.
+ Only worked for Latin languages.
+ Decimal numbers was not represented by their equivalent in binary. (e.g. 0110100 will print '4', but has an actual decimal value of 52.)

#### Unicode
+ Unicode is the current encoding standard for giving every relevant character a binary value.
+ Comes in 8, 16 and 32 bit forms.
+ Created to allow all main languages and lesser known languages to be typed onto the computer.

#### Error checking and correction

##### Parity Bit:
+ Simplest form of error checking.
+ Works by both computers agreeing on whether the data has an odd or even parity.
+ A parity bit is added to the data to fit the parity. (e.g. Even parity, 011001010001 has an odd parity, therefore, the parity bit is '1'.)

##### Majority Voting:
+ Each bit in a piece of data is sent three times.
+ The receiving computer decides whether a bit is a 0 or 1, depending on which is the majority in each set. (e.g. 001=0, 111=1, 110=1) 

##### Check Sum:
+ Data is divided into bytes and an algorithm is applied to generate the check sum value.
+ Receiving computer receives the value and repeats the algorithm on the bytes it's received. If the resultant value is identical to the check sum value, the data received is supposedly correct.
+ E.g. 0001+0010+0011+0001=7. If the receiving computer also generates a value of 7, the data is supposdely uncorrupt.

##### Check Digit:
+ Works by adding an extra digit in front of or before the whole data value.
+ An example of check digit is barcodes, both Universal Product Code (UPC) and International Standard Book Number (ISBN).

+ Note, these error checkers are not full proof.

### 3.5.6 Representing images, sound and other data

#### Bit patterns, images,  sound  and other  data

#### Analogue and digital
+ Analogue data have continuous values with an infinite number potential values in between. (e.g. sound)
+ Digital data is desicrete and finite in size. (e.g. Binary data.)

#### Analogue and digital conversion
+ Either form of data can be converted into the other, by varying means.
+ An example of analogue to digital data would be recording sound. One way this is done is with sample resolution.
+ Digital data converted to analogue will never sound quite the same as the original analogue data. This is because the conversion involves making 'guesses' in order to be as accurate as possible.

#### Bitmapped graphics

#### Digital representation of sound
+ Sample resolution works by assigning a digital value to a specific datum. Higher sample rate/frequency equals better sound resolution.
+ They Nyquist/Sampling Theorem states that the sampling frequncy should be at least twice that of the highest recorded frequency of sound in order to accurately resemble the sound data.
+ A greater sample rate equals larger file sizes.
+ The standard sample frequncy is 44.1kHz. 
+ File size(in bits)= sample frequency x sample resolution x sound length (e.g. (4.5 mins x 60 = 150s) x 16 bit resolution x 441000 Hz = 1905120000 b = 23.6 MB)

#### Musical Instrument Digital Interface (MIDI)
+ Audio file type that works by generating instructions on producing the sound, instead of recording the sound itself (MIDI event messages).
+ Primarily used for music.
+ As a result, it has a smaller file size and smaller load times.
+ Completely editable.

#### Data compression
+ Used to significantly reduce file size to much more manageable levels and for quicker file transfer.
+ Exists as both lossy and lossless compression.

#### Encryption
+ Original message/ data is called plaintext.
+ Encrypted data is called cipher text.
+ The method is called a cipher.
+ The secret code for encrypting/decrypting data is called the key.
+ Only unbreakable cipher is the Vernam Cipher.

##### Vernam Cipher
+ Works by using a true random one-time key (aka one-time pad) and applying XOR to the plaintext.
+ XOR generates datum, based on whether the plaintext and the key datum is identical or not. (e.g. 1+1=0, 0+0=0, 1+0=1.)