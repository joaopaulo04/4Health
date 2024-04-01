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
                              f'data_nascimento INTEGER NOT NULL,'
                              f'sexo TEXT NOT NULL,'
                              f'telefone INTEGER NOT NULL,'
                              f'tipo_sanguineo TEXT NOT NULL,'
                              f'altura INTEGER NOT NULL,'
                              f'peso INTEGER NOT NULL)')

            cls.execute_query(f'CREATE TABLE IF NOT EXISTS agenda('
                              f'id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,'
                              f'id_usuario INTEGER NOT NULL references usuarios(id_usuario),'
                              f'titulo_evento TEXT NOT NULL,'
                              f'desc_evento TEXT,'
                              f'data_evento TEXT NOT NULL,'
                              f'hora_evento TEXT NOT NULL)')

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
                              f'data_consulta TEXT NOT NULL)')

            cls.execute_query(f'CREATE TABLE IF NOT EXISTS exame('
                              f'id_exame INTEGER PRIMARY KEY AUTOINCREMENT,'
                              f'id_usuario INTEGER NOT NULL references usuarios(id_usuario),'
                              f'nome_exame TEXT NOT NULL,'
                              f'desc_exame TEXT,'
                              f'data_exame TEXT NOT NULL)')
    #Metodo para ver valores do banco
    @classmethod
    def show_users(cls):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        connection.close()
        return usuarios
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

    #Metodos para adicionar/remover/editar usuarios(table)
    @classmethod
    def add_users(cls, nome, email, senha, data_nascimento, sexo, telefone , tipo_sanguineo, altura, peso):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO usuarios(nome, email, senha, data_nascimento, sexo, telefone , tipo_sanguineo, altura, peso) VALUES"
                       f"('{nome}',"
                       f"'{email}',"
                       f"'{senha}',"
                       f"{data_nascimento},"
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
        cls.execute_query(f"DELETE FROM usuarios WHERE id = {id_usuario}")
    @classmethod
    def edit_users(cls, id_usuario, senha, telefone, altura, peso):
        cls.execute_query(f"UPDATE usuarios SET"
                       f"senha = '{senha}',"
                       f"telefone = {telefone},"
                       f"altura = {altura},"
                       f"peso = {peso}"
                       f"WHERE id_usuario = {id_usuario}")
    #Metodos para adicionar/remover/editar calendario
    @classmethod
    def add_agenda(cls,id_usuario, titulo_evento, desc_evento, data_evento, hora_evento):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO agenda(id_usuario, titulo_evento, desc_evento, data_evento, hora_evento)VALUES"
                       f"{id_usuario},"
                       f"'{titulo_evento}',"
                       f"'{desc_evento}',"
                       f"'{data_evento}',"
                       f"'{hora_evento}'"
                       f")")
        connection.commit()
        connection.close()
    @classmethod
    def remove_agenda(cls, id_agendamento):
        cls.execute_query(f"DELETE FROM agenda WHERE id = {id_agendamento}")
    @classmethod
    def edit_agenda(cls, id_agendamento, titulo_evento, desc_evento, data_evento, hora_evento):
        cls.execute_query(f"UPDATE agenda SET"
                          f"titulo_evento = '{titulo_evento}',"
                          f"desc_evento = {desc_evento},"
                          f"data_evento = {data_evento},"
                          f"hora_evento = {hora_evento}"
                          f"WHERE id_agendamento = {id_agendamento}")
    #Metodos para adicionar/remover/editar remedios
    @classmethod
    def add_remedio(cls, id_usuario, nome_remedio, desc_remedio, intervalo_uso, primeiro_uso):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO remedio (id_usuario, nome_remedio, desc_remedio, intervalo_uso, primeiro_uso) VALUES"
                       f"({id_usuario},"
                       f"'{nome_remedio}',"
                       f"'{desc_remedio}',"
                       f"'{intervalo_uso}',"
                       f"'{primeiro_uso}'"
                       f")")
        connection.commit()
        connection.close()
    @classmethod
    def remove_remedio(cls, id_remedio):
        cls.execute_query(f"DELETE FROM remedio WHERE id = {id_remedio}")
    @classmethod
    def edit_remedio(cls, nome_remedio, desc_remedio, intervalo_uso, primeiro_uso):
        cls.execute_query(f"UPDATE remedio SET"
                          f"nome_remedio = {nome_remedio},"
                          f"desc_remedio = {desc_remedio},"
                          f"intervalo_uso = {intervalo_uso},"
                          f"primeiro_uso = {primeiro_uso}")
    #Metodos para adicionar/remover/editar consultas
    @classmethod
    def add_consulta(cls, id_usuario, nome_consulta, desc_consulta, data_consulta):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO consulta (id_usuario, nome_consulta, desc_consulta, data_consulta) VALUES"
                       f"({id_usuario},"
                       f"'{nome_consulta}',"
                       f"'{desc_consulta}',"
                       f"'{data_consulta}'"
                       f")")
    @classmethod
    def remove_consulta(cls, id_consulta):
        cls.execute_query(f"DELETE FROM consulta WHERE id = {id_consulta}")

    @classmethod
    def edit_consulta(cls, nome_consulta, desc_consulta, data_consulta):
        cls.execute_query(f"UPDATE remedio SET"
                          f"nome_consulta = {nome_consulta},"
                          f"desc_consulta = {desc_consulta},"
                          f"data_consulta = {data_consulta}")
    #Metodos para adicionar/remover/editar exames
    @classmethod
    def add_exame(cls, id_usuario, nome_exame, desc_exame, data_exame):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO exame (id_usuario, nome_exame, desc_exame, data_exame)VALUES"
                       f"({id_usuario},"
                       f"'{nome_exame}',"
                       f"'{desc_exame}',"
                       f"'{data_exame}'"
                       f")")

    @classmethod
    def remove_exame(cls, id_exame):
        cls.execute_query(f"DELETE FROM exame WHERE id = {id_exame}")

    @classmethod
    def edit_exame(cls, nome_exame, desc_exame, data_exame):
        cls.execute_query(f"UPDATE exame SET"
                          f"nome_exame = {nome_exame},"
                          f"desc_exame = {desc_exame},"
                          f"data_exame = {data_exame}")