import logging
from api import app
from api.helpers import force_data_update


logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

@app.cli.command()
def update_data():
    """Update blood levels data."""
    logger.info('Updating data...')
    _, status = force_data_update()
    if status == 200:
        pass
        logger.info('Update done successfuly!')
    else:
        pass
        logger.info('Update failed!')