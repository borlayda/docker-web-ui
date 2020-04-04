"""
The REST interface definition of the WebUI backend service. It is based on a
YAML file which has the endpoint definitions, and this module only initialize
the servica application and adds the route records.
"""
import yaml
import os
import sys

from importlib import import_module
from flask import Flask


app = Flask("DockerWebUI")
app.logger.setLevel(20) # INFO level logging
INTERFACE_FILE = os.environ.get(
    "BACKEND_INTERFACE_FILE",
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'web.yml'))


def generate_interface():
    """
    This function makes the URL bindings of the backend service based on the
    YAML file found in the BACKEND_INTERFACE_FILE environment variable, or in
    the web.yml file next to this one. The yaml file contains the end uri,
    parameter, call method, http method and request/response format information,
    which will be used in the decorated function.
    """
    global app
    interface = yaml.safe_load(open(INTERFACE_FILE, 'r').read())
    endpoints = interface['endpoints']
    for itype in endpoints.keys():
        base_uri = "/" + itype
        for endpoint in endpoints[itype]:
            uri = base_uri + endpoint['uri']
            app.logger.info("Trying to register '{uri}' with method '{methods}' and function '{function}'".format(
                uri=uri, methods=endpoint['methods'], function=endpoint['function']))
            try:
                module_data = endpoint['function'].split('.')
                method_name = module_data[-1]
                module = import_module(".".join(module_data[:-1]))
                call_method = getattr(module, method_name)
                decorated_func = app.route(uri, methods=endpoint['methods'])
                decorated_func(call_method)
            except Exception as err:
                app.logger.error("Couldn't bind the '{uri}'".format(uri=uri))
                app.logger.error(str(err))

generate_interface()
