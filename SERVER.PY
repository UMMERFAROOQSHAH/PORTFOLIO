from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7006760858",
    database="ME"
)
cursor = db.cursor()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    sql = "INSERT INTO FORM (id, name, phone, address, email, query) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (data['id'], data['name'], data['phone'], data['address'], data['email'], data['query'])

    try:
        cursor.execute(sql, values)
        db.commit()
        return jsonify({"message": "Form submitted successfully!"})
    except Exception as e:
        return jsonify({"message": "Error inserting data into MySQL", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
