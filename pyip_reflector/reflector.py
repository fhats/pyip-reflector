#!/usr/bin/env python
from optparse import OptionParser

from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
def ip(path):
    ip_addr = request.remote_addr
    return ip_addr


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-a', '--address', default="0.0.0.0", help="The address to bind to. Defaults to 0.0.0.0.")
    parser.add_option('-p', '--port', type=int, default=10704, help="The port to listen on. Defaults to 10704.")
    options, args = parser.parse_args()

    app.run(host=options.address, port=options.port, debug=False)
