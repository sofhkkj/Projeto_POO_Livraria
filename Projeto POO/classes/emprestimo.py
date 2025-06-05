from db.conexao import conectar
from datetime import date

class Emprestimo:  #Classes e Objetos — Definição da classe
    def __init__(self, data_emprestimo, data_prevista, cod_usuario, cod_funcionario, data_real=None):  
        # ✔️ 1. Atributos — características de um empréstimo
        self.data_emprestimo = data_emprestimo
        self.data_prevista = data_prevista
        self.data_real = data_real
        self.cod_usuario = cod_usuario
        self.cod_funcionario = cod_funcionario

    def salvar(self):  #Método — comportamento: salvar no banco
        conexao = conectar()
        if conexao is None:
            print("Não foi possível salvar o empréstimo.")
            return
        cursor = conexao.cursor()
        
        sql = """
            INSERT INTO tb_emprestimo (data_emprestimo, data_prevista, data_real, cod_usuario, cod_funcionario)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (self.data_emprestimo, self.data_prevista, self.data_real, self.cod_usuario, self.cod_funcionario)

        try:
            cursor.execute(sql, valores)
            conexao.commit()
            print("Empréstimo registrado com sucesso!")  #Polimorfismo possível em `salvar()` se usado em várias classes
        except Exception as e:
            print(f"Erro ao salvar empréstimo: {e}")
        finally:
            cursor.close()
            conexao.close()
