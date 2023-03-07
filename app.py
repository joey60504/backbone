from flask import Flask,render_template
from product import product_list
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home_page():
    return render_template('home.html',product_list = product_list)

@app.route('/product/<pid>')
def product_show(pid):
    pid = str(pid)
    productList:dict
    for list in product_list:
        title = list.get('title')
        if title == pid:
            productList = list
    return render_template('product_show.html',product = productList)

if __name__ == '__main__':
    app.run(debug=True)