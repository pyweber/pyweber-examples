from manage_sql import SQLITE
from manage_sql.Utils.utils_sqlite import Column, ColumnData, Types

class Database:
    def __init__(self):
        # create database
        self.db = SQLITE(database='users')

        # create table
        self.db.create_table(
            tablename='usuarios',
            columns=[
                Column(
                    name='username',
                    column_type=Types.text
                ),
                Column(
                    name='email',
                    column_type=Types.text
                ),
                Column(
                    name='password',
                    column_type=Types.text
                )
            ]
        )
        self.inserting_data()

    def inserting_data(self):
        # inserting data
        for user in [['webtech', "webtech@email.com", 'Aa123'], ['devpython', "devpython@email.com", 'Aa124']]:
            self.db.insert_data(
                tablename='usuarios',
                insert_query=[
                    ColumnData(
                        column='username',
                        value=user[0]
                    ),
                    ColumnData(
                        column='email',
                        value=user[1]
                    ),
                    ColumnData(
                        column='password',
                        value=self.db.encrypt_value(user[-1])
                    )
                ]
            )

if __name__ == '__main__':
    Database()