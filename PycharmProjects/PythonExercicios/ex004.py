print('====== DESAFIO 04 ======')

a = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(a))

print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minuscúlas?', a.islower())
print('Está capitalizada?', a.istitle())

# Capitalizada: É quando a palavra começa com uma letra maiúscula e o resto é minúscula.