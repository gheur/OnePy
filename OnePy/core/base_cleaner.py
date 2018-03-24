

from OnePy.environment import Environment
from OnePy.event import EVENT, Event

class CleanerBase(object):
    env = None
    gvar = None

    """Docstring for RiskManagerBase. """

    def __init__(self,name):
        self.env.cleaners.update({name:self})

    def run(self):
        pass
        