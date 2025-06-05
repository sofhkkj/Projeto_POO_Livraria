from db.conexao import conectar

class Usuario:  # Classes e Objetos — Definição de classe
    def __init__(self, nome, cpf, email, telefone, endereco):  #Atributos definidos no construtor
        self.nome = nome
        self.cpf = cpf  #Encapsulamento sugerido (privado lógico)
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def salvar(self):  #Método — comportamento da classe
        conexao = conectar()
        cursor = conexao.cursor()

        try:
            #Método que insere os dados no banco de dados (ação da classe)
            sql = "INSERT INTO tb_usuario (nome, cpf, email, telefone, endereco) VALUES (%s, %s, %s, %s, %s)"
            valores = (self.nome, self.cpf, self.email, self.telefone, self.endereco)
            cursor.execute(sql, valores)
            conexao.commit()
            print("Usuário salvo com sucesso!")  #Método com saída de controle
        except Exception as e:
            print("Erro ao salvar usuário:", e)
        finally:
            cursor.close()
            conexao.close()
