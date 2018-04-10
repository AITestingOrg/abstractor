'''
Flask endpoint controller for abstractions
'''
from flask import request, Blueprint, jsonify
from api.utils.exceptions import InvalidUsage
from api.tasks.abstraction_tasks import get_abstraction, get_concrete_example, get_abstractions
from api.utils import logger

abstraction_bp = Blueprint('abstraction', __name__, url_prefix='/abstraction')

logger = logger.create_logger(__name__)

@abstraction_bp.route('/supported', methods=('GET',))
def get_abstractions_supported():
    '''
    Returns supported abstractions
    '''
    logger.info('REQUEST: /abstractions')
    return jsonify(get_abstractions())


@abstraction_bp.route('/concrete/example/<abstraction>', methods=('GET',))
def get_example(abstraction):
    '''
    Returns an example of the abstraction given, if the abstraction
    is invalid it will return a 400 error
    '''
    logger.info('REQUEST: /concrete/example/{}'.format(abstraction))
    concrete_example = get_concrete_example(abstraction)
    if concrete_example is not None:
        return jsonify({ 'example': concrete_example, 'abstraction': abstraction })
    else:
        raise InvalidUsage('The abstraction {} does not exist.'.format(abstraction.upper()), status_code=400)


@abstraction_bp.route('/', methods=('POST',))
def get_example_abstraction():
    '''
    Returns the abstraction for a given example, will return 201 if found abstraction
    else it will return 200
    '''
    logger.info('REQUEST: /')
    body = request.get_json()
    abstraction = get_abstraction(body)
    if abstraction is not None:
        return jsonify({ 'abstraction': abstraction, 'target': body['value'] }), 201
    else:
        raise InvalidUsage('Could not find an abstraction for: {}.'.format(body['value']), status_code=200)