import csv

with open("cadastro_funcionarios.csv", encoding="utf-8") as arquivo:
    funcionarios = list(csv.DictReader(arquivo))

while True:
    print("\n" + "="*50)
    print("ANALISADOR DE SALARIOS")
    print("="*50)
    print("1. Media salarial de um setor")
    print("2. Media salarial de todos os setores")
    print("3. Maior e menor salario de um setor")
    print("4. Sair")
    print("="*50)
    
    opcao = input("Escolha uma opcao: ")
    
    if opcao == "1":
        setores = sorted(set(f["setor"] for f in funcionarios))
        print("\nSetores disponiveis:", ", ".join(setores))
        
        setor = input("Digite o setor: ")
        funcionarios_setor = [f for f in funcionarios if f["setor"] == setor]
        
        if funcionarios_setor:
            salarios = [float(f["salario"]) for f in funcionarios_setor]
            media = sum(salarios) / len(salarios)
            print(f"\nMedia salarial do {setor}: R$ {media:,.2f}")
            print(f"Total: {len(funcionarios_setor)} funcionarios")
        else:
            print("Setor nao encontrado!")
    
    elif opcao == "2":
        print("\nMEDIA POR SETOR:")
        setores = {}
        for f in funcionarios:
            if f["setor"] not in setores:
                setores[f["setor"]] = []
            setores[f["setor"]].append(float(f["salario"]))
        
        for setor, salarios in sorted(setores.items()):
            media = sum(salarios) / len(salarios)
            print(f"  {setor:15} | Media: R$ {media:,.2f} | ({len(salarios)} func.)")
    
    elif opcao == "3":
        setores = sorted(set(f["setor"] for f in funcionarios))
        print("\nSetores disponiveis:", ", ".join(setores))
        
        setor = input("Digite o setor: ")
        funcionarios_setor = [f for f in funcionarios if f["setor"] == setor]
        
        if funcionarios_setor:
            salarios = [float(f["salario"]) for f in funcionarios_setor]
            print(f"\nSETOR: {setor}")
            print(f"  Menor salario: R$ {min(salarios):,.2f}")
            print(f"  Maior salario: R$ {max(salarios):,.2f}")
            print(f"  Media: R$ {sum(salarios)/len(salarios):,.2f}")
        else:
            print("Setor nao encontrado!")
    
    elif opcao == "4":
        print("Ate logo!")
        break
    
    else:
        print("Opcao invalida!")