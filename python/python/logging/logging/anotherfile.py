import logging
from datetime import datetime
logger = logging.getLogger(__name__)

def do_something():
    logger.info('Doing something')
    print("I'm already did")
    count = 0
    while count < 10:
        count += 1
        if count == 5:
            logger.warning(f"Watch out count value is going be too high")

        elif count == 9:
            logger.error(f"WTF is too high, i'm gonna finish this.")
            break

        logger.info(f"Count value: {count} at {datetime.now().strftime('%d-%m-%Y, %H:%M:%S')}")