#!/usr/bin/env python3

import sys
import os
import argparse

ROOT = HERE = os.path.abspath(os.path.dirname(__file__))
READIES = os.path.join(ROOT, "deps/readies")
sys.path.insert(0, READIES)
import paella

#----------------------------------------------------------------------------------------------

class RedisTimeSeriesSetup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)

    def common_first(self):
        self.install("git jq curl unzip")
        self.run("%s/bin/enable-utf8" % READIES, sudo=self.os != 'macos')
        slef.install("java maven")

    def debian_compat(self):
        pass

    def redhat_compat(self):
        self.install("redhat-lsb-core")
        self.run("%s/bin/getepel" % READIES, sudo=True)

    def archlinux(self):
        pass

    def fedora(self):
        pass

    def macos(self):
        self.install_gnu_utils()

    def common_last(self):
        self.run("{PYTHON} {READIES}/bin/getdocker --compose".format(PYTHON=self.python, READIES=READIES))
        self.pip_install("-r {ROOT}/tests/flow/requirements.txt".format(ROOT=ROOT))
        self.pip_install("gevent")

    def linux_last(self):
        pass

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RedisTimeSeriesSetup(nop = args.nop).setup()
