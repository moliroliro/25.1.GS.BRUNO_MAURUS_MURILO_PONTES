##Bruno Pereira Maurus RM562503
##Murilo Alencar Pontes RM561290

tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_afetados = []
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

num_desastres = int(input("Insira a quantidade de desastres: "))

for i in range(num_desastres):
    print(f" Desastre {i + 1} ")

    tipos_desastres.append(input("Tipo do desastre: "))
    paises.append(input("País: "))
    cidades.append(input("Cidade: "))
    bairros.append(input("Bairro: "))
    ruas.append(input("Rua: "))

    while True:
        total = int(input("Total de pessoas que foram afetadas: "))

        crianca = int(input("Número de crianças: "))
        adulto = int(input("Número de adultos: "))
        idoso = int(input("Número de idosos: "))
        mobilidade = int(input("Número de pessoas com mobilidade reduzida: "))
        ferido = int(input("Número de feridos: "))

        if crianca + adulto + idoso + mobilidade + ferido == total:
            criancas.append(crianca)
            adultos.append(adulto)
            idosos.append(idoso)
            mobilidade_reduzida.append(mobilidade)
            feridos.append(ferido)
            total_afetados.append(total)
            break
        else:
            print("A quantidade não corresponde ao total, faça novamente")

total_desastre = len(tipos_desastres)
total_afetados_geral = sum(total_afetados)
soma_crianca = sum(criancas)
soma_adulto = sum(adultos)
soma_idoso = sum(idosos)
soma_mobilidade = sum(mobilidade_reduzida)
soma_ferido = sum(feridos)

tipos = [soma_crianca, soma_adulto, soma_idoso, soma_mobilidade, soma_ferido]
nomes_categorias = ["Crianças", "Adultos", "Idosos", "Mobilidade reduzida", "Feridos"]

indice_mais_afetado = tipos.index(max(tipos))
categoria_mais_afetada = nomes_categorias[indice_mais_afetado]

mais_grave = total_afetados.index(max(total_afetados))
local_mais_afetado = f"{ruas[mais_grave]}, {bairros[mais_grave]}, {cidades[mais_grave]}, {paises[mais_grave]}"
tipo_mais_grave = tipos_desastres[mais_grave]

print(" Relatório")
print(f"Numero total de desastres registrados: {total_desastre}")
print("Resumo de pessoas que foram afetadas por categoria:")
print(f"Crianças: {soma_crianca} | Adultos: {soma_adulto} | Idosos: {soma_idoso} | Mobilidade reduzida: {soma_mobilidade} | Feridos: {soma_ferido}")
print(f"Categoria mais afetada: {categoria_mais_afetada}")
print(f"Total de pessoas que foram afetadas: {total_afetados_geral}")
print("Desastre com maior número de pessoas afetadas:")
print(f"Tipo: {tipo_mais_grave}")
print(f"Local: {local_mais_afetado}")