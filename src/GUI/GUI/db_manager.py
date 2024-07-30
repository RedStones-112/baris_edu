import sqlite3
import pandas as pd
from GUI.abs import DBAbstractClass
from GUI.config import DBConfig

class DBManager(DBAbstractClass):
    def __init__(self) -> None:
        self.connect_db()

    
    def make_db_base(self):
        try:
            self.make_table()
        except:
            pass
        data = DBConfig.base_data
        
        for command in data:
            self.cur.execute('''
                INSERT INTO robot_command_list (cmd, par1, par2, par3, par4, par5) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (command['cmd'], command['par1'], command['par2'], command['par3'], command['par4'], command['par5']))

        self.con.commit()

    def set_cammand(self, cmd, par1, par2, par3, par4, par5):
        self.cur.execute('''
                INSERT INTO robot_command_list (cmd, par1, par2, par3, par4, par5) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (cmd, par1, par2, par3, par4, par5))

        self.con.commit()

    
    def get_cammand(self, ID) -> dict:
        if type(ID) != int :
            print("unable ID")
            return
        self.cur.execute(f'''SELECT * FROM robot_command_list WHERE id = {ID};''')
        rows = self.cur.fetchone()
        # print(dict(rows))
        try:
            return dict(rows)
        except TypeError:
            return
        
    
    def get_max_id(self) -> int:
        self.cur.execute(DBConfig.max_id_query)
        max_id = dict(self.cur.fetchone())["MAX(id)"]
        return int(max_id)

    
    def connect_db(self):
        self.con = sqlite3.connect(DBConfig.db_path)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    
    def disconnect_db(self):
        del(self.cur)
        self.con.close()

    def show_table(self):
        self.cur.execute(DBConfig.all_data_query)
        rows = self.cur.fetchall()
        print(rows)

    def make_table(self):
        self.cur.execute(DBConfig.create_table_query)


    def __del__(self):
        try:
            self.disconnect_db()
            print("auto disconnect activate")
        except:
            pass

if __name__ == "__main__":
    db = DBManager()
    # db.get_cammand(4)
    # db.set_cammand()
    # db.make_table()
    db.disconnect_db()