from db.conexao import conectar

class Funcionario:  # Classes e Objetos — definição de uma entidade do sistema
    def __init__(self, nome, matricula, cargo):
        # Atributos — representam as características do objeto
        self.nome = nome
        self.matricula = matricula
        self.cargo = cargo

    def salvar(self):  # Método — comportamento responsável por persistência no banco
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO tb_funcionario (nome, matricula, cargo)
            VALUES (%s, %s, %s)
        """
        valores = (self.nome, self.matricula, self.cargo)

        # Lógica de persistência — ação do objeto
        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f"Funcionário {self.nome} salvo com sucesso!")  #Feedback de ação executada
