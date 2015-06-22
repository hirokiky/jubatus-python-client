# This file is auto-generated from burst.idl(0.6.4-96-g66ed74d) with jenerator version 0.5.1-457-g49229fa/master
# *** DO NOT EDIT ***


import sys
import msgpack
import jubatus.common
from jubatus.common.types import *


class KeywordWithParams:
    TYPE = TTuple(TString(), TFloat(), TFloat())

    def __init__(self, keyword, scaling_param, gamma):
        self.keyword = keyword
        self.scaling_param = scaling_param
        self.gamma = gamma

    def to_msgpack(self):
        t = (self.keyword, self.scaling_param, self.gamma)
        return self.__class__.TYPE.to_msgpack(t)

    @classmethod
    def from_msgpack(cls, arg):
        val = cls.TYPE.from_msgpack(arg)
        return KeywordWithParams(*val)

    def __repr__(self):
        gen = jubatus.common.MessageStringGenerator()
        gen.open("keyword_with_params")
        gen.add("keyword", self.keyword)
        gen.add("scaling_param", self.scaling_param)
        gen.add("gamma", self.gamma)
        gen.close()
        return gen.to_string()


class Batch:
    TYPE = TTuple(TInt(True, 4), TInt(True, 4), TFloat())

    def __init__(self, all_data_count, relevant_data_count, burst_weight):
        self.all_data_count = all_data_count
        self.relevant_data_count = relevant_data_count
        self.burst_weight = burst_weight

    def to_msgpack(self):
        t = (self.all_data_count, self.relevant_data_count, self.burst_weight)
        return self.__class__.TYPE.to_msgpack(t)

    @classmethod
    def from_msgpack(cls, arg):
        val = cls.TYPE.from_msgpack(arg)
        return Batch(*val)

    def __repr__(self):
        gen = jubatus.common.MessageStringGenerator()
        gen.open("batch")
        gen.add("all_data_count", self.all_data_count)
        gen.add("relevant_data_count", self.relevant_data_count)
        gen.add("burst_weight", self.burst_weight)
        gen.close()
        return gen.to_string()


class Window:
    TYPE = TTuple(TFloat(), TList(TUserDef(Batch)))

    def __init__(self, start_pos, batches):
        self.start_pos = start_pos
        self.batches = batches

    def to_msgpack(self):
        t = (self.start_pos, self.batches)
        return self.__class__.TYPE.to_msgpack(t)

    @classmethod
    def from_msgpack(cls, arg):
        val = cls.TYPE.from_msgpack(arg)
        return Window(*val)

    def __repr__(self):
        gen = jubatus.common.MessageStringGenerator()
        gen.open("window")
        gen.add("start_pos", self.start_pos)
        gen.add("batches", self.batches)
        gen.close()
        return gen.to_string()


class Document:
    TYPE = TTuple(TFloat(), TString())

    def __init__(self, pos, text):
        self.pos = pos
        self.text = text

    def to_msgpack(self):
        t = (self.pos, self.text)
        return self.__class__.TYPE.to_msgpack(t)

    @classmethod
    def from_msgpack(cls, arg):
        val = cls.TYPE.from_msgpack(arg)
        return Document(*val)

    def __repr__(self):
        gen = jubatus.common.MessageStringGenerator()
        gen.open("document")
        gen.add("pos", self.pos)
        gen.add("text", self.text)
        gen.close()
        return gen.to_string()
