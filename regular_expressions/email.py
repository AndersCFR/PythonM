import re
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
passpat = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
string = 'anderson@f.c'
passw= 'ddfdafda564'
a = pattern.match(string)
print(a)
b= passpat.fullmatch(passw)
print(b)


