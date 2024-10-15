import qubalab
from qubalab.qupath import qupath_gateway
import numpy as np
import pandas as pd
import umap

token = None
port = 25333
gateway = qupath_gateway.create_gateway(auth_token=token, port=port)

detections = gateway.getDetectionObjects()
measurement_names = detections[0].getMeasurements().keySet()
measurement_names = [x for x in measurement_names if x.startswith("Cell") and x.endswith("Mean")]

df = pd.DataFrame(columns = measurement_names)
for det in detections:
    row = {name: det.getMeasurements().get(name) for name in measurement_names}
    df = df._append(row, ignore_index=True)

normalized_df = (df - df.mean()) / df.std()

embedding = umap.UMAP().fit_transform(normalized_df)


for i in range(embedding.shape[0]):
    detections[i].getMeasurementList().put("UMAP1", float(embedding[i][0]))
    detections[i].getMeasurementList().put("UMAP2", float(embedding[i][1]))

import leidenalg as la
import igraph
from sklearn.neighbors import kneighbors_graph

A = kneighbors_graph(normalized_df, 50)
g = igraph.Graph.Adjacency((A > 0))

partition = la.find_partition(g, la.ModularityVertexPartition)

for i in range(embedding.shape[0]):
    detections[i].setClassification(f"Cluster {partition.membership[i]}")
