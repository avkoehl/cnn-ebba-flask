import numpy as np

def load_files(filepath):
    i = open(filepath, "r")
    files = i.read().rstrip().split(",")
    return files

def zip_sort(files, dists):
    idxs = dists.argsort()
    files = np.array(files)
    f = files[idxs]
    d = dists[idxs]
    return f,d

def distance(alldistances, inds, files, img):
    idx = inds[img]
    dists = alldistances[idx]
    sorted_files,sorted_dists = zip_sort(files,dists)

    results = []
    for i,f in enumerate(sorted_files):
        res = f + " " + str(sorted_dists[i])
        results.append(res)

    return ",".join(results)

def metadistance(metadistances, cid):
    dists = metadistances[cid]
    sorted_cids,sorted_dists = zip_sort(range(metadistances.shape[0]),dists)

    results = []
    for i,c in enumerate(sorted_cids):
        res = str(c) + " " + str(sorted_dists[i])
        results.append(res)

    return ",".join(results)
