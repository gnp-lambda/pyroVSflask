#!/usr/bin/python
from __future__ import unicode_literals, print_function, absolute_import

from flask import Flask, request, Response

from common import generate_payload

app = Flask('pyro_vs_http')


@app.route('/get_value/<int:size>', methods=['GET', 'POST'])
def get_value(size):
    request.get_data()  # Forzar la lectura del payload
    return Response(generate_payload(size), mimetype='text')


if __name__ == '__main__':
    app.run('0.0.0.0', '8000')
