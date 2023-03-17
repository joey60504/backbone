# type命名規則:
#     椅子:
#     客製款-->chair_customize
#     特規款-->chair_special
#     旗艦款-->chair_expensive
#     桌子:
#     電動款-->table_electric_customize
#     手動款-->table_manual_customize
#     配件:
#     椅款配件-->fitting_c
#     桌款配件-->fitting_t
#     其他配件-->fitting_o
#     wavebone:
#     一般款:music_customize

# 'image :"", 圖片位址 
# 'title': '',產品名
# 'type': '',型別
# 'price': ,價格
# 'is_published':,是否有貨
# 'seat_Level':,坐墊等級 1=Q綿起 2=泡綿起 3=旗艦款 4=特規款
# 'back_SingleOrDouble': 單框=False 雙框=True,
    

product_list = [{
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzI2NDUxMDM2LzE2MzUxNTQzMTBfMmJmYmJmMDAwZDVhNTE0YjNmMjIuanBlZyJdLFsicCIsInRodW1iIiwiNjAweDYwMCJdXQ.jpeg?sha=7d4f36ec98355041",
    'title': 'Kangaroo',
    'type': 'chair_customize',
    'price': 7080,
    'is_published': True,
    'seat_Level':2,
    'back_SingleOrDouble':True,
    
},
    {
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzI2NDUxMDM5LzE2MjYzMTg5MjBfNTg1YjA5MTM2MWRhNWNlZmM5OTMuanBlZyJdLFsicCIsInRodW1iIiwiNjAweDYwMCJdXQ.jpeg?sha=15eaea97635bf078",
    'title': 'Bear',
    'type': 'chair_customize',
    'price': 7080,
    'is_published': True,
    'seat_Level':2,
    'back_SingleOrDouble':True
},
    {
    'image' :"https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzI5NzkzNTM4L-e2sl8yN2Y5YmRhMGMxOGY0MWVjMjQxMC5qcGVnIl0sWyJwIiwidGh1bWIiLCI2MDB4NjAwIl1d.jpeg?sha=c99764ebffbed854",
    'title': 'KingKong',
    'type': 'chair_expensive',
    'price': 20400,
    'is_published': True,
    'seat_Level':3,
    'back_SingleOrDouble':True
},
    {
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzMzNjc2MDczLzE2MjE0MDM4MzVfYjQzYmQ2NTNhMzBhMWIxMTRkNGQuanBlZyJdLFsicCIsInRodW1iIiwiNjAweDYwMCJdXQ.jpeg?sha=bc0f38bc9a5e18c8",
    'title': 'Kabuto',
    'type': 'chair_special',
    'price': 12880,
    'is_published': True,
    'seat_Level':4,
    'back_SingleOrDouble':True
},
    {
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzM0MjYwMDA1LzE2Mjg4NDY4ODBfZTk5ODQwMWQ3NDE5OTAwMzc5MmUuanBlZyJdLFsicCIsInRodW1iIiwiNjAweDYwMCJdXQ.jpeg?sha=6c3712c8fc3d756a",
    'title': 'Mamba',
    'type': 'chair_special',
    'price': 7880,
    'is_published': True,
    'seat_Level':4,
    'back_SingleOrDouble':True
},
    {
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzI2NDUxMDE5L0hZLTA2TV80ZjdiNjMyMzczMjQ1MzBmMmQ5Yi5qcGVnIl0sWyJwIiwidGh1bWIiLCI2MDB4NjAwIl1d.jpeg?sha=23a2fe0bff2473ee",
    'title': 'Eagle',
    'type': 'chair_customize',
    'price': 4280,
    'is_published': True,
    'seat_Level':1,
    'back_SingleOrDouble':False
},
    {
    'image':"https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzM4ODE4NDM1LzE2NzAyMzI5NDVfMDRmY2UyNjEzYzM5MGQ0OGZhODAucG5nIl0sWyJwIiwidGh1bWIiLCI2MDB4NjAwIl1d.png?sha=f2a9d76f075b65d5",
    'title': 'Owl',
    'type': 'chair_special',
    'price': 4600,
    'is_published': True,
    'seat_Level':4,
    'back_SingleOrDouble':False
},
    {
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzI2NDUxMDU0L-iqv-aVtOakheasvuWkp-Wwjy02MDB4NjAwXzYzMzM2OGFjMTNkNjMxYTlmYmJkLmpwZWciXSxbInAiLCJ0aHVtYiIsIjYwMHg2MDAiXV0.jpeg?sha=db736b12dbd55910",
    'title': 'Ox',
    'type': 'chair_customize',
    'price': 5800,
    'is_published': True,
    'seat_Level':2,
    'back_SingleOrDouble':True
},
    {
    'image' :"https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzI2NDUxMDU3L2h5LTA2bV9kZGVlZmIwNmQzMDg2MmIxNWYxMi5qcGVnIl0sWyJwIiwidGh1bWIiLCI2MDB4NjAwIl1d.jpeg?sha=80b62c67d84b0789",
    'title': 'Hydra Lite',
    'type': 'chair_customize',
    'price' :4280,  
    'is_published': True,
    'seat_Level':1,
    'back_SingleOrDouble':True
},
    {
    'image':"https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzI3MjAwMDk4L0hZLTAxTV9hNTU1NTk3NmQ3YTZhOWI3ZmMwNC5qcGVnIl0sWyJwIiwidGh1bWIiLCI2MDB4NjAwIl1d.jpeg?sha=5b8483649b9bd3b8",
    'title': 'Koala',
    'type': 'chair_customize',
    'price' :4380,  
    'is_published': True,
    'seat_Level':1,
    'back_SingleOrDouble':True  
},
    {
    'image' : "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzI2NDUxMDQyL0hZLTAxTV82YTdlYTUzOTQ4NzJiMTcyMmViOC5qcGVnIl0sWyJwIiwidGh1bWIiLCI2MDB4NjAwIl1d.jpeg?sha=b518a24764b00195",
    'title': 'Deer',
    'type': 'chair_customize',
    'price' :4280,  
    'is_published': True,
    'seat_Level':1,
    'back_SingleOrDouble':False
},
    {
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzMxNDgzNDg4LzE2NTc1MTczNTNfZDI3NTFjNGFiYTdhYTljMDU1M2MuanBlZyJdLFsicCIsInRodW1iIiwiNjAweDYwMCJdXQ.jpeg?sha=c90d0a01e904ec4e",
    'title': 'Dyback04',
    'type': 'table_electric_customize',
    'price': 15700,
    'is_published': True
},
    {
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzI4OTM1MTE4L-aDheWig182MDB4NjAwXzAyXzMyYjZiM2I4NjkwNzc5YzYwZmFkLmpwZWciXSxbInAiLCJ0aHVtYiIsIjYwMHg2MDAiXV0.jpeg?sha=893eb46851454625",
    'title': 'CityDesk',
    'type': 'table_manual_customize',
    'price': 8888,
    'is_published': True
},
    {
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzM5NDk4MzU5LzE2NzYzNjkyNDNfNDg3YzdhZDM0ODBkOGE0ZTNjMjcucG5nIl0sWyJwIiwidGh1bWIiLCI2MDB4NjAwIl1d.png?sha=f8abfa93941cb936",
    'title': 'Reef桌上平台螢幕架',
    'type': 'fitting_t',
    'price': 1200,
    'is_published': True
},
    {
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzM3MTA4NDA5LzE2NTQ4NTY0NDJfNGZjYTA0YjU5MGE5N2YxZGVjZTIucG5nIl0sWyJwIiwidGh1bWIiLCI2MDB4NjAwIl1d.png?sha=e4657b6df73325f0",
    'title': 'JellyFish透氣腳拖',
    'type': 'fitting_c',
    'price': 2000,
    'is_published': True
},
    {
    'image': "https://cdn1.cybassets.com/media/W1siZiIsIjExNTM0L3Byb2R1Y3RzLzI5NzMzNzU4LzQ1XzNhZDdhY2Q3YTY5ZmI0NzAwY2ZiLmpwZWciXSxbInAiLCJ0aHVtYiIsIjYwMHg2MDAiXV0.jpeg?sha=20774b2527efa5eb",
    'title': 'headquarter音樂工作站',
    'type': 'music_customize',
    'price': 22900,
    'is_published': True
}
]
#桌款客製
table_electric_customize_model_dic = {
    '大小': [
        '123cm*70cm', '150cm*75cm'
    ],
    '桌板顏色': [
        '黑', '白', '拼接木紋', '淺木紋'
    ],
    '桌腳顏色': [
        '黑', '白'
    ]
}
table_manual_customize_model_dic = {
    '大小': [
        '120cm*60cm'
    ],
    '桌款顏色': [
        '黑桌+黑腳', '白桌+白腳', '拼接木紋桌+黑腳', '淺木紋桌+白腳'
    ]
}
Backrest_Frame = [
    '黑','白'
]
headrest = [
    '無頭枕','有頭枕'
]
Armrest = [
    '無扶手', '1D', '旋轉1D', '3D', '3D肘拖', '旋轉3D扶手'
]
Seatpad_material = [
    'Q綿坐墊', '方厚成形泡綿','圓泡綿','小網座', '強力網座', 'PVC合成皮', '全牛皮'
]
Mechaniam = [
    'STG分離傾仰', 'XTG多段傾仰', 'SXTG滑動座殼'
]
Base = [
    '尼龍椅腳', '鋁製椅腳'
]
Casters = [
    '固定椅腳', 'PP耐磨椅輪', 'PU靜音椅輪'
]
head_And_Backrest_Color = {
    'HOA網座': {
        'HOA網座': [
            'BMF-01文墨黑', 'BMF-02盎然綠', 'BMF-03晴空藍', 'BMF-04香檳金',
            'BMF-06稻穗黃', 'BMF-07銀河灰', 'BMF-08尊貴黃', 'BMF-09烈焰紅', 'BMF-10葵花橘'
        ]
    },
    '透氣網面': {
        'HY彈性網布': [
            'BK-01M炭晶黑', 'BK-02M韓花紅', 'BK-04M草原綠', 'BK-06M沉靜灰', 'BK-07M米月白', 'BK-08M秋波藍', 'BK-09M東方藍'
        ]
    },
    '泡綿布面': {
        '雨點布': [
            '26-60雅典黑', '26-61暖灰', '26-63玉子黃', '26-64珊瑚灰', '26-65紅鬱金',
            '26-66芥子綠', '26-67海水藍', '26-68瑪瑙紅', '26-69朽葉棕'
        ],
        '傢飾布': [
            '37-102珍珠白', '37-102-1唐茶棕', '37-102-2銀鼠棕', '37-102-3青竹綠', '37-102-4赤緋紅', '37-102-5燕脂紅',
            '37-102-6菖蒲紫', '37-102-7秋夜藍', '37-102-8銀月灰', '37-102-9玄鐵灰', '37-102-10琵琶棕',
            '37-102-11博雅黑', '37-102-12藤黃', 'C03-1象牙白', 'C03-2白茶棕', 'C03-3水銀灰', 'C03-4胭脂紅',
            'C03-5深緋紅', 'C03-6桔梗紫', 'C03-7群青藍', 'C03-8黑橡藍', 'C03-9桑茶黃', 'C03-10秋芒綠', 'C03-11深川藍',
            'C03-12千歲綠', 'C03-13白橡灰', 'C03-14礪茶棕', 'C03-15焦茶棕', 'C03-16胡桃灰', 'C03-17古月灰', 'C03-18遂空黑'
        ]
    },
    'PVC合成皮': {
        'PVC合成皮': [
            '黑'
        ]
    },
    '真牛皮': {
        '真牛皮': [
            '黑'
        ]
    }
}
seat_Color = {
    'HOA網座': {
        'HOA網座': [
            'BMF-01文墨黑', 'BMF-02盎然綠', 'BMF-03晴空藍', 'BMF-04香檳金',
            'BMF-06稻穗黃', 'BMF-07銀河灰', 'BMF-08尊貴黃', 'BMF-09烈焰紅', 'BMF-10葵花橘'
        ]
    },
    'HY彈性布': {
        '彈性布': [
            'BK-01炭晶黑', 'BK-02韓花紅', 'BK-03灣岸藍'
        ],
        '雨點布': [
            '26-60雅典黑', '26-61暖灰', '26-63玉子黃', '26-64珊瑚灰', '26-65紅鬱金',
            '26-66芥子綠', '26-67海水藍', '26-68瑪瑙紅', '26-69朽葉棕'
        ],
        '傢飾布': [
            '37-102珍珠白', '37-102-1唐茶棕', '37-102-2銀鼠棕', '37-102-3青竹綠', '37-102-4赤緋紅', '37-102-5燕脂紅',
            '37-102-6菖蒲紫', '37-102-7秋夜藍', '37-102-8銀月灰', '37-102-9玄鐵灰', '37-102-10琵琶棕',
            '37-102-11博雅黑', '37-102-12藤黃', 'C03-1象牙白', 'C03-2白茶棕', 'C03-3水銀灰', 'C03-4胭脂紅',
            'C03-5深緋紅', 'C03-6桔梗紫', 'C03-7群青藍', 'C03-8黑橡藍', 'C03-9桑茶黃', 'C03-10秋芒綠', 'C03-11深川藍',
            'C03-12千歲綠', 'C03-13白橡灰', 'C03-14礪茶棕', 'C03-15焦茶棕', 'C03-16胡桃灰', 'C03-17古月灰', 'C03-18遂空黑'
        ]
    },
    'PVC合成皮': {
        'PVC合成皮': [
            '黑'
        ]
    },
    '真牛皮': {
        '真牛皮': [
            '黑'
        ]
    }
}
special_Color = {
    '黑','灰'
}