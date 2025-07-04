from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    date = request.form['date']
    conn = mysql.connector.connect(
        host='database-1.ca9a0e62indh.us-east-1.rds.amazonaws.com',
        user='admin',
        password='mahammad',
        database='your_database_name'
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (name, date) VALUES (%s, %s)", (name, date))
    conn.commit()
    conn.close()
    return "Booking successful!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
