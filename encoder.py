#!/usr/bin/env python3
# encoder.py

import sys


def main():
    my_string = str(input("Введите текст для шифрования: "))
    text_len = len(my_string)
    #print("Длина текста:",text_len)
    key = str(input("Введите ключ (до 45 символов): "))
    key_len = len(key)
    #print("Длина ключа:",key_len)
    if key_len > 45:
        print("ОШИБКА: Ключ должен быть не больше 45 символов!")
        return -1
    encoded_text = ""
    key_idx = 0
    for letter in my_string:
        letter_number = ord(letter)
        key_number = ord(key[key_idx])
        encoded_number = letter_number ^ key_number
        encoded_letter = chr(160 + encoded_number)
        encoded_text = encoded_text + encoded_letter
        # print("DEBUG: ",letter, key_idx, key[key_idx], letter_number, key_number, encoded_number, encoded_letter)
        key_idx += 1
        if key_idx > key_len - 1:
            key_idx = 0
    print("Зашифрованный текст: [", encoded_text,"]")
    encoded_len = len(encoded_text)
    #print("Длина зашифрованного текста:",encoded_len)
    if text_len == encoded_len:
        #print("Отлично!")
        pass
    else:
        print("ОШИБКА: Зашифрованный текст должен быть той же длинны что и оригинальный!")
        return -2

if __name__ == "__main__":
    sys.exit(main())