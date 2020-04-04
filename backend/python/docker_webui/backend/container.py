"""
This module is responsible for the operations of the Docker containers.
List them, run them get the logs from it or other options.
"""

import docker
import json

from flask import request


def get_containers() -> list:
    """
    Gives back a set of containers to be shown on the user interface.

    @return: The list of containers e filtered
    @type return: str
    """
    result = []
    client = docker.from_env()
    name = request.args.get('name', '')
    all = request.args.get('all', 'no')
    type = request.args.get('type', '')
    filters = {}
    if (name != ""):
        filters['name'] = name
    if (type != ""):
        filters['ancestor'] = type
    for container in client.containers.list(all=(all == 'yes'), filters=filters):
        result.append(container.attrs)
    return json.dumps({'containers': result})
