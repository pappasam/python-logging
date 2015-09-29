import logging.config
from calculator import add_5, subtract_10
from lexicon import WordSmith
import yaml
import os

'''
See the following link for a good resource on YAML configuration
http://stackoverflow.com/questions/15693529/how-to-specify-in-yaml-to-always-create-log-file-in-the-projects-folder-using-d

Run this module (requires pyaml)

Sends log messages INFO or above to a file called info_logs.log
Prints all logs DEBUG and above to standard output

Currently relies entirely on the root logger, through handlers
'''
logger = logging.getLogger(__name__)

def logmaker_info():
    path = os.path.dirname(os.path.abspath(__file__))
    path_log = os.path.join(path, 'logs', 'info_logs.log')
    return logging.FileHandler(path_log)

def main():
    PATH_PYTHON = os.path.dirname(os.path.abspath(__name__))
    PATH_YAML = os.path.join(PATH_PYTHON, 'yaml')
    PATH_LOG_CONFIG = os.path.join(PATH_YAML, 'logger.yaml')

    with open(PATH_LOG_CONFIG, 'rt') as f:
        logging_config = yaml.load(f.read())
    logging.config.dictConfig(logging_config)

    kanye = WordSmith("excellence", "nothing")

    seventeen = add_5(12)
    logger.debug("%i had better be 17", seventeen)

    one = subtract_10(11)
    logger.debug("%i had better be 1", one)

    nice_sentence = kanye.sentence_with_best_word()
    bad_sentence = kanye.sentence_with_worst_word()

    logger.info("nice sentence: %s", nice_sentence)
    logger.info("bad sentence: %s", bad_sentence)

if __name__ == '__main__':
    main()
