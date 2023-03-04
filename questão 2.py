num = int(input("Digite um número: "))

# Define os valores iniciais da sequência
a, b = 0, 1
while b < num:
    # Calcula o próximo valor da sequência
    a, b = b, a+b
    
# Verifica se o número informado pertence à sequência
if b == num:
    print(num, "pertence à sequência de Fibonacci")
else:
    print(num, "não pertence à sequência de Fibonacci")
