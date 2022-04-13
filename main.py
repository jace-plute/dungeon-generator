from flask import Flask, request
from map import Map
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/generateMap')
def getMap():
    # Expect the user to pass in integers for the width and height of the dungeon, the start position, and the end position.
    width = int(request.args.get('width'))
    height = int(request.args.get('height'))
    startX = int(request.args.get('startX'))
    startY = int(request.args.get('startY'))
    endX = int(request.args.get('endX'))
    endY = int(request.args.get('endY'))

    # Generate a map with the passed in parameters.
    myMap = Map(width, height, startX, startY, endX, endY)
    myMap.generateMap()

    # Dump the returned map into a json structure, which the endpoint will return.
    jsonReturn = json.dumps(myMap.map.tolist())

    # The caller will be responsible for taking this json and manipulating it to create a UI or graphical representation.
    return jsonReturn
