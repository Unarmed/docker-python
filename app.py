from flask import Flask
from flask import request
import psycopg2
import sys

con = psycopg2.connect(host='postgres', port='5432', database='postgres', user='postgres', password='secret')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS reverse (input VARCHAR(255), output VARCHAR(255))")
con.commit()

app = Flask(__name__)
@app.route("/reverse", methods = ["POST"])
def reverse():
    reverse = request.get_data()[::-1]
    cur = con.cursor()
    cur.execute("INSERT INTO reverse VALUES ('" + request.get_data() + "', '" + reverse + "')")
    con.commit()
    return reverse

@app.route("/cache", methods = ["GET"])
def get():
    cur = con.cursor()
    cur.execute('SELECT * FROM reverse')
    return str(cur.fetchall())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
