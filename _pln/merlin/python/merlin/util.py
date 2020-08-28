
from ozark import util as ozark_util


def init():
    ozark_util.init()


def build(location=None):
    ozark_util.build(location)

    # write project config into avalon db
