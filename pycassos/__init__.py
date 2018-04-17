# -*- coding: utf-8 -*-
"""pycassos main module

Initializes flask app, brings all routes together.
"""

from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask('pycassos')
api = Api(app)

# Frontend
@app.route('/')
@app.route('/static/song/')
def root():
    return app.send_static_file('song/index.html')

# Backend
# TODO move to visualization module
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ioff()
import mpld3
from mpld3 import plugins

# Setting up matplotlib styles using BMH
#s = json.load(open("./static/bmh_matplotlibrc.json"))
#matplotlib.rcParams.update(s)

#mpld3 hack
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        import numpy as np
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.int64):
            return int(obj)
        return json.JSONEncoder.default(self, obj)
from mpld3 import _display
_display.NumpyEncoder = NumpyEncoder
#TODO push to mpld3 repo

@app.route('/dosage/<gene>')
def dosage(gene):
    from bidali.LSD.dealer.external import cohorts
    import bidali.visualizations as biv
    nrc = cohorts.get_NRC()
    #TODO full nrc preparation in bidali.LSD
    nrc.metadata['high_risk'] = nrc.metadata.nrc_inss.apply(lambda x: '1' if x in ('st3','st4') else '0')
    nrc.metadata['mycn_status'] = nrc.metadata.nrc_mycna.apply(lambda x: '1' if x == 'yes' else '0')
    nrc.geneCNA=nrc.geneCNVannotation
    fig, ax = plt.subplots()
    biv.dosageViolin(gene,dataset=nrc,ax=ax)
    return mpld3.fig_to_html(fig)
    
class DosageSensitivity(Resource):
    def get(self):
        #return {'genes': [{'id':1, 'name':'BRIP1'},{'id':2, 'name':'BRCA1'}]}
        fig, ax = plt.subplots()
        ax.scatter(range(10),range(10))
        return mpld3.fig_to_html(fig)

api.add_resource(DosageSensitivity, '/restdosage') # Route_1
