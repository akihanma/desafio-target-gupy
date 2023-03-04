string = "Exemplo de string"

# Converte a string para uma lista de caracteres
lista_caracteres = list(string)

# Inverte a lista de caracteres
for i in range(len(lista_caracteres) // 2):
    temp = lista_caracteres[i]
    lista_caracteres[i] = lista_caracteres[-i - 1]
    lista_caracteres[-i - 1] = temp

# Converte a lista de caracteres de volta para a string
string_invertida = "".join(lista_caracteres)

print(string_invertida)
