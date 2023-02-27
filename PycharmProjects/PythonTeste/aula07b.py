n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.2f}!', end=' ')
# :.3 casas decimais, flutuante.
# end='' coloca na mesma linha os dois prints.
# \n coloca na próxima linha tudo que estiver depois dele.
print(f'Divisão inteira {di} \n e potência {e}!')
