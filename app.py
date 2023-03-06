from flask import Flask,render_template
from product import product_list
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html',product_list = product_list)

@app.route('/route_name')
def product_show():
    return render_template('product_show.html')

if __name__ == '__main__':
    app.run(debug=True)