'''
Main file for API
'''
from api.utils import logger
from os import environ
from api.factory import create_app
from pyeureka import SimpleEurekaServiceWrapper

APP = create_app()

if __name__ == "__main__":
    '''
    API entry point with configurable port
    '''
    PORT = int(environ.get("PORT", 8080))
    APP.run(host='0.0.0.0', port=PORT)

    app = 'spacyservice'
    eureka_url = 'http://localhost:8761'
    heartbeat = 5.0
    instance = {
        'ipAddr': '127.0.0.1',
        'app': app,
        'instanceId': 'spacyservice'
    }

    logger.info("Eureka address: {}".format(eureka_url))
    logger.info("Service definition")
    logger.info(instance)
    service_wrapper = SimpleEurekaServiceWrapper(eureka_url, instance, heartbeat)

    logger.info("Registering service")
    service_wrapper.run()

    logger.info("Stopping service")
    service_wrapper.stop()
