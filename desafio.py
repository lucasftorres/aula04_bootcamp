### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

#1 Solicita ao usuario que digite seu nome
# Usuario pode inserir o nomer não válido utilizando numeros ou simbolos ou vazio


def gerador_de_kpi():

    nome_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False

    while not nome_valido:
        try:
            nome: str = input("Digite seu nome aqui: ") 

            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio!")
            elif not all(char.isalpha() for char in nome):
                raise ValueError('Você digitou um valor inválido, por favor informe um nome alfabetico!')
            else:
                print(f'Nome valido: {nome}')
                nome_valido = True

        except ValueError as e:
            print(e)

    while not salario_valido:
        try:
            salario = float(input("Digite o valor do seu salario: "))

            if salario <= 0:
                raise ValueError('Voce digitou um valor menor ou igual a zero para salario!')
            else:
                salario_valido = True
        except ValueError as e:
            print(e)

    while not bonus_valido:
        try:

            bonus = float(input("Digite o valor do seu bônus: "))
            if bonus <= 0:
                raise ValueError('Voce digitou um valor menor ou igual a zero para bonus!')
            else:
                bonus_valido = True
        except ValueError as e:
            print(e)

    return nome, salario, bonus

#5 Imprima o calculo de KPI do usuario
# O Resultado dos itens anteriores podem zerar a remuneração ou gerar um soma de tipos de dados errados.

nome_usuario, salario_usuario, bonus_usuario = gerador_de_kpi()
bonus_final: float = (1000 + salario_usuario) * bonus_usuario

print(f"O calculo de KPI eh: (1000 + {salario_usuario}) * {bonus_usuario} = {bonus_final}")

#6 Imprima o nome do usuario e o valor do bonus final
# O resultado dos itens anteriores gerar um impressão incorreta
print(f"Nome: {nome_usuario}, Bônus Final: {bonus_final:.2f}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?