#!/usr/bin/env python3
# decoder.py

import sys


def main():
    my_string = str(input("Введите текст для расшифровки: "))
    text_len = len(my_string)
    #print("Длина зашифрованного текста:",text_len)
    key = str(input("Введите секретный ключ (не более 45 символов): "))
    key_len = len(key)
    #print("Длина ключа:",key_len)
    if key_len > 45:
        print("ОШИБКА: Ключ должен быть не более 45 символов!")
        return -1
    decoded_text = ""
    key_idx = 0
    for letter in my_string:
        letter_number = ord(letter) - 160
        key_number = ord(key[key_idx])
        decoded_number = letter_number ^ key_number
        decoded_letter = chr(decoded_number)
        decoded_text = decoded_text + decoded_letter
        #print("DEBUG: ",letter, key_idx, key[key_idx], letter_number, key_number, decoded_number, decoded_letter)
        key_idx += 1
        if key_idx > key_len - 1:
            key_idx = 0
    print("Расшифрованный текст: [", decoded_text,"]")
    decoded_len = len(decoded_text)
    #print("Дина расшифрованного текста:",decoded_len)
    if text_len == decoded_len:
        #print("Отлично!")
        pass
    else:
        print("ОШИБКА: Длины расшифрованного и зашифрованного текста должны совпадать!")
        return -2

if __name__ == "__main__":
    sys.exit(main())