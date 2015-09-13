# pyip-reflector

A miniature IP reflector built in Python using [Flask](http://flask.pocoo.org).

## Usage

pyip-reflector pirmarily exposes a WSGI application called `app` in the
pyip_reflector module. Plug this in to your favorite WSGI framework (gunicorn,
uwsgi, etc). You can also run the reflector using the built-in Flask server:

    python pyip_reflector/reflector.py --address 0.0.0.0 --port 10704

pyip_reflector will "reflect" the IP address of a connecting client back to it.
This means that the address returned to clients may vary depending on hosts
that are multi-homed and support IPv6. If you want to support e.g. IPv6, simply
teach the server forwarding requests to this application to bind to an IPv6
address. For example, using the built-in server:

    python pyip_reflector/reflector.py --address :: --port 10704

