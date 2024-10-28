import logging
from anotherfile import do_something

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='teste_log.log', level=logging.INFO)
    logger.info('Started')
    do_something()
    logger.info('Finish')

if __name__ == '__main__':
    main()
