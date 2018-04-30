'''
Main file for API
'''
from os import environ
from api.factory import create_app

APP = create_app()

if __name__ == "__main__":
    '''
    API entry point with configurable port
    '''
    PORT = int(environ.get("PORT", 5000))
    APP.run(host='0.0.0.0', port=PORT)
