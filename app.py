from flask import Flask, render_template
from product import product_list
from product import Backrest_Frame, headrest, Armrest, Seatpad_material, Mechaniam, Base, Casters
from product import head_And_Backrest_Color, seat_Color,special_Color
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
    for list in product_list:
        title = list.get('title')
        if title == pid:
            productList = list
        
    BackrestFrame_List = Backrest_Frame.copy()
    headrest_List = headrest.copy()
    Armrest_List = Armrest.copy()
    Seatpadmaterial_List = Seatpad_material.copy()
    Mechaniam_List = Mechaniam.copy()
    Base_List = Base.copy()
    Casters_List = Casters.copy()
    headAndBackrestColor_List = head_And_Backrest_Color.copy()
    seatColor_List = seat_Color.copy()
    special_Color_List= special_Color.copy()
    # 椅子客製選項
    if 'chair_customize' == productList.get('type'):
        #黑白框
        if('Peacock' == productList.get('title')):
            BackrestFrame_List.remove('白')
        #座墊標配等級Q綿->泡綿->網座    
        if(productList.get('seat_Level') == 2):
            Seatpadmaterial_List.remove('Q綿坐墊')
        #背部可否升級網座    
        #單框僅可選擇透氣網背
        if(productList.get('back_SingleOrDouble') == False):
            headAndBackrestColor_List.pop('HOA網座')
            headAndBackrestColor_List.pop('泡綿布面')
            headAndBackrestColor_List.pop('PVC合成皮')
            headAndBackrestColor_List.pop('真牛皮')
        #雙框部分款式可選擇透氣網背 其餘僅能網座/布面/皮    
        if(productList.get('back_SingleOrDouble') == True):
            if(productList.get('title') == 'Kangaroo' or
               productList.get('title') == 'Bear' or
               productList.get('title') == 'Peacock'):
                headAndBackrestColor_List.pop('透氣網面')   
    # 椅子特規選項
    if 'chair_special' == productList.get('type'):
        if('Kabuto' != productList.get('title')):
            BackrestFrame_List.remove('白')
        if('Viking' != productList.get('title')):
            headrest_List.remove('無頭枕')
        if('Mamba' == productList.get('title')):
            special_Color_List.remove('灰')
        if('Owl' == productList.get('title')):
            headrest_List.remove('有頭枕')
            special_Color_List.clear()
            special_Color_List.add('背部銀灰色 | 椅座黑色')
        if(productList.get('seat_Level') == 4):
            Seatpadmaterial_List.clear()
            Seatpadmaterial_List.append('網座')
            Seatpadmaterial_List.append('泡棉')    
        Armrest_List.clear()
        Armrest_List.append('標配扶手')    
        
        Mechaniam_List.clear()
        Mechaniam_List.append('標配底盤')    
        
        Base_List.clear()
        Base_List.append('標配椅腳')    
        
        Casters_List.clear()
        Casters_List.append('標配椅輪')    
        
        headAndBackrestColor_List.clear()
        
        seatColor_List = special_Color_List
    # 椅子旗艦選項    
    if 'chair_expensive' ==  productList.get('type'):
        headrest_List.clear()
        headrest_List.append('標配頭枕')  
        
        BackrestFrame_List.clear()
        BackrestFrame_List.append('黑')
        
        Armrest_List.clear()
        Armrest_List.append('標配扶手')    
        
        Seatpadmaterial_List.remove('Q綿坐墊')
        Seatpadmaterial_List.remove('圓泡綿')
        Seatpadmaterial_List.remove('小網座')
        Seatpadmaterial_List.remove('方厚成形泡綿')
        
        Mechaniam_List.clear()
        Mechaniam_List.append('標配底盤')    
        
        Base_List.clear()
        Base_List.append('標配椅腳')    
        
        Casters_List.clear()
        Casters_List.append('標配椅輪')    
        
        headAndBackrestColor_List.clear()
        
        seatColor_List.pop('HY彈性布')
    # 桌子客製選項
    if 'table_electric_customize' == productList.get('type'):
        tableDict = table_electric_customize_model_dic
    if 'table_manual_customize' == productList.get('type'):
        tableDict = table_manual_customize_model_dic  
    return render_template('product_show.html', 
                           product = productList,
                           Backrest_Frame = BackrestFrame_List,
                           headrest = headrest_List,
                           Armrest = Armrest_List,
                           Seatpad_material = Seatpadmaterial_List,
                           Mechaniam = Mechaniam_List,
                           Base = Base_List,
                           Casters = Casters_List,
                           head_And_Backrest_Color = headAndBackrestColor_List,
                           seat_Color = seatColor_List)


if __name__ == '__main__':
    app.run(debug=True)
