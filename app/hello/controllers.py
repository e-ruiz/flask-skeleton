# -*- coding: utf-8 -*-

from flask import Blueprint, Response, request, json
from . models import Hello
import settings
import json

hello = Blueprint('hello', __name__, template_folder='templates')


# GET /hello
@hello.route('', methods=['GET'])
def get_hello():
    name = request.args.get('name') if request.args.get('name') else ''
    hello = Hello()
    msg = hello.sayHelloTo(name)

    return Response(json.dumps({"msg": msg}) , mimetype='application/json', status=200)
    # return jsonify({"msg": msg})

