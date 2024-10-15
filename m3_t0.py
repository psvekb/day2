# import string as st

# Используйте модуль string и слайсы, чтобы выполнить 2 задания:
import string as st

# 1. Вывести 16-ричный алфавит с помощью двух разных вариантов
# Out: '0123456789ABCDEF'
# # Variant 1

# print(st.ascii_uppercase.index('G'))
print(st.digits + st.ascii_uppercase[:6])
#
# # Variant 2
# print(st.hexdigits.strip('abcdef'))
print(st.hexdigits.replace('abcdef',''))


# 2. Вывести знаки пунктуации от знака '=' и до конца строки
s = st.punctuation
# print(st.punctuation)
print(s[s.index('='):])