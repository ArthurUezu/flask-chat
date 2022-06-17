from distutils.log import debug
from app import app
from app import io
if(__name__ == '__main__'):
    io.run(app, debug=True)