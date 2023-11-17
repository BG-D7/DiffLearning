import time
from config_reader import config
import sqlite3


class DbWorker:


    def __init__(self):

        self.connection = sqlite3.connect(config.db_name.get_secret_value())
        self.cursor = self.connection.cursor()

    def create_db(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id BIGINT PRIMARY KEY,
        lessons TEXT,
        is_admin BOOL,
        status BOOL
        )
        ''')
        self.connection.commit()
        return 1

    def add_user_to_db(self,uid):
        self.cursor.execute(
            f'INSERT INTO `Users` (`id`, `lessons`, `is_admin`, `status`) VALUES ({uid}, "", 0, 0) ' +
            f'ON CONFLICT(id) DO UPDATE SET `status`=not `status` WHERE `id`={uid};')
        self.connection.commit()
        return 1

    def read_user_lessons(self,uid):
        self.cursor.execute(f"SELECT * FROM `Users` WHERE `id`={uid}")
        status = self.cursor.fetchall()
        self.connection.commit()
        status = status[0][1]
        if len(status)==0: return "Вы не прошли не одного урока"
        else:
            msg = "Вы изучили уроки под номерами: "
            set_lessons = set(status.split("_"))
            set_lessons.discard("")
            list_lessons = sorted([int(j) for j in list(set_lessons)])
            for i in list_lessons: msg+=f"{i},"
            return msg[:-1]

    def append_to_lessons(self,uid,added):
        self.cursor.execute(f"SELECT * FROM `Users` WHERE `id`={uid}")
        status = self.cursor.fetchall()
        status = status[0][1].split("_")
        set_status = set(status)
        set_status.add(added)
        status=""
        for i in set_status:
            status+=f"{i}"+"_"
        self.cursor.execute(f"UPDATE `Users` SET `lessons` = ? WHERE `id`= ?",(status,uid))
        self.connection.commit()

        return 1

    def is_admin(self,uid):
        self.cursor.execute(f"SELECT is_admin FROM `Users` WHERE `id`={uid}")
        self.connection.commit()
        return bool(int(self.cursor.fetchall()[0][0]))

    def mgmt_admin(self,uid,status=1):
        self.cursor.execute(f"UPDATE `Users` SET `is_admin` = {status} WHERE `id`={uid}")
        self.connection.commit()
        return 1


    def close_connect(self):
        self.connection.commit()
        self.connection.close()
