import logging
import time

logger = logging.getLogger(__name__)

class WordSmith(object):

    def __init__(self, best_word, worst_word):
        '''Initialize wordsmith's best and worst word'''
        logger.debug("My favorite word: %s", best_word)
        time.sleep(1)
        logger.debug("My worst word: %s", worst_word)
        time.sleep(1)
        self.best_word = best_word
        self.worst_word = worst_word

    def sentence_with_best_word(self):
        logger.warning("Be careful... words can hurt, especially '%s'",
                self.best_word)
        time.sleep(1)
        return "'%s' is my best word" % self.best_word

    def sentence_with_worst_word(self):
        logger.critical("Not sure I can take hearing '%s'", self.worst_word)
        time.sleep(1)
        return "I hate '%s'" % self.worst_word
