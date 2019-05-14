def verificar_alpha(string):
    new_string = "".join(filter(str.isalpha, string.lower()))
    return new_string


def palindromo(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return palindromo(string[1:-1])
        else:
            return False


string1 = 'kayak'
string2 = 'aibohphobia'
string3 = verificar_alpha('Live not on evil')
string4 = verificar_alpha('Reviled did I live, said I, as evil I did deliver')
string5 = verificar_alpha('Go hang a salami; I’m a lasagna hog.')
string6 = verificar_alpha('Able was I ere I saw Elba')
string7 = verificar_alpha('Kanakanak – uma cidade no Alaska')
string8 = verificar_alpha('Wassamassaw – uma cidade em South Dakota')

print(string1 + ":", palindromo(string1))
print(string2 + ":", palindromo(string2))
print(string3 + ":", palindromo(string3))
print(string4 + ":", palindromo(string4))
print(string5 + ":", palindromo(string5))
print(string6 + ":", palindromo(string6))
print(string7 + ":", palindromo(string7))
print(string8 + ":", palindromo(string8))










