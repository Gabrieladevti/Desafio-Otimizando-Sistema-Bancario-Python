import textwrap 

def menu():
    menu = """\n
        Bem vindo!               MyBank
    ==================================================

    Realize uma operação!

    [6]\tNovo usuário
    [5]\tNova conta
    [4]\tListar contas
    [3]\tDepositar
    [2]\tSacar
    [1]\tExtrato
    [0]\tSair

    ==================================================
    Informe o número da operação => """
    return input(textwrap.dedent(menu))


def deposit(balance, value, statement, /):
    if value <= 0:
        print("A operação não pôde ser concluída! O valor informado é inválido.")
        return balance, statement

    balance += value
    statement += f"Depósito:\tR$ {value:.2f}\n"
    print("Operação de depósito bem-sucedida!")
    
    return balance, statement


def withdraw_from_account(*, balance, value, statement, limit, number_of_withdrawals, WITHDRAWAL_LIMIT):
    if value <= 0:
        print("A operação não pôde ser concluída! O valor informado é inválido.")
        return balance, statement, number_of_withdrawals

    elif value > balance:
        print("A operação não pôde ser concluída! Você não tem saldo suficiente.")
        return balance, statement, number_of_withdrawals

    elif value > limit:
        print("A operação não pôde ser concluída! O valor do saque excede o limite.")
        return balance, statement, number_of_withdrawals

    elif number_of_withdrawals >= WITHDRAWAL_LIMIT:
        print("A operação não pôde ser concluída! Número máximo de saques excedido.")
        return balance, statement, number_of_withdrawals

    balance -= value
    statement += f"Saque:\t\tR$ {value:.2f}\n"
    number_of_withdrawals += 1
    print("Operação de saque concluída com sucesso!")
    
    return balance, statement, number_of_withdrawals


def display_statement(balance, /, *, statement):
    print(" EXTRATO ".center(50,"="))
    print("Não foram realizadas movimentações." if not statement else statement)
    print(f"\nSaldo: R$ {balance:.2f}\n"+("="*50))


def create_user(users): 
    cpf = input("Digite o seu CPF (apenas números): ")
    user = filter_user(cpf, users)

    if user:
        print("\nO CPF informado já possui cadastro!")
        return

    name = input("Digite o seu nome completo: ")
    date_birth = input("Digite a sua data de nascimento (dd-mm-aaaa): ")
    address = input("Digite o seu endereço (logradouro, número - bairro - cidade/sigla estado): ")

    users.append({
        "nome": name, 
        "data_nascimento": date_birth,
        "cpf": cpf, 
        "endereco": address
        })

    print("Usuário criado! Seja bem Vindo ao MyBank")
 

def filter_user(cpf, users):
    users_filters = [user for user in users if user["cpf"] == cpf]
    return users_filters[0] if users_filters else None


def create_account(bank_branch, account_number, users):
    cpf = input("Digite o CPF cadastrado: ")
    user = filter_user(cpf, users)

    if user:
        print("\nConta MyBank criada com sucesso!")
        return {"bank_branch": bank_branch, "account_number": account_number, "user": user}
    
    print("\nUsuário não encontrado, Cadastre um usuário!")


def list_accounts(bank_accounts):
    for account in bank_accounts:
        print("=" * 100)
        print(f"Agência:\t{account['bank_branch']}")
        print(f"C\C:\t\t{account['account_number']}")
        print(f"Titular:\t{account['user']['nome']}")

    
def main(): 
    WITHDRAWAL_LIMIT = 3
    BANK_BRANCH = "0001"

    balance = 0
    limit = 500
    statement = ""
    number_of_withdrawals = 0
    users = [] 
    banck_accounts = []

    while True:
        option = menu()

        if option == "3":
            value = float(input("Adicione o valor do depósito: "))

            balance, statement = deposit(balance, value, statement) 

        elif option == "2":
            value = float(input("Adicione o valor do saque: "))

            balance, statement, number_of_withdrawals = withdraw_from_account(
                balance=balance,
                value=value,
                statement=statement,
                limit=limit,
                number_of_withdrawals=number_of_withdrawals,
                WITHDRAWAL_LIMIT=WITHDRAWAL_LIMIT,
            )

        elif option == "1":
            display_statement(balance, statement=statement)

        elif option == "6": 
            create_user(users)

        elif option == "5":
            account_number = len(banck_accounts) + 1 
            account = create_account(BANK_BRANCH, account_number, users)

            if account:
                banck_accounts.append(account)

        elif option == "4":
            list_accounts(banck_accounts)

        elif option == "0":
            print("Seção finalizada!\nObrigado por utilizar o MyBank ^-^")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()