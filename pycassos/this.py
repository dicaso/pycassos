# -*- coding: utf-8 -*-
"""this easter egg module

generates the dicaso universe of packages
"""

import os, pydot as dot
#assets = os.path.join(os.path.dirname(__file__),'pycassos/static/assets/logos')
assets = '/tmp'
dicaso = dot.Dot('dicaso universe',graph_type='digraph')

# create nodes
rootnode = dot.Node('root', label='', shape="box", image=os.path.join(assets,'dicaso-text-logo.png'))
dicaso.add_node(rootnode)
pycassos = dot.Node('pycassos', label='', shape="box", image=os.path.join(assets,'pycassos-text-logo.png'))
dicaso.add_node(pycassos)
hotendms = dot.Node('hotend', label='', shape="box", image=os.path.join(assets,'hotend_logo.png'))
dicaso.add_node(hotendms)
leopard = dot.Node('leopard', label='', shape="box", image=os.path.join(assets,'leopard_logo.png'))
dicaso.add_node(leopard)
genairics = dot.Node('genairics', label='', shape="box", image=os.path.join(assets,'gax_logo.png'))
dicaso.add_node(genairics)
bidali = dot.Node('bidali', label='', shape="box", image=os.path.join(assets,'bidali_logo.png'))
dicaso.add_node(bidali)
pyni = dot.Node('pyni', label='', shape="box", image=os.path.join(assets,'ni_logo.png'))
dicaso.add_node(pyni)

# create edges: node A depends on node B
dicaso.add_edge(dot.Edge(rootnode,pycassos))
dicaso.add_edge(dot.Edge(rootnode,hotendms))
dicaso.add_edge(dot.Edge(pycassos,hotendms))
for e in (leopard, genairics, bidali, pyni):
    dicaso.add_edge(dot.Edge(pycassos,e))
dicaso.add_edge(dot.Edge(pyni,bidali))
dicaso.add_edge(dot.Edge(bidali,leopard))
dicaso.add_edge(dot.Edge(genairics,leopard))

dicaso.write_png('/home/christophe/Desktop/dicaso-uni.png')
