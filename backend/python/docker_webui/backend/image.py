"""
This module is responsible for the operations of the Docker images.
List them, delete them, get infrmation from it or other options.
"""

import docker
import json

from flask import request


def get_images() -> list:
    """
    Gives back a set of images to be shown on the user interface.

    @return: The list of images e filtered
    @type return: str
    """
    result = []
    client = docker.from_env()
    name = request.args.get('name', None)
    all = request.args.get('all', 'no')
    for image in client.images.list(all=(all == 'yes'), name=name):
        result.append(image.attrs)
    return json.dumps({'containers': result})
