# -*- coding: utf-8 -*-
"""pycassos main module

Initializes flask app, brings all routes together.
"""

from flask import Flask, request
from flask_restful import Resource, Api
import json

# serving static files from root to directly serve ng frontend
app = Flask('pycassos',static_url_path='')
api = Api(app)

# Frontend
#@app.route('/', defaults={'path': ''})
#@app.route('/static/<path:path>')
@app.route('/', defaults={'path': ''})
@app.errorhandler(404)
def root(path):
    return app.send_static_file('index.html')

#@app.errorhandler(404)
#def page_not_found(e):
#    return render_template('404.html'), 404

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

# Lock for server heavy calculations
# necessary when running flask server directly
# might not be necessary when deploying through nginx
# TODO check
from threading import Lock
lock = Lock()

@app.route('/rest/dosage/<gene>')
def dosage(gene):
    with lock:
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

api.add_resource(DosageSensitivity, '/rest/restdosage') # Route_1
