from sqlite3 import *

DATABASE_NAME = "banco.db"


class Exam:

    @classmethod
    def create_connection(cls):
        connection = connect(f'{DATABASE_NAME}')
        return connection

    @classmethod
    def execute_query(cls, query):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    @classmethod
    def show_exames(cls, id_usuario):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM exame WHERE id_usuario = {id_usuario}')
        exame = cursor.fetchall()
        connection.close()
        return exame

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
    def edit_exame(cls, id_exame, nome_exame, desc_exame, data_exame, hora_exame):
        cls.execute_query(f"UPDATE exame SET nome_exame = '{nome_exame}',"
                          f"desc_exame = '{desc_exame}',"
                          f"data_exame = '{data_exame}',"
                          f"hora_exame = '{hora_exame}' WHERE id_exame = {id_exame};")
