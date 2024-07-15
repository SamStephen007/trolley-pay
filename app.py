from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Route to render the form
@app.route('/')
def index():
    return render_template('trolley.html')

# Route to handle form submission
@app.route('/addItem', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get data from the form
        product = request.form['product']
        quantity = request.form['quantity']
        price = request.form['price']
        
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            host='localhost',
            database='sam_stephen',
            user='postgres',
            password='9789114664'
        )
        cur = conn.cursor()
        
        # Insert data into the database
        cur.execute('INSERT INTO trolley (product, quantity,price) VALUES (%s, %s,%s)', (product, quantity,price))
        
        # Commit changes and close connection
        conn.commit()
        cur.close()
        conn.close()

        return "Data entered"
        

if __name__ == '__main__':
    app.run(debug=True)
