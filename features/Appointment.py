from sqlite3 import *

DATABASE_NAME = "banco.db"


class Appointment:

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
    def show_consultas(cls, id_usuario):
        connection = cls.create_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM consulta WHERE id_usuario = {id_usuario}')
        consulta = cursor.fetchall()
        connection.close()
        return consulta

    @classmethod
    def add_consulta(cls, id_usuario, nome_consulta, desc_consulta, hora_consulta, data_consulta):
        cls.execute_query(
            f"INSERT INTO consulta (id_usuario, nome_consulta, desc_consulta, hora_consulta, data_consulta) VALUES ("
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
