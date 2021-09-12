import sqlite3
from dataclasses import dataclass

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

class Database:
    def __init__(self, name):
        self.conn = sqlite3.connect(name + ".db")
        self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY,title STRING, content STRING NOT NULL ); ")

    def add(self, note : "Note"):
        title = note.title
        content = note.content

        sql = f"INSERT INTO note (title, content) VALUES ('{title}','{content}')"
        self.conn.execute(sql)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        notes = []
        for line in cursor:
            id = line[0]
            title = line[1]
            content = line[2]
            new_note = Note(id, title, content)
            notes.append(new_note)
        return notes

    def update(self, entry : "Note"):
        id = entry.id
        title = entry.title
        content = entry.content
        sql = f"UPDATE note SET title = '{title}', content = '{content}'  WHERE id = {id}"
        self.conn.execute(sql)
        self.conn.commit()
    
    def delete(self, note_id : int):
        sql = f"DELETE FROM note WHERE id = {note_id}"
        self.conn.execute(sql)
        self.conn.commit()



