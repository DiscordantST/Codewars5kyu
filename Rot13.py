alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_uper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13(message):
    simple_string_decod_rot13 = ""
    d = 0
    for i in message:
        if i in alphabet:
            d += alphabet.index(i) - 13
            simple_string_decod_rot13 += alphabet[d]
            d = 0
        elif i in alphabet_uper:
            d += alphabet_uper.index(i) - 13
            simple_string_decod_rot13 += alphabet_uper[d]
            d = 0
        else:
            simple_string_decod_rot13 += i
    return simple_string_decod_rot13
