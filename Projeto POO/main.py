from classes.usuario import Usuario           # Uso de classes para representar entidades do sistema
from classes.funcionario import Funcionario   
from classes.livro import Livro               
from classes.emprestimo import Emprestimo    
from classes.doacao import Doacao             
from datetime import date

# Função que instancia objetos da classe Usuario e utiliza seu método salvar
def cadastrar_usuarios():
    while True:
        print("\nCadastro de Usuário")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")

        usuario = Usuario(nome=nome, cpf=cpf, email=email, telefone=telefone, endereco=endereco)  # Objeto sendo instanciado
        usuario.salvar()  # Método da classe sendo utilizado (comportamento)

        continuar = input("Deseja cadastrar outro usuário? (s/n): ").lower()
        if continuar != 's':
            break

#Cadastro de funcionários — outra classe instanciada com seus atributos
def cadastrar_funcionarios():
    while True:
        print("\nCadastro de Funcionário")
        nome = input("Nome do funcionário: ")
        cpf = input("CPF do funcionário: ")
        cargo = input("Cargo do funcionário: ")

        funcionario = Funcionario(nome, cpf, cargo)  #Objeto da classe Funcionario
        funcionario.salvar()

        continuar = input("Deseja cadastrar outro funcionário? (s/n): ").lower()
        if continuar != 's':
            break

# Cadastro de livros — instanciando a classe Livro e usando o método salvar
def cadastrar_livros():
    while True:
        print("\nCadastro de Livro")
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano_publicacao = input("Ano de publicação: ")
        editora = input("Editora: ")
        genero = input("Gênero: ")
        isbn = input("ISBN: ")

        livro = Livro(titulo=titulo, autor=autor, ano_publicacao=ano_publicacao,
                      editora=editora, genero=genero, isbn=isbn)
        livro.salvar()

        continuar = input("Deseja cadastrar outro livro? (s/n): ").lower()
        if continuar != 's':
            break

# Cadastro de empréstimos — classe com relacionamento entre Livro, Usuario e Funcionario
def cadastrar_emprestimo():
    while True:
        try:
            print("\nCadastro de Empréstimo")
            cod_livro = int(input("Código do livro: "))
            cod_usuario = int(input("Código do usuário: "))
            cod_funcionario = int(input("Código do funcionário: "))
            data_emprestimo = date.today()  # Definindo atributo de data com a data atual

            # Objeto da classe Emprestimo sendo criado com seus atributos
            emprestimo = Emprestimo(cod_livro, cod_usuario, cod_funcionario, data_emprestimo)
            emprestimo.salvar()
        except Exception as e:
            print("Erro ao salvar empréstimo:", e)

        continuar = input("Deseja cadastrar outro empréstimo? (s/n): ").lower()
        if continuar != 's':
            break

#  Cadastro de doações — classe com atributos e condição para anonimato
def cadastrar_doacao():
    while True:
        try:
            print("\nCadastro de Doação")
            cod_livro = int(input("Código do livro doado: "))
            anonimo = input("Deseja doar anonimamente? (s/n): ").lower()

            cod_usuario = None
            if anonimo != 's':
                cod_usuario = int(input("Código do usuário doador: "))

            data_doacao = date.today()

            # Objeto da classe Doacao sendo instanciado
            doacao = Doacao(cod_livro, data_doacao, cod_usuario)
            doacao.salvar()
        except Exception as e:
            print("Erro ao salvar doação:", e)

        continuar = input("Deseja cadastrar outra doação? (s/n): ").lower()
        if continuar != 's':
            break

# Menu principal para navegar entre funcionalidades — interface simples
def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar Usuário")
        print("2. Cadastrar Funcionário")
        print("3. Cadastrar Livro")
        print("4. Cadastrar Empréstimo")
        print("5. Cadastrar Doação")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuarios()
        elif opcao == '2':
            cadastrar_funcionarios()
        elif opcao == '3':
            cadastrar_livros()
        elif opcao == '4':
            cadastrar_emprestimo()
        elif opcao == '5':
            cadastrar_doacao()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
