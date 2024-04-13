from sqlite3 import *
import os

DATABASE_NAME = "banco.db"

class DataMethods():
    #Metodo para criar conexão
    @classmethod
    def create_connection(cls):
        connection = connect(f'{DATABASE_NAME}')
        return connection
        
    #Metodo para executar querys
    @classmethod
    def execute_query(cls, query):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        
    #Metodo para identificar se o banco ja existe ou nao
    @classmethod
    def initialize(cls):
        print("Inicializando banco")
        if os.path.exists(f'./{DATABASE_NAME}'):
            print('Banco existe')
        else:
            print('Banco não existe')
            print('Criando banco de dados')
            cls.execute_query(f'CREATE TABLE IF NOT EXISTS usuarios('
                              f'id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,'
                              f'nome TEXT NOT NULL,'
                              f'email TEXT UNIQUE NOT NULL,'
                              f'senha TEXT NOT NULL,'
                              f'data_nascimento TEXT NOT NULL,'
                              f'sexo TEXT NOT NULL,'
                              f'telefone INTEGER NOT NULL,'
                              f'tipo_sanguineo TEXT NOT NULL,'
                              f'altura REAL NOT NULL,'
                              f'peso REAL    NOT NULL)')

            cls.execute_query(f'CREATE TABLE IF NOT EXISTS remedio('
                              f'id_remedio INTEGER PRIMARY KEY AUTOINCREMENT,'
                              f'id_usuario INTEGER NOT NULL references usuarios(id_usuario),'
                              f'nome_remedio TEXT NOT NULL,'
                              f'desc_remedio TEXT,'
                              f'intervalo_uso TEXT,'
                              f'primeiro_uso TEXT NOT NULL)')

            cls.execute_query(f'CREATE TABLE IF NOT EXISTS consulta('
                              f'id_consulta INTEGER PRIMARY KEY AUTOINCREMENT,'
                              f'id_usuario INTEGER NOT NULL references usuarios(id_usuario),'
                              f'nome_consulta TEXT NOT NULL,'
                              f'desc_consulta TEXT,'
                              f'hora_consulta TEXT NOT NULL,'
                              f'data_consulta TEXT NOT NULL)')

            cls.execute_query(f'CREATE TABLE IF NOT EXISTS exame('
                              f'id_exame INTEGER PRIMARY KEY AUTOINCREMENT,'
                              f'id_usuario INTEGER NOT NULL references usuarios(id_usuario),'
                              f'nome_exame TEXT NOT NULL,'
                              f'desc_exame TEXT,'
                              f'hora_exame TEXT NOT NULL,'
                              f'data_exame TEXT NOT NULL)')
            DataMethods.add_users("Arthur", "arthur.faria@gmail.com", "arthur123", "24/08/2004", "M", 19995128382, "A+",1.70, 86.4)

    #Metodo para ver valores do banco
    @classmethod
    def show_users(cls):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        connection.close()
        return usuarios

    @classmethod
    def show_exames(cls, id_usuario):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM exame WHERE id_usuario = {id_usuario}')
        exame = cursor.fetchall()
        connection.close()
        return exame

    @classmethod
    def show_consultas(cls, id_usuario):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM consulta WHERE id_usuario = {id_usuario}')
        consulta = cursor.fetchall()
        connection.close()
        return consulta

    @classmethod
    def show_remedios(cls, id_usuario):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM remedio WHERE id_usuario = {id_usuario}')
        remedio = cursor.fetchall()
        connection.close()
        return remedio


    #Metodo para verificar login
    @classmethod
    def verify_login(cls, email: str, senha: str) -> bool:
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM usuarios')
        data = cursor.fetchall()
        for user in data:
            if user[2] == email:
                if user[3] == senha:
                    return True
                else:
                    return False
            else:
                continue
        connection.close()
        return False

    #Metodos para adicionar/remover/editar usuarios(table)
    @classmethod
    def add_users(cls, nome, email, senha, data_nascimento, sexo, telefone, tipo_sanguineo, altura, peso):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO usuarios(nome, email, senha, data_nascimento, sexo, telefone , tipo_sanguineo, altura, peso) VALUES ("
                       f"'{nome}',"
                       f"'{email}',"
                       f"'{senha}',"
                       f"'{data_nascimento}',"
                       f"'{sexo}',"
                       f"{telefone},"
                       f"'{tipo_sanguineo}',"
                       f"{altura},"
                       f"{peso}"
                       f")")
        connection.commit()
        connection.close()
    @classmethod
    def remove_users(cls, id_usuario):
        cls.execute_query(f"DELETE FROM usuarios WHERE id_usuario = {id_usuario}")

    @classmethod
    def edit_users(cls, id_usuario, senha, telefone, altura, peso):
        cls.execute_query(f"UPDATE usuarios SET senha = '{senha}',"
                          f"telefone = {telefone}, "
                          f"altura = {altura}, "
                          f"peso = {peso} "
                          f"WHERE id_usuario = {id_usuario};")

    @classmethod
    def edit_user_password(cls, id_usuario, senha):
        cls.execute_query(f"UPDATE usuarios SET senha = '{senha}'"
                          f"WHERE id_usuario = {id_usuario};")
        
    #Metodos para adicionar/remover/editar remedios
    @classmethod
    def add_remedio(cls, id_usuario, nome_remedio, desc_remedio, intervalo_uso, primeiro_uso):
        cls.execute_query(f"INSERT INTO remedio(id_usuario, nome_remedio, desc_remedio, intervalo_uso, primeiro_uso) VALUES("
                       f"{id_usuario},"
                       f"'{nome_remedio}',"
                       f"'{desc_remedio}',"
                       f"'{intervalo_uso}',"
                       f"'{primeiro_uso}'"
                       f")")

    @classmethod
    def remove_remedio(cls, id_remedio):
        cls.execute_query(f"DELETE FROM remedio WHERE id_remedio = {id_remedio};")

    @classmethod
    def edit_remedio(cls,id_remedio, nome_remedio, desc_remedio, intervalo_uso, primeiro_uso):
        cls.execute_query(f"UPDATE remedio SET nome_remedio = '{nome_remedio}',"
                          f"desc_remedio = '{desc_remedio}',"
                          f"intervalo_uso = '{intervalo_uso}',"
                          f"primeiro_uso = '{primeiro_uso}'"
                          f"WHERE id_remedio = {id_remedio};")
        
    #Metodos para adicionar/remover/editar consultas
    @classmethod
    def add_consulta(cls, id_usuario, nome_consulta, desc_consulta, hora_consulta, data_consulta):
        cls.execute_query(f"INSERT INTO consulta (id_usuario, nome_consulta, desc_consulta, hora_consulta, data_consulta) VALUES ("
                       f"{id_usuario},"
                       f"'{nome_consulta}',"
                       f"'{desc_consulta}',"
                       f"'{hora_consulta}',"
                       f"'{data_consulta}'"
                       f")")

    @classmethod
    def remove_consulta(cls, id_consulta):
        cls.execute_query(f"DELETE FROM consulta WHERE id_consulta = {id_consulta};")

    @classmethod
    def edit_consulta(cls, id_consulta, nome_consulta, desc_consulta, data_consulta, hora_consulta):
        cls.execute_query(f"UPDATE consulta SET nome_consulta = '{nome_consulta}',"
                          f"desc_consulta = '{desc_consulta}',"
                          f"data_consulta = '{data_consulta}',"
                          f"hora_consulta ='{hora_consulta}'"
                          f"WHERE id_consulta = {id_consulta};")
        
    #Metodos para adicionar/remover/editar exames
    @classmethod
    def add_exame(cls, id_usuario, nome_exame, desc_exame, data_exame, hora_exame):
        cls.execute_query(f"INSERT INTO exame(id_usuario, nome_exame, desc_exame, data_exame, hora_exame) VALUES("
                       f"{id_usuario},"
                       f"'{nome_exame}',"
                       f"'{desc_exame}',"
                       f"'{data_exame}',"
                       f"'{hora_exame}'"
                       f")")

    @classmethod
    def remove_exame(cls, id_exame):
        cls.execute_query(f"DELETE FROM exame WHERE id_exame = {id_exame};")

    @classmethod
    def edit_exame(cls,id_exame, nome_exame, desc_exame, data_exame, hora_exame):
        cls.execute_query(f"UPDATE exame SET nome_exame = '{nome_exame}',"
                          f"desc_exame = '{desc_exame}',"
                          f"data_exame = '{data_exame}',"
                          f"hora_exame = '{hora_exame}' WHERE id_exame = {id_exame};")
