from flask import Flask, render_template
from product import product_list
from product import chair_customize_model_dic,chair_seat_customize_model_color_dic,chair_headandback_customize_model_color_dic
from product import table_electric_customize_model_dic, table_manual_customize_model_dic
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home_page():
    chairList = []
    tableList = []
    fittingList = []
    musicList = []
    for product in product_list:
        if 'chair' in product['type']:
            chairList.append(product)
        if 'table' in product['type']:
            tableList.append(product)
        if 'fitting' in product['type']:
            fittingList.append(product)
        if 'music' in product['type']:
            musicList.append(product)   
    return render_template('home.html', chairList=chairList,
                           tableList=tableList, fittingList=fittingList, musicList=musicList)


@app.route('/product/<pid>')
def product_show(pid):
    pid = str(pid)
    productList: dict
    colorSeatList : dict
    colorHeadAndBackList :dict
    for list in product_list:
        title = list.get('title')
        if title == pid:
            productList = list
    # 椅子客製選項
    if 'chair_customize' == productList.get('type'):
        choiceDict = chair_customize_model_dic
        colorSeatList = chair_seat_customize_model_color_dic
        colorHeadAndBackList = chair_headandback_customize_model_color_dic
    # 桌子客製選項
    if 'table_electric_customize' == productList.get('type'):
        choiceDict = table_electric_customize_model_dic
        colorSeatList = {}
        colorHeadAndBackList = {}
    if 'table_manual_customize' == productList.get('type'):
        choiceDict = table_manual_customize_model_dic
        colorSeatList = {}
        colorHeadAndBackList = {}
    return render_template('product_show.html', product=productList,
                           choiceDict=choiceDict,colorSeatList = colorSeatList,
                           colorHeadAndBackList = colorHeadAndBackList)


if __name__ == '__main__':
    app.run(debug=True)
