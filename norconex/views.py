from flask import Blueprint
import json


crawls = Blueprint('crawls', __name__)

@crawls.route('/')
def crawl_list():
    crawls = {'crawls': {
        'medsites': {
            'config': 'config/medsites.xml',
            'vars': 'medsites.properties',
            'status': 'IDLE'
        },
        'mplusmonitor': {
            'config': 'config/mplusmonitor.xml',
            'vars': 'mplusmon.properties',
            'status': 'IDLE'
        },
    }}
    return json.dumps(crawls)

