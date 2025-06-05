from db.conexao import conectar

class Doacao:  # Classe — representa a entidade "Doação"
    def __init__(self, livro, data_doacao, cod_usuario):
        # Atributos — definem características de cada doação
        self.livro = livro                # código ou nome do livro doado
        self.data_doacao = data_doacao    # data do registro da doação
        self.cod_usuario = cod_usuario    # pode ser um usuário identificado ou anônimo

    def salvar(self):  # Método — comportamento que salva a doação no banco
        conexao = conectar()
        cursor = conexao.cursor()

        # Lógica de persistência — insere os dados na tabela de doações
        sql = "INSERT INTO tb_doacao (cod_livro, data_doacao, cod_usuario) VALUES (%s, %s, %s)"
        valores = (self.livro, self.data_doacao, self.cod_usuario)

        try:
            cursor.execute(sql, valores)
            conexao.commit()
            print("Doação salva com sucesso!")  #Confirmação do comportamento executado
        except Exception as e:
            print(f"Erro ao salvar doação: {e}")
        finally:
            cursor.close()
            conexao.close()

def main():
    print("Cadastro de Doação")
    livro = input("Nome do livro: ")
    data_doacao = input("Data da doação (AAAA-MM-DD): ")

    # Planejamento: cod_usuario pode ser 0 (anônimo) ou um ID real
    cod_usuario_anonimo = 0

    # Objeto sendo instanciado com os dados informados
    doacao = Doacao(livro, data_doacao, cod_usuario_anonimo)
    doacao.salvar()  # Método sendo chamado

if __name__ == "__main__":
    main()

