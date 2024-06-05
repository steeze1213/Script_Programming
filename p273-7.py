import string

def caesar_cipher(text, shift):
    src_str = string.ascii_uppercase + string.ascii_lowercase
    dst_str = src_str[shift:] + src_str[:shift]

    encrypted_text = ''

    for char in text:
        if char not in src_str:
            encrypted_text += char
        else:
            index = src_str.find(char)
            encrypted_text += dst_str[index]

    return encrypted_text

text = input("문장을 입력하시오: ")
shift = int(input("이동시킬 칸 수를 입력하시오: "))

encrypted_text = caesar_cipher(text, shift)

print("암호화된 문자:", encrypted_text)
