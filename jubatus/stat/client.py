# This file is auto-generated from stat.idl(0.6.4-33-gcc8d7ca) with jenerator version 0.5.1-457-g49229fa/master
# *** DO NOT EDIT ***


import msgpackrpc
import jubatus.common
from .types import *
from jubatus.common.types import *


class Stat(jubatus.common.ClientBase):

    def __init__(self, host, port, name, timeout=10):
        super(Stat, self).__init__(host, port, name, timeout)

    def push(self, key, value):
        return self.jubatus_client.call("push", [key, value], TBool(), [TString(),
                                                                        TFloat()])

    def sum(self, key):
        return self.jubatus_client.call("sum", [key], TFloat(), [TString()])

    def stddev(self, key):
        return self.jubatus_client.call("stddev", [key], TFloat(), [TString()])

    def max(self, key):
        return self.jubatus_client.call("max", [key], TFloat(), [TString()])

    def min(self, key):
        return self.jubatus_client.call("min", [key], TFloat(), [TString()])

    def entropy(self, key):
        return self.jubatus_client.call("entropy", [key], TFloat(), [TString()])

    def moment(self, key, degree, center):
        return self.jubatus_client.call("moment", [key, degree, center], TFloat(),
                                        [TString(), TInt(True, 4), TFloat()])

    def clear(self):
        return self.jubatus_client.call("clear", [], TBool(), [])
