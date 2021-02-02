#!/usr/bin/env python3

import os
import cherrypy

PATH = os.path.abspath(os.path.dirname(__file__)) + "/html"
class Root(object): pass

cherrypy.tree.mount(Root(), '/', config={
        '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
                'tools.staticdir.index': 'index.html',
            },
    })

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.server.socket_port = 8000
cherrypy.engine.start()
cherrypy.engine.block()

