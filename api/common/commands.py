import logging
from flask import Blueprint
from api.common.helpers import force_data_update

update_data_bp = Blueprint('data', __name__)

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

@update_data_bp.cli.command('update')
def update_data():
    """Update blood levels data."""
    logger.info('Updating data...')
    _, status = force_data_update()
    if status == 200:
        logger.info('Update done successfuly!')
    else:
        logger.info('Update failed!')
