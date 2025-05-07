#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 18:52:08 2024

@author: Dhananjoy Bhuyan
"""
import webbrowser
import os
import string
from random import randint as rnt
from random import choice as chs
import detect_typo as dt

__version__ = '1.0.0'

__all__ = ["encrypt",
           "decrypt",
           "encryptor_GUI",
           "terminal_UI"]


def encrypt(message: str = None):

    # check if message is given
    if message:
        # The mapping dict:
        letters_to_numbers = {
            " ": 0,
            "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
            "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
            "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
            "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36,
            "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46,
            "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52,
            "1": 53, "2": 54, "3": 55, "4": 56, "5": 57, "6": 58, "7": 59, "8": 60, "9": 61, "0": 62,
            "!": 63, "@": 64, "#": 65, "$": 66, "%": 67, "^": 68, "&": 69, "*": 70, "(": 71, ")": 72,
            "-": 73, "_": 74, "=": 75, "+": 76, "`": 77, "~": 78, "[": 79, "{": 80, "]": 81, "}": 82,
            "|": 83, ":": 84, ";": 85, '"': 86, "'": 87, ",": 88, "<": 89, ".": 90, ">": 91, "?": 92,
            "/": 93, "\\": 94, "\n": 95, "\a": 96
        }
        message = str(message)
        # encryption level 1
        key_base = []
        num_message = []
        for i in message:
            rand_num = rnt(1, 2934802984357)
            key_base.append(str(rand_num))
            num_message.append(
                str((letters_to_numbers[i] + (rand_num*3))))

        num_message = '-'.join(num_message)

        # encryption level 2

        # encrypt key_base to make the final key
        key = []
        # This funtion is for obfuscation of the encrypted message

        def generate_random_strings():
            characters = list((string.digits + '.'))
            obfuscation_string = ''
            for i in range(46):
                obfuscation_string += chs(characters)

            return obfuscation_string

        for i in key_base:
            rand_num2 = rnt(12, 345349599)
            key.append(str(int(i) + (rand_num2*2)) +
                       f'.{rand_num2}')

        obfuscation_marker = generate_random_strings()
        num_message += obfuscation_marker + generate_random_strings()

        key = '-'.join(key)
        key = obfuscation_marker + '=.' + key

        # encryption level 3: obfuscation

        final_message = key + '.=' + generate_random_strings() + '=.' + num_message

        return final_message


def decrypt(enc_msg: str) -> str:

    if any(letter in enc_msg for letter in string.ascii_letters):
        return None
    try:
        # number to letter mapping:
        numbers_to_letters = {'0': ' ', '1': 'a', '': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z', '27': 'A', '28': 'B', '29': 'C', '30': 'D', '31': 'E', '32': 'F', '33': 'G', '34': 'H', '35': 'I', '36': 'J', '37': 'K', '38': 'L', '39': 'M', '40': 'N', '41': 'O', '42': 'P', '43': 'Q', '44': 'R', '45': 'S', '46': 'T', '47': 'U',
                              '48': 'V', '49': 'W', '50': 'X', '51': 'Y', '52': 'Z', '53': '1', '54': '2', '55': '3', '56': '4', '57': '5', '58': '6', '59': '7', '60': '8', '61': '9', '62': '0', '63': '!', '64': '@', '65': '#', '66': '$', '67': '%', '68': '^', '69': '&', '70': '*', '71': '(', '72': ')', '73': '-', '74': '_', '75': '=', '76': '+', '77': '`', '78': '~', '79': '[', '80': '{', '81': ']', '82': '}', '83': '|', '84': ':', '85': ';', '86': '"', '87': "'", '88': ',', '89': '<', '90': '.', '91': '>', '92': '?', '93': '/', '94': '\\', '95': '\n', '96': '\x07'}

        # get the variables back.
        obfuscation_marker = enc_msg[:enc_msg.find("=.")]
        key = enc_msg[enc_msg.find("=.") + 2:enc_msg.find(".=")]

        num_message = enc_msg[enc_msg.find("=.", enc_msg.find("=.") + 2) + 2:]

        # key to key_base
        key = key.split("-")
        key_base = []

        for i in key:
            i = i.split(".")
            num = int(i[0])
            rand_num2 = int(i[1])
            key_base.append(num - (rand_num2*2))

        # Extract the message
        message = num_message[:num_message.find(obfuscation_marker)]
        message = message.split("-")

        # Form the message.
        decrypted_message = ''
        for number, rand_num in zip(message, key_base):
            decrypted_message += numbers_to_letters[str(
                (int(number) - (rand_num*3)))]
        return decrypted_message
    except ValueError:
        return None


def encryptor_GUI():
    path = "file://" + \
        os.path.dirname(os.path.realpath(__file__)) + "/msg_gui.html"

    webbrowser.open(path)


def terminal_UI():
    print("\nWelcome to Msg Encryptor!!\n")

    while 1:
        msg = input("\nEnter your message/encrypted number: ").strip()

        options = input("""\n
Type 'help' for a guide.

Options:
    1. [Encrypt]
    2. [Decrypt]
Enter option number(1 or 2): """).strip()

        if options in ["1", "2"]:
            if options == "1":
                print("\n" + encrypt(msg) + "\n")
            else:
                dmsg = decrypt(msg)
                if dmsg:
                    print("\n" + dmsg + "\n")
                else:
                    print("\nThat is not an encrypted code.  Coudn't decrypt.\n")

        else:
            if options.lower() == 'help' or dt.is_typo('help', options.lower()):
                print("""

    How to use msg_encrypt module:
        Funtions:
            encrypt(): Encrypt a message or any text.
            decrypt(): Decrypt an encrypted message generated by the encrypt() function.
            
            encryptor_GUI(): Open a GUI version of the encrypter in your browser.
            
            terminal_UI(): An interactive user-friendly encryptor software which will take inputs and give outputs.
            
    encrypt() function usage:
        To use this function you can just pass the message as an argument into this function and this function will return some BIG encrypted numbers.
        >>> from msg_encrypt import encrypt
        >>> encrypt('Hello World!!')
        '850701407986.6.68961.1654815212048043.61537488=.392178327576.235827365-139560656067.304053045-1610519473736.183121221-906064629857.178144932-525434748532.254177507-479773768808.196016372-1527162316577.178983467-1083911118899.205570376-111703982019.93816192-350750148693.63877351-2096623517033.64594884-1787193777688.49040884-372532720512.51286408.=162887573014147873507224.746794706162789255475=.1175120018572-416857649936-4830459693894-2717125019991-1574779180569-1438145208192-4580413048978-3250499934456-334549048923-1051867181985-6289482981799-5361287087823-1117290443151850701407986.6.68961.1654815212048043.61537488472.958.4653801.37250583561079291.05214650.7.5'
        >>>

    decrypt function:
        A function to decrypt the encryption generated by the encrypt function.
        
        Usage:
        >>> # Let's assume we encrypted 'Hello World!!'
        >>> decrypt('850701407986.6.68961.1654815212048043.61537488=.392178327576.235827365-139560656067.304053045-1610519473736.183121221-906064629857.178144932-525434748532.254177507-479773768808.196016372-1527162316577.178983467-1083911118899.205570376-111703982019.93816192-350750148693.63877351-2096623517033.64594884-1787193777688.49040884-372532720512.51286408.=162887573014147873507224.746794706162789255475=.1175120018572-416857649936-4830459693894-2717125019991-1574779180569-1438145208192-4580413048978-3250499934456-334549048923-1051867181985-6289482981799-5361287087823-1117290443151850701407986.6.68961.1654815212048043.61537488472.958.4653801.37250583561079291.05214650.7.5')
        >>> 'Hello World!!'

    encryptor_GUI():
        A function that opens a GUI version of the encryptor in your browser, and it is user friendly.
        
        Usage:
        >>> encryptor_GUI()
        # Opens a GUI version in the browser.

    terminal_UI():
        User friendly encryptor in your terminal!
        
        Usage:
        >>> terminal_UI()
        Welcome to Msg Encryptor!!
        
        Enter your message/encrypted number: Python
        
        Type 'help' to know how to use this module.
        
        Options:
            1. [Encrypt]
            2. [Decrypt]
        Enter option number(1 or 2): 1 # will encrypt 'Python'
        
        <Output will be here>
        
        Enter your message/encrypted number: '13767410330823891319033269162332.1.62032.98967=.2124765987049.176398285.=21.079.73698594333.502639537082739886.84007672=.637323957143813767410330823891319033269162332.1.62032.989675.2810467030859.9027.9166365350636541.3.731088'
        
        Options:
            1. [Encrypt]
            2. [Decrypt]
        Enter option number: 2 # Decrypt the number given.
        
        <Output>
        
        ....
        ...
        ...
        >>>
        >>>
        

    To exit you can press Ctrl + C
    And for help you can simply type 'help'.
    """)
            elif (options.lower() in ['encrypt', 'decrypt', '[decrypt]', '[encrypt]']) or (dt.is_typo('encrypt', options.lower())) or (dt.is_typo('decrypt', options.lower())) or (dt.is_typo('[encrypt]', options.lower())) or (dt.is_typo('[decrypt]', options.lower())):
                if '[' in options:
                    options = options.replace('[', '')
                if ']' in options:
                    options = options.replace(']', '')
                correct = dt.is_typo('encrypt', options.lower()) or dt.is_typo(
                    'decrypt', options.lower())
                if correct:
                    options = correct[1]

                if options == 'encrypt':
                    encrypt(msg)
                else:
                    decrypt(msg)

            else:
                print(
                    '\nInvalid input! Please enter an option number from 1 to 2 or enter "help" for the "How to use" guide.\n')
