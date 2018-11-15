import numpy as np

english_freq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33,
                'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41,
                'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98,
                'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

pairs = english_freq.items()
english_freq_array = np.array([i[1] for i in sorted(pairs, key=lambda x: x[0])])

def error_calc(guess_text):
    guess_freq = calc_freq(guess_text)
    error = np.multiply(guess_freq - english_freq_array, guess_freq - english_freq_array)
    sub = guess_freq - english_freq_array
    return np.sum(error)/26

def calc_freq(text):
    text = text.upper()
    count = np.zeros(26)
    for c in text:
        index = ord(c)-65
        count[index] = count[index] + 1
    return count / len(text) * 100

def caeser_decode(text, shift):
    text = text.upper()
    guess_text = ""
    for c in text:
        letter = (ord(c) - shift)
        if letter < 65:
            letter = 91 + letter - 65
        guess_text = guess_text + chr(letter)
    return guess_text

def guess_shift(text):
    errors = np.zeros(26)
    for i in range(0,26):
        errors[i] = error_calc(caeser_decode(text, i))
    std = np.std(errors)
    mean = np.mean(errors)
    argmins = []
    for i in range(0,26):
        if errors[i] < mean - std:
            argmins.append(i)
    return argmins, errors


if __name__ == "__main__":
    #text = "gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk"
    text = "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"
    argmins, errors = guess_shift(text)
    for shift in argmins:
        print(caeser_decode(text, shift))
    print(errors)
