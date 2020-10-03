from flask import Flask
import mariadb
import json

app = Flask(__name__)

config = {
    'host': 'database',
    'port': 3306,
    'user': 'root',
    'password': 'practica8',
    'database': 'SA'
}

@app.route("/")
def initApp():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("select *from Estudiante;")

    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]

    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    return json.dumps(json_data)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)