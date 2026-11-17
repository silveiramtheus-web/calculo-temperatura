
temperaturas = []

# Receber e validar as temperaturas
for i in range(7):
    temperatura = float(input("Digite a temperatura do dia: "))

    while temperatura < -10 or temperatura > 50:
        print("Temperatura inválida.")
        temperatura = float(input("Digite novamente: "))

    temperaturas.append(temperatura)


# Encontrar a maior temperatura
maior = temperaturas[0]
dia_maior = 0

for i in range(7):
    if temperaturas[i] > maior:
        maior = temperaturas[i]
        dia_maior = i

print("Maior temperatura:", maior)
print("Dia da maior temperatura:", dia_maior + 1)


# Encontrar a menor temperatura
menor = temperaturas[0]

for i in range(7):
    if temperaturas[i] < menor:
        menor = temperaturas[i]

print("Menor temperatura:", menor)


# Contar dias acima de 32 graus
contador = 0

for i in range(7):
    if temperaturas[i] > 32:
        contador = contador + 1

print("Dias acima de 32 graus:", contador)


# Reduzir temperaturas acima de 30 graus
for i in range(7):
    if temperaturas[i] > 30:
        temperaturas[i] = temperaturas[i] - 4.5

        if temperaturas[i] < 15:
            temperaturas[i] = 15


# Mostrar temperaturas atualizadas
print("Temperaturas atualizadas:", temperaturas)


# Calcular a nova média
soma = 0

for i in range(7):
    soma = soma + temperaturas[i]

nova_media = soma / 7

print("Nova média:", nova_media)
