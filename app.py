from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# MySQL connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",  # your MySQL password
    database="expen_db"
)
cursor = db.cursor()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        house_rent = float(request.form['house_rent'])
        water_bill = float(request.form['water_bill'])
        school_fees = float(request.form['school_fees'])
        kitchen_spend = float(request.form['kitchen_spend'])
        other_spend = float(request.form['other_spend'])

        total = house_rent + water_bill + school_fees + kitchen_spend + other_spend

        cursor.execute("""INSERT INTO users
            (name, house_rent, water_bill, school_fees, kitchen_spend, other_spend, total)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (name, house_rent, water_bill, school_fees, kitchen_spend, other_spend, total))

        db.commit()
        return redirect('/')

    cursor.execute("SELECT * FROM users ORDER   BY id DESC")
    data = cursor.fetchall()
    return render_template('index.html', users =data)


if __name__ == '__main__':
    app.run(debug=True)
