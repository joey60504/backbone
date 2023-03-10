from flask import Flask, render_template
from product import product_list
from product import Backrest_Frame, headrest, Armrest, Seatpad_material, Mechaniam, Base, Casters
from product import head_And_Backrest_Color, seat_Color, special_Color
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
    productList = {}
    choiceDict = {}
    colorDict = {}
    for list in product_list:
        title = list.get('title')
        if title == pid:
            productList = list
    BackrestFrame = Backrest_Frame.copy()
    Seatpadmaterial = Seatpad_material.copy()
    headAndBackrestColor = head_And_Backrest_Color.copy()
    seatColor = seat_Color.copy()
    specialColor = special_Color.copy()
    # 椅子客製選項
    if 'chair_customize' == productList.get('type'):
        #黑白框
        if('Peacock' == productList.get('title')):
            BackrestFrame.append('白')
        #座墊標配等級Q綿->泡綿->網座    
        if(productList.get('seat_Level') == 2):
            Seatpadmaterial.remove('Q綿坐墊')
        #背部可否升級網座    
        #單框僅可選擇透氣網背
        if(productList.get('back_SingleOrDouble') == False):
            headAndBackrestColor.pop('HOA網座')
            headAndBackrestColor.pop('泡綿布面')
            headAndBackrestColor.pop('PVC合成皮')
            headAndBackrestColor.pop('真牛皮')
        #雙框部分款式可選擇透氣網背 其餘僅能網座/布面/皮    
        if(productList.get('back_SingleOrDouble') == True):
            if(productList.get('title') == 'Kangaroo' or
               productList.get('title') == 'Bear' or
               productList.get('title') == 'Peacock'):
                headAndBackrestColor.pop('透氣網面')   
        choiceDict["背框(Backrest Frame)"] = BackrestFrame
        choiceDict["頭枕(Headrest)"] = headrest
        choiceDict["扶手(Armrest)"] = Armrest
        choiceDict["坐墊材質(Seatpad Material)"] = Seatpadmaterial
        choiceDict["底盤功能(Mechaniam)"] = Mechaniam
        choiceDict["椅腳(Base)"] = Base
        choiceDict["椅輪(Casters)"] = Casters
        colorDict["頭枕、椅背顏色(BackRest & HeadRest Color)"] = headAndBackrestColor
        colorDict["坐墊顏色(Seatpad Color)"] = seatColor
    # 椅子特規選項
    if 'chair_special' == productList.get('type'):
        if('Kabuto' == productList.get('title')):
            BackrestFrame.append('白')
        if(productList.get('seat_Level') == 4):
            Seatpadmaterial.remove('Q綿坐墊')
            Seatpadmaterial.remove('圓泡綿')
            Seatpadmaterial.remove('小網座')
            Seatpadmaterial.remove('PVC合成皮')
            Seatpadmaterial.remove('全牛皮')
        if('Mamba' == productList.get('title')):
            specialColor.remove('灰')
        elif('Owl' == productList.get('title')):
            specialColor.clear()
            specialColor.add('頭枕背部銀灰色 | 椅座黑色')
        choiceDict["背框(Backrest Frame)"] = BackrestFrame
        choiceDict["坐墊材質(Seatpad Material)"] = Seatpadmaterial
        colorDict["椅面顏色(Chair Color)"] = specialColor
    # 椅子旗艦選項    
    if 'chair_expensive' ==  productList.get('type'):
        Seatpadmaterial.remove('Q綿坐墊')
        Seatpadmaterial.remove('圓泡綿')
        Seatpadmaterial.remove('小網座')
        Seatpadmaterial.remove('方厚成形泡綿')
        headAndBackrestColor.pop('透氣網面')  
        headAndBackrestColor.pop('泡綿布面')  
        choiceDict["椅面材質(Chair Material)"] = Seatpadmaterial  
        choiceDict["椅輪(Casters)"] = Casters
        colorDict["椅面顏色(Chair Color)"] = headAndBackrestColor      
    # 桌子客製選項
    if 'table_electric_customize' == productList.get('type'):
        choiceDict = table_electric_customize_model_dic
    if 'table_manual_customize' == productList.get('type'):
        choiceDict = table_manual_customize_model_dic
    return render_template('product_show.html', product=productList, choiceDict=choiceDict ,colorDict = colorDict)


if __name__ == '__main__':
    app.run(debug=True)
