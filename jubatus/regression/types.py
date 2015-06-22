# This file is auto-generated from regression.idl(0.6.4-33-gcc8d7ca) with jenerator version 0.5.1-457-g49229fa/master
# *** DO NOT EDIT ***


import sys
import msgpack
import jubatus.common
from jubatus.common.types import *


class ScoredDatum:
    TYPE = TTuple(TFloat(), TDatum())

    def __init__(self, score, data):
        self.score = score
        self.data = data

    def to_msgpack(self):
        t = (self.score, self.data)
        return self.__class__.TYPE.to_msgpack(t)

    @classmethod
    def from_msgpack(cls, arg):
        val = cls.TYPE.from_msgpack(arg)
        return ScoredDatum(*val)

    def __repr__(self):
        gen = jubatus.common.MessageStringGenerator()
        gen.open("scored_datum")
        gen.add("score", self.score)
        gen.add("data", self.data)
        gen.close()
        return gen.to_string()
