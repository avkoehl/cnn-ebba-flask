from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import numpy as np

app = Flask(__name__)
CORS(app)

def load_files():
    i = open("files.csv", "r")
    files = i.read().rstrip().split(",")
    return files

def zip_sort(files, dists):
    idxs = dists.argsort()
    files = np.array(files)
    f = files[idxs]
    d = dists[idxs]
    return f,d

alldistances = np.load("distances.npy")
files = load_files()
inds = {}
for i,f in enumerate(files):
    inds[f] = i

@app.route('/')
def index():
    return "Ebba CNN distances"

@app.route('/distance', methods=['GET'])
def get_distances():
    img = request.args.get('img', type = str)
    idx = inds[img]
    dists = alldistances[idx]
    sorted_files,sorted_dists = zip_sort(files,dists)

    results = []
    for i,f in enumerate(sorted_files):
        res = f + " " + str(sorted_dists[i])
        results.append(res)

    return ",".join(results)

if __name__ == '__main__':
    app.run(debug=True)

