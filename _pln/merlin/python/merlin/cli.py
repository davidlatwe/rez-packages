
import sys
from ozark import cli as ozark_cli
from ozark import util as ozark_util
from . import util


def party(opt):
    if opt.init:
        util.init()
    else:
        if opt.list:
            ozark_util.ls(location=opt.at)
        else:
            util.build(location=opt.at)


def main(argv=None):
    argv = argv or sys.argv

    parsers = ozark_cli.make_parsers()
    parser = parsers["main"]
    parser_party = parsers["party"]

    parser_party.set_defaults(run=party)

    # Parsing args
    opt = parser.parse_args(argv[1:])
    opt.run(opt)
