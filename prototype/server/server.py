from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_flattype_names', methods=['GET'])
def get_flatType_names():
    response = jsonify({
        'flatTypes': util.get_flatType_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_region_names', methods=['GET'])
def get_region_names():
    response = jsonify({
        'regions': util.get_region_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_city_names', methods=['GET'])
def get_city_names():
    response = jsonify({
        'cities': util.get_city_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_materialtype_names', methods=['GET'])
def get_materialType_names():
    response = jsonify({
        'materialTypes': util.get_materialType_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    newBuilding = int(request.form['newBuilding'])
    floorNumber = int(request.form['floorNumber'])
    fromDeveloper = int(request.form['fromDeveloper'])
    isApartments = int(request.form['isApartments'])
    isAuction = int(request.form['isAuction'])
    kitchenArea = int(request.form['kitchenArea'])
    livingArea = int(request.form['livingArea'])
    roomsCount = int(request.form['roomsCount'])
    totalArea = int(request.form['totalArea'])
    floorsCount = int(request.form['floorsCount'])
    isComplete = int(request.form['isComplete'])
    passengerLiftsCount = int(request.form['passengerLiftsCount'])
    cargoLiftsCount = int(request.form['cargoLiftsCount'])
    hasBalcony = int(request.form['hasBalcony'])
    isBasement = int(request.form['isBasement'])
    isFirstFloor = int(request.form['isFirstFloor'])
    isLastFloor = int(request.form['isLastFloor'])
    flatType = request.form['flatType']
    region = request.form['region']
    city = request.form['city']
    materialType = request.form['materialType']

    response = jsonify({
        'estimated_price': util.get_estimated_price(
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
            )
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    print(util.get_flatType_names())
    app.run()

