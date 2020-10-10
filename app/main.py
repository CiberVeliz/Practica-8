from flask import Flask
import sqlite3
import json
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
DATABASE_PATH = os.path.join(APP_ROOT, '../database')

@app.route("/")
def initApp():
    conn = sqlite3.connect(os.path.join(DATABASE_PATH, 'dbpractica9.db'))
    cur = conn.cursor()
    cur.execute("select *from Estudiante;")

    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]

    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    conn.close()

    return json.dumps(json_data)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)