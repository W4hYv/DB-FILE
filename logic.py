import sqlite3
from config import DATABASE, TOKEN

class DB_Manager:
    def __init__(self, database):
        self.database = database
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)

        with conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS skills (
                skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                skill_name TEXT UNIQUE
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS status (
                status_id INTEGER PRIMARY KEY AUTOINCREMENT,
                status_name TEXT UNIQUE
            )''')

            conn.execute('''CREATE TABLE IF NOT EXISTS projects (
                project_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                project_name TEXT,
                description TEXT,
                url TEXT,
                status_id INTEGER,
                FOREIGN KEY (status_id) REFERENCES status (status_id)
            )''')
            
            conn.execute('''CREATE TABLE IF NOT EXISTS project_skills (
                project_id INTEGER,
                skill_id INTEGER,
                FOREIGN KEY(project_id) REFERENCES projects(project_id),
                FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
            )''')

            conn.commit()

        print("Tables created successfully.")

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()

    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()

    def default_insert(self):     
        skills = [ (_,) for _ in (['Python', 'SQL', 'API', 'Discord'])]
        statuses = [ (_,) for _ in (['Pembuatan Prototipe', 'Dalam Pengembangan', 'Selesai, siap digunakan', 'Diperbarui', 'Selesai, tapi tidak sedang dilanjutkan'])]
        
        sql_skills = 'INSERT OR IGNORE INTO skills (skill_name) values(?)'
        self.__executemany(sql_skills, skills)
        
        sql_status = 'INSERT OR IGNORE INTO status (status_name) values(?)'
        self.__executemany(sql_status, statuses)

    def insert_project(self, data):
        sql = """INSERT INTO projects (user_id, project_name, url, status_id) values(?, ?, ?, ?)"""
        self.__executemany(sql, data)

    def get_statuses(self):
        sql = "SELECT status_name from status"
        return self.__select_data(sql)

    def update_projects(self, param, data):
        sql = f"""UPDATE projects SET {param} = ? WHERE project_name = ? AND user_id = ?"""
        self.__executemany(sql, [data]) 

    def delete_project(self, user_id, project_id):
        sql = """DELETE FROM projects WHERE user_id = ? AND project_id = ? """
        self.__executemany(sql, [(user_id, project_id)])

    def get_projects(self, user_id):
        sql = """SELECT * FROM projects WHERE user_id = ?"""
        return self.__select_data(sql, data = (user_id,))

    def delete_status_by_id(self, status_id):
        sql = "DELETE FROM status WHERE status_id = ?"
        self.__executemany(sql, [(status_id,)])
        print(f"Status dengan ID {status_id} berhasil dihapus.")

    def add_new_skill(self, skill_name):
        sql = "INSERT OR IGNORE INTO skills (skill_name) VALUES (?)"
        self.__executemany(sql, [(skill_name,)])
        print(f"Keterampilan '{skill_name}' berhasil ditambahkan.")

    def update_project_status(self, user_id, project_name, status_id):
        sql = "UPDATE projects SET status_id = ? WHERE project_name = ? AND user_id = ?"
        self.__executemany(sql, [(status_id, project_name, user_id)])
        print(f"Status proyek '{project_name}' berhasil diperbarui ke ID {status_id}.")

    def delete_skill(self, project_id, skill_id):
        sql = """DELETE FROM project_skills WHERE skill_id = ? AND project_id = ? """
        self.__executemany(sql, [(skill_id, project_id)])

    def get_status_id(self, status_name):
        sql = "SELECT status_id FROM status WHERE status_name = ?"
        res = self.__select_data(sql, (status_name,))
        return res[0][0] if res else None

    def get_skills(self):
        sql = "SELECT * FROM skills"
        return self.__select_data(sql)

    def get_project_id(self, project_name, user_id):
        sql = "SELECT project_id FROM projects WHERE project_name = ? AND user_id = ?"
        res = self.__select_data(sql, (project_name, user_id))
        return res[0][0] if res else None

    def insert_skill(self, user_id, project_name, skill_name):
        project_id = self.get_project_id(project_name, user_id)

        sql_skill = "SELECT skill_id FROM skills WHERE skill_name = ?"
        res_skill = self.__select_data(sql_skill, (skill_name,))
        skill_id = res_skill[0][0] if res_skill else None
        
        if project_id and skill_id:
            sql_insert = "INSERT INTO project_skills (project_id, skill_id) VALUES (?, ?)"
            self.__executemany(sql_insert, [(project_id, skill_id)])
