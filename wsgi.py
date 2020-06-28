from os import environ
from _4TPyModel import app

if __name__ == '__main__':
    app.run()

    # HOST = environ.get('SERVER_HOST', 'localhost')
    # try:
    #    PORT = int(environ.get('SERVER_PORT', '5555'))
    # except ValueError:
    # PORT = 5000
    # app.run(HOST, PORT)