#Manuela Clara Jurgens Baptista - RM 563730 (representante)
#Raissa Neves Costa - RM 566323

quantidade_desastres = int(input("Qual a quantidade de desastres registrados?"))
tipos_desastres = str(input("Qual o tipo de desastre?"))
pais = str(input("Em qual país isso ocorreu?"))
cidade = str(input("Em qual cidade?"))
bairro = str(input("Em qual bairro?"))
rua = str(input("Qual o nome da rua?"))

quantidade_afetados = int(input("Qual a quantidade total de pessoas afetadas?"))
quantidade_criancas = int(input("Qual a quantidade de crianças afetadas?"))
quantidade_adultos = int(input("Qual a quantidade de adultos afetados?"))
quantidade_idosos = int(input("Qual a quantidade de idosos afetados?"))
quantidade_mob_reduzida = int(input("Quantas pessoas com mobilidade reduzida foram afetadas?"))
quantidade_feridos = int(input("Quantas pessoas foram feridas?"))

while True:
    if quantidade_criancas + quantidade_adultos + quantidade_idosos + quantidade_mob_reduzida + quantidade_feridos == quantidade_afetados:
        print("Informações armazenadas")
        break
    else:
        print("Dados inválidos. Alguma informação foi inserida com a quantidade errada. Insira novamente todas as quantidades.")
        break





