# importar biblioteca para validação de email
import re

from datetime import datetime

# lista para armazenar dicionario (cadastro de pessoas)
usuarios = []
log_exclusao = []


def calcular_idade(data_nascimento):
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year

    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    return idade


def validar_nome(nome):
    if not nome or len(nome.strip()) < 2:
        return False

    for c in nome:
        if not (c.isalpha() or c.isspace()):
            return False

    return True


def validar_cidade(cidade):
    if not cidade or len(cidade.strip()) < 2:
        return False

    for c in cidade:
        if not (c.isalpha() or c.isspace()):
            return False

    return True

# função para validar email


def validar_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.fullmatch(pattern, email) is not None

# função de cadastro de usuario, verificação de duplicação de e-mail


def cadastro_usuario():
    while True:
        nome = input("Digite o nome: ").strip()
        if validar_nome(nome):
            break
        else:
            print("\nNome inválido! Use apenas letras (mínimo 2 caracteres).\n")

    while True:
        try:
            data_nasc_str = input(
                "Digite a data de nascimento (DD/MM/AAAA): ").strip()
            data_nascimento = datetime.strptime(data_nasc_str, "%d/%m/%Y")

            if data_nascimento > datetime.now():
                print("\nData de nascimento não pode ser no futuro!\n")
                continue
            idade = calcular_idade(data_nascimento)

            if idade < 0:
                print("\nData inválida!\n")
                continue
            break
        except ValueError:
            print("\nFormato de data inválido! use DD/MM/AAAA\n")

    while True:
        cidade = input("Digite a cidade: ").strip()
        if validar_cidade(cidade):
            break
        else:
            print("\nCidade inválida! Use apenas letras (mínimo 2 caracteres).\n")

    while True:
        email = input("Digite o E-mail: ").strip()
        email_correcao = email.lower()
        email_duplicado = False

        if not validar_email(email):
            print("\nE-mail em formato inválido!\n")
            continue

        for user in usuarios:
            if user["email"] == email_correcao:
                print("\nE-mail já cadastrado!\n")
                email_duplicado = True
                break
        if not email_duplicado:
            break

    if usuarios:
        novo_id = usuarios[-1]["id"] + 1
    else:
        novo_id = 1

    usuario = {"id": novo_id,
               "nome": nome,
               "data_nascimento": data_nasc_str,
               "idade": idade,
               "cidade": cidade,
               "email": email
               }

    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!\n")


# função para mostrar lista de usuários
def listar_usuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado!\n")
    else:
        usuarios_ordenados = sorted(
            usuarios, key=lambda usuario: usuario['nome'].lower())

        for usuario in usuarios_ordenados:
            print(f"ID: {usuario['id']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Cidade: {usuario['cidade']}")
            print(f"E-mail: {usuario['email']}")
            print("-"*20)


def listar_usuarios_excluidos():
    if not log_exclusao:
        print("\nNenhum usuário excluido!\n")
    else:
        for exclusao in log_exclusao:
            usuario = exclusao['usuario']
            data = exclusao['data']

            print(f"ID: {usuario['id']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Cidade: {usuario['cidade']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Data da exclusão: {data.strftime('%d/%m/%Y %H:%M:%S')}")
            print("-"*40)


def estatisticas_idades():
    if not usuarios:
        print("\nNenhum usuário cadastrado!\n")
        return

    idades = [usuario['idade'] for usuario in usuarios]

    idade_minima = min(idades)
    idade_maxima = max(idades)
    idade_media = sum(idades) / len(idades)

    idades_ordenadas = sorted(idades)
    total_de_usuarios = len(idades_ordenadas)

    if total_de_usuarios % 2 == 0:
        mediana = (idades_ordenadas[total_de_usuarios//2 - 1] +
                   idades_ordenadas[total_de_usuarios//2]) / 2
    else:
        mediana = idades_ordenadas[total_de_usuarios//2]

    variancia = sum((idade - idade_media) **
                    2 for idade in idades) / len(idades)

    desvio_padrao = variancia ** 0.5

    print("\n" + "="*29)
    print(" --- ESTATÍSTICAS DAS IDADES ---")
    print("="*29)
    print(f"Total de pessoas: {len(usuarios)}")
    print(f"Menor idade: {idade_minima} anos")
    print(f"Maior idade: {idade_maxima} anos")
    print(f"Média das idades: {idade_media:.2f} anos")
    print(f"Mediana das idades: {mediana:.2f} anos")
    print(f"Desvio-padrão: {desvio_padrao:.2f}")
    print("="*29 + "\n")

# Buscar usuario por ID, criado para a função de exclusão


def buscar_usuario_por_id():
    try:
        id_buscado = int(input("Digite o ID que procura: "))
    except ValueError:
        print("\nID inválido! use apenas números.\n")
        return

    encontrado = False

    if not usuarios:
        print("\nNenhum usuário cadastrado!\n")
    else:
        for usuario in usuarios:
            if usuario['id'] == id_buscado:
                print("\nUsuário encontrado!\n")
                print(f"ID: {usuario['id']}")
                print(f"Nome: {usuario['nome']}")
                print(f"Idade: {usuario['idade']}")
                print(f"Cidade: {usuario['cidade']}")
                print(f"E-mail: {usuario['email']}")
                encontrado = True
        if not encontrado:
            print("\nID não encontrado!\n")

# função para buscar usuário por nome


def buscar_usuario_por_nome():
    nome_buscado = input("Digite o nome que procura: ").strip().lower()
    encontrado = False

    if not usuarios:
        print("\nNenhum usuário cadastrado!\n")

    else:
        for usuario in usuarios:
            if usuario['nome'].lower() == nome_buscado:
                print("\nUsuário encontrado!\n")
                print(f"ID: {usuario['id']}")
                print(f"Nome: {usuario['nome']}")
                print(f"Idade: {usuario['idade']}")
                print(f"Cidade: {usuario['cidade']}")
                print(f"E-mail: {usuario['email']}")
                encontrado = True
        if not encontrado:
            print("\nNome não encontrado!\n")

# função para buscar usuário por e-mail


def buscar_usuario_por_email():
    email_buscado = input("Digite o E-mail que procura: ").strip()
    encontrado = False

    if not usuarios:
        print("\nNenhum usuário cadastrado!\n")

    else:
        for usuario in usuarios:
            if usuario['email'] == email_buscado:
                print("\nUsuário encontrado!\n")
                print(f"ID: {usuario['id']}")
                print(f"Nome: {usuario['nome']}")
                print(f"Idade: {usuario['idade']}")
                print(f"Cidade: {usuario['cidade']}")
                print(f"E-mail: {usuario['email']}")
                encontrado = True
        if not encontrado:
            print("\nE-mail não encontrado!\n")


def excluir_usuario_por_id():
    try:
        excluir_usuario_id = int(
            input("\nDigite o Id do usuário a ser excluido: "))
    except ValueError:
        print("\nID inválido! use apenas números.")
        return

    encontrado = False

    for usuario in usuarios:
        if usuario['id'] == excluir_usuario_id:
            print("\nUsuário encontrado!\n")
            print(f"ID: {usuario['id']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Cidade: {usuario['cidade']}")
            print(f"E-mail: {usuario['email']}")

            encontrado = True

            confirmar_exclusao = input("Confirma?[S/N]: ").strip().lower()

            if confirmar_exclusao == "s":
                usuarios.remove(usuario)
                log_exclusao.append(
                    {'usuario': usuario, 'data': datetime.now()})
                print("\nExclusão concluida.\n")

            elif confirmar_exclusao == "n":
                print("\nExclusão cancelada.\n")

            else:
                print("\nOpção inválida!\n")

            return

    if not encontrado:
        print("\nID não encontrado!\n")


def excluir_usuario():
    print("="*29)
    print("| 1 - ID     |")
    print("| 2 - Nome   |")
    print("| 3 - E-mail |")
    print("="*29)
    menu_exclusao = input("escolha a opção de exclusão: ")

    if menu_exclusao == "1":
        buscar_usuario_por_id()
        excluir_usuario_por_id()

    elif menu_exclusao == "2":
        buscar_usuario_por_nome()
        excluir_usuario_por_id()

    elif menu_exclusao == "3":
        buscar_usuario_por_email()
        excluir_usuario_por_id()
    else:
        print("Opção Inválida!")
        return


while True:
    print("="*29)
    print("|---------- MENU -----------|")
    print("="*29)
    print("| 1 - Cadastrar             |")
    print("| 2 - Listar                |")
    print("| 3 - Estatísticas de idade |")
    print("| 4 - Buscar por nome       |")
    print("| 5 - Buscar por E-mail     |")
    print("| 6 - Excluir usuário       |")
    print("| 7 - Usuários excluídos    |")
    print("| 0 - Sair                  |")
    print("="*29)

    opcao = input("Escolha: ")

    if opcao == "0":
        break

    elif opcao == "1":
        cadastro_usuario()

    elif opcao == "2":
        listar_usuarios()

    elif opcao == "3":
        estatisticas_idades()

    elif opcao == "4":
        buscar_usuario_por_nome()

    elif opcao == "5":
        buscar_usuario_por_email()

    elif opcao == "6":
        excluir_usuario()

    elif opcao == "7":
        listar_usuarios_excluidos()

    else:
        print("\nOpção inválida!\n")
