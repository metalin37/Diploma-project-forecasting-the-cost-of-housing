import json
import pickle
import numpy as np
 
flatTypes = None
cities = None
regions = None
materialTypes = None
data_columns = None
model = None


# создаем необходимые словари
# dic_flatType = {
#     'Свободная планировка': 'flatType_openPlan',
#     'Комнаты': 'flatType_rooms',
#     'Студия': 'flatType_studio'
# }
# dic_region = {
#     'Крым': 'region_crimea',
#     'Краснодарский': 'region_krasnodar',
#     'Севастополь': 'region_sevastopol'
# }
# dic_city = {
#     'Алушта': 'city_alushta',
#     'Анапа': 'city_anapa',
#     'Балаклавский район': 'city_balaklavskiy',
#     'Евпатория': 'city_evpatoriya',
#     'Феодосия': 'city_feodosiya',
#     'Гагаринский район': 'city_gagarinskiy',
#     'Генелджик': 'city_gelendzhik',
#     'Керчь': 'city_kerch',
#     'Ленинский район': 'city_leninskiy',
#     'Нахимовский район': 'city_nakhimovskiy',
#     'Новороссийск': 'city_novorossiysk',
#     'Саки': 'city_saki',
#     'Сакский район': 'city_sakskiy',
#     'Симферополь': 'city_simferopol',
#     'Симферопольский район': 'city_simferopolskiy',
#     'Сочи': 'city_sochi',
#     'Судак': 'city_sudak',
#     'Туапсе': 'city_tuapse',
#     'Туапсинский район': 'city_tuapsinskiy',
#     'Ялта': 'city_yalta',
# }
dic_cityPopulation = {
    'city_novorossiysk': 274956,
    'city_anapa': 88879,
    'city_sochi': 443562,
    'city_simferopol': 342054,
    'city_gelendzhik': 76783,
    'city_yalta': 79056,
    'city_gagarinskiy': 159017,
    'city_leninskiy': 58441,
    'city_evpatoriya': 108248,
    'city_feodosiya': 68001,
    'city_alushta': 30088,
    'city_kerch': 151548,
    'city_nakhimovskiy': 119507,
    'city_simferopolskiy': 161997,
    'city_tuapse': 61180,
    'city_saki': 24654,
    'city_balaklavskiy': 51092,
    'city_sakskiy': 76426,
    'city_tuapsinskiy': 127717,
    'city_sudak': 16489,
}
dic_cityArea = {
    'city_novorossiysk': 83.5,
    'city_anapa': 59,
    'city_sochi': 176.8,
    'city_simferopol': 107.4,
    'city_gelendzhik': 19.25,
    'city_yalta': 18.2,
    'city_gagarinskiy': 61.1,
    'city_leninskiy': 2918.6,
    'city_evpatoriya': 65,
    'city_feodosiya': 40,
    'city_alushta': 7,
    'city_kerch': 108,
    'city_nakhimovskiy': 267.7,
    'city_simferopolskiy': 1752.5,
    'city_tuapse': 33.4,
    'city_saki': 28.7,
    'city_balaklavskiy': 530.3,
    'city_sakskiy': 2257.5,
    'city_tuapsinskiy': 2399.2,
    'city_sudak': 23.5,
}
# dic_materialType = {
#     'Газобетонный блок': 'materialType_aerocreteBlock',
#     'Блок': 'materialType_block',
#     'Кирпич район': 'materialType_brick',
#     'Пенобетонный блок': 'materialType_foamConcreteBlock',
#     'Газовый силикатный блок': 'materialType_gasSilicateBlock',
#     'Монолит': 'materialType_monolith',
#     'Монолитный кирпич': 'materialType_monolithBrick',
#     'Старый': 'materialType_old',
#     'Панель': 'materialType_panel',
#     'Сталинка': 'materialType_stalin',
#     'Неизвестно': 'materialType_unknown',
#     'Каркас': 'materialType_wireframe',
#     'Дерево': 'materialType_wood',
# }

dic_populationDencity = {k: dic_cityPopulation.get(k, 0) / dic_cityArea.get(k, 0) for k in set(dic_cityPopulation) & set(dic_cityArea)}

# flatTypes = [
#     'Свободная планировка',
#     'Комнаты',
#     'Студия',
#     ]

# regions = [
#     'Крым',
#     'Краснодарский',
#     'Севастополь',
# ]

# cities = [
#     'Новороссийск',
#     'Анапа',
#     'Сочи',
#     'Симферополь',
#     'Генелджик',
#     'Ялта',
#     'Гагаринский район',
#     'Ленинский район',
#     'Евпатория',
#     'Феодосия',
#     'Алушта',
#     'Керчь',
#     'Нахимовский район',
#     'Симферопольский район',
#     'Туапсе',
#     'Саки',
#     'Балаклавский район',
#     'Сакский район',
#     'Туапсинский район',
#     'Судак'
# ]

# materialTypes = [
#     'Газобетонный блок',
#     'Блок',
#     'Кирпич',
#     'Пенобетонный блок',
#     'Газовый силикатный блок',
#     'Монолит',
#     'Монолитный кирпич',
#     'Старый',
#     'Панель',
#     'Сталинка',
#     'Неизвестно',
#     'Каркас',
#     'Дерево',
# ]


# функция для расчета стоимости квартиры
def get_estimated_price(
    newBuilding,
    floorNumber,
    fromDeveloper,
    isApartments,
    isAuction,
    kitchenArea,
    livingArea,
    roomsCount,
    totalArea,
    floorsCount,
    isComplete,
    passengerLiftsCount,
    cargoLiftsCount,
    hasBalcony,
    isBasement,
    isFirstFloor,
    isLastFloor,
    flatType,
    region,
    city,
    materialType 
    ):

    # определяем номер столбца по значению поля
    try:
        flatType_index = data_columns.index(flatType.lower())
    except:
        flatType_index = -1

    try:
        region_index = data_columns.index(region.lower())
    except:
        region_index = -1

    try:
        city_index = data_columns.index(city.lower())
    except:
        city_index = -1

    try:
        materialType_index = data_columns.index(materialType.lower())
    except:
        materialType_index = -1

    # вычисляем значение признаков
    cityPopulation = dic_cityPopulation.get(city)
    cityArea = dic_cityArea.get(city)
    populationDensity = dic_cityPopulation.get(city) / dic_cityArea.get(city)
    areaPerRoom = totalArea / roomsCount

    # заполняем значения переменных
    x = np.zeros(len(data_columns))
    x[0] = newBuilding
    x[1] = floorNumber
    x[2] = fromDeveloper
    x[3] = isApartments
    x[4] = isAuction
    x[5] = kitchenArea
    x[6] = livingArea
    x[7] = roomsCount
    x[8] = totalArea
    x[9] = floorsCount
    x[10] = isComplete
    x[11] = passengerLiftsCount
    x[12] = cargoLiftsCount
    x[13] = hasBalcony
    x[14] = isBasement
    x[15] = isFirstFloor
    x[16] = isLastFloor
    x[17] = cityPopulation
    x[18] = cityArea
    x[19] = populationDensity
    x[20] = areaPerRoom
    if flatType_index >= 0:
        x[flatType_index] = 1
    if region_index >= 0:
        x[region_index] = 1
    if city_index >= 0:
        x[city_index] = 1
    if materialType_index >= 0:
        x[materialType_index] = 1

    return round(model.predict([x])[0],2)


# функция для загрузки названий колонок
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global data_columns
    global flatTypes
    global regions
    global cities
    global materialTypes

    with open("./artifacts/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        flatTypes = data_columns[21:24]
        regions = data_columns[24:27]
        cities= data_columns[27:47]
        materialTypes = data_columns[47:60]

    global model
    if model is None:
        with open('./artifacts/best_cb_model.pkl', 'rb') as f:
            model = pickle.load(f)
    print("loading saved artifacts...done")    


def get_flatType_names():
    return flatTypes

def get_region_names():
    return regions

def get_city_names():
    return cities

def get_materialType_names():
    return materialTypes


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_flatType_names())
    print(get_materialType_names())
    print(get_region_names())
    print(get_city_names())
    print(get_estimated_price(0,12,1,0,0,8,120,2,60,18,1,1,1,1,0,0,0,'flattype_rooms','region_crimea','city_alushta','materialtype_monolith'))