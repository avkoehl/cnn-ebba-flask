from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import numpy as np
from functions import *

app = Flask(__name__)
CORS(app)


#=================== LOAD DATA ======================#
alldistances = np.load("./data/distances.npy")
metadistances = np.load("./data/meta-distances.npy")
files = load_files("./data/files.csv")

inds = {}
for i,f in enumerate(files):
    inds[f] = i



#====================== APP =========================#
@app.route('/')
def index():
    return "Ebba CNN distances"

@app.route('/distance', methods=['GET'])
def get_distances():
    img = request.args.get('img', type = str)
    if inds[img]:
        return distance(alldistances, inds, files, img)
    else:
        return "error, impression not found in the distance matrix"

@app.route('/metadistance', methods=['GET'])
def get_metadistances():
    cid = request.args.get('cid', type = int)
    if cid >= 0 and cid < metadistances.shape[0]:
        return metadistance(metadistances,cid)
    else:
        return "error cluster id not found"

if __name__ == '__main__':
    app.run(port=5555, debug=True)

