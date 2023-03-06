from flask import Flask,render_template
from product import product_list
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home_page():
    return render_template('home.html',product_list = product_list)

@app.route('/product/<pid>')
def product_show(pid):
    pid = int(pid)
    product = product_list[pid]
    return render_template('product_show.html',product = product)

if __name__ == '__main__':
    app.run(debug=True)