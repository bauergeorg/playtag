#! /usr/bin/env python
from playtag.lib.userconfig import UserConfig
from playtag.lib.userconfig import basic_startup
from playtag.svf import runsvf

class SvfFileError(Exception):
    """Svf error"""

class SvfDefaults(object):
    SVF = None

#config = UserConfig()
config = basic_startup()

if config.SHOW_CONFIG:
    print(config.dump())

config.add_defaults(SvfDefaults)

config.SVF = 'simple_example.svf'

if not config.SVF:
    print('Expected SVF=<fname>')
    raise SvfFileError("Please add a filename!")

runsvf(config.SVF, config.driver)
