"""
Simhash Encoding Python Script:

This Python script implements Simhash encoding, a technique used for efficient near-duplicate detection in large datasets. 

Key Features:
Simhash Generation: The script calculates the simhash for the data present on the website or URL given by the user.

How to Use:
Run you file as given below:

>>> python3 simhash.py   URL1   URL2

Submitted by: Divyansh Mishra
Completion date: 03/03/2024
"""

import string
import sys
from myCrawler import crawl

urls = sys.argv[1:]
url1 = urls[0] # input("Enter the first url: ")
url2 = urls[1] # input("Enter the second url: ")

text1 = crawl(url1)
text2 = crawl(url2)

def tokenize_words(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words

tokenized_words1 = tokenize_words(text1)
tokenized_words2 = tokenize_words(text2) # word_tokenize(text2)

def make_dict(words):
    words = clean_word_list(words)
    words = makeNgram(words, 5)
    word_dict = {}
    try:
        for word in words:
            if (len(word)>=3 and len(word) <=45):
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
        return word_dict
    except Exception as e:
        return (f"An error occurred: {e}")


def genHash_dict(word_dict):
    """
    Returns the dictionary containing key as a unique word and value as a tuple having the first element as its frequency and the second as its bit representation
    """
    p = 53
    for key in word_dict:
        sum = 0
        for i in range(len(key)):
            value = ord(key[i])*(p**i)
            sum += value
        sum = sum % 2**64

        bin_value_base = bin(sum)[2:]
        bin_value = bin_value_base.zfill(64)

        word_dict[key] = (word_dict[key], str(bin_value))
    return word_dict


def genHash(word_dict_2):
    """
    Returns the 64 bit hash function
    """
    hashCode = ''
    for i in range(64):
        sum = 0
        for key in word_dict_2:
            bin_value = word_dict_2[key][1]
            coeff = -1 if (int(bin_value[i]) == 0) else 1
            sum += coeff * word_dict_2[key][0]

        hashCode = (hashCode + "1") if (sum>=0) else (hashCode + "0")
    return hashCode


def makeNgram(wordList, n=5):
    '''
    Makes n (5 default) gram with 2 in common
    '''
    n = 5
    n_gram = []
    if n > len(wordList) or n<=0:
        print("Invalid size of n gram")
    else:
        for i in range(0,len(wordList),3):
            if len(wordList[i:i+n]) == n:
                n_word = ""
                for w in wordList[i:i+n]:
                    n_word += w + " "
                n_gram.append(n_word)
    return n_gram

def count_different_bits(binary1, binary2):
    if len(binary1) != 64 or len(binary2) != 64:
        raise ValueError("Both binary numbers must be 64 bits long")
    different_bits_count = sum(bit1 != bit2 for bit1, bit2 in zip(binary1, binary2))
    return different_bits_count


def clean_word_list(word_list):
    word_list = [''.join(char for char in word if char not in string.punctuation) for word in word_list]
    return word_list


hash1 = genHash(genHash_dict(make_dict(tokenized_words1)))
hash2 = genHash(genHash_dict(make_dict(tokenized_words2)))
diff = count_different_bits(hash1, hash2)
similar = (64 - diff)
print(64 - diff)
print("Percentage similarity: ", (similar/64)*100, "%")