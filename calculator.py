import logging

logger = logging.getLogger(__name__)

def add_5(x):
    '''Add 5 to number x'''
    if type(x) not in (int, float):
        msg = "{} neither int nor float".format(x)
        logger.error(msg)
        raise ValueError(msg)
    logger.info("Adding 5 to {}".format(x))
    return int(x + 5)

def subtract_10(x):
    '''Subtract 10 from number x'''
    if type(x) not in (int, float):
        msg = "{} neither int nor float".format(x)
        logger.error(msg)
        raise ValueError(msg)
    logger.info("Subtracting 10 from {}".format(x))
    return int(x - 10)
