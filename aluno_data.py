from aluno_modulo import Aluno
import pymysql.cursors

class AlunoData:
    def __init__(self):
        self.conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='escola',
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conexao.cursor()

    def insert(self, aluno:Aluno):
        try:
            sql = "INSERT INTO aluno "\
                   "VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (aluno.matricula,
                                      aluno.nome,
                                      aluno.idade,
                                      aluno.curso,
                                      aluno.nota))
            self.conexao.commit()

        except Exception as error:
            print(f"Error ao inserir: erro : {error}")

    def update(self, aluno:Aluno):
        try:
            sql = "UPDATE aluno SET nome = %s, idade = %s, curso = %s, nota = %s WHERE matricula = %s"
            self.cursor.execute(sql, (aluno.nome,
                                      aluno.idade,
                                      aluno.curso,
                                      aluno.nota,
                                      aluno.matricula))
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao atualizar! Error: {error} ')

    def select(self):
        try:
            sql = "SELECT * FROM aluno"
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall()
            return alunos
        except Exception as error:
            print(f"Erro ao lista! {error}")

    def delete(self, matricula: str):
        try:
            sql = "DELETE FROM aluno WHERE matricula = %s"
            self.cursor.execute(sql, matricula)
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao deletar! {error}")


if __name__ == '__main__':
    a = AlunoData()
    a.delete('98d259b6-02ac-4bbc-89e3-ca1b4ce8e8cf')
    print(a.select())