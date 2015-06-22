# This file is auto-generated from graph.idl(0.6.4-33-gcc8d7ca) with jenerator version 0.5.1-457-g49229fa/master
# *** DO NOT EDIT ***


import sys
import msgpack
import jubatus.common
from jubatus.common.types import *


class Node:
    TYPE = TTuple(TMap(TString(), TString()), TList(TInt(False, 8)), TList(TInt(
        False, 8)))

    def __init__(self, property, in_edges, out_edges):
        self.property = property
        self.in_edges = in_edges
        self.out_edges = out_edges

    def to_msgpack(self):
        t = (self.property, self.in_edges, self.out_edges)
        return self.__class__.TYPE.to_msgpack(t)

    @classmethod
    def from_msgpack(cls, arg):
        val = cls.TYPE.from_msgpack(arg)
        return Node(*val)

    def __repr__(self):
        gen = jubatus.common.MessageStringGenerator()
        gen.open("node")
        gen.add("property", self.property)
        gen.add("in_edges", self.in_edges)
        gen.add("out_edges", self.out_edges)
        gen.close()
        return gen.to_string()


class Query:
    TYPE = TTuple(TString(), TString())

    def __init__(self, from_id, to_id):
        self.from_id = from_id
        self.to_id = to_id

    def to_msgpack(self):
        t = (self.from_id, self.to_id)
        return self.__class__.TYPE.to_msgpack(t)

    @classmethod
    def from_msgpack(cls, arg):
        val = cls.TYPE.from_msgpack(arg)
        return Query(*val)

    def __repr__(self):
        gen = jubatus.common.MessageStringGenerator()
        gen.open("query")
        gen.add("from_id", self.from_id)
        gen.add("to_id", self.to_id)
        gen.close()
        return gen.to_string()


class PresetQuery:
    TYPE = TTuple(TList(TUserDef(Query)), TList(TUserDef(Query)))

    def __init__(self, edge_query, node_query):
        self.edge_query = edge_query
        self.node_query = node_query

    def to_msgpack(self):
        t = (self.edge_query, self.node_query)
        return self.__class__.TYPE.to_msgpack(t)

    @classmethod
    def from_msgpack(cls, arg):
        val = cls.TYPE.from_msgpack(arg)
        return PresetQuery(*val)

    def __repr__(self):
        gen = jubatus.common.MessageStringGenerator()
        gen.open("preset_query")
        gen.add("edge_query", self.edge_query)
        gen.add("node_query", self.node_query)
        gen.close()
        return gen.to_string()


class Edge:
    TYPE = TTuple(TMap(TString(), TString()), TString(), TString())

    def __init__(self, property, source, target):
        self.property = property
        self.source = source
        self.target = target

    def to_msgpack(self):
        t = (self.property, self.source, self.target)
        return self.__class__.TYPE.to_msgpack(t)

    @classmethod
    def from_msgpack(cls, arg):
        val = cls.TYPE.from_msgpack(arg)
        return Edge(*val)

    def __repr__(self):
        gen = jubatus.common.MessageStringGenerator()
        gen.open("edge")
        gen.add("property", self.property)
        gen.add("source", self.source)
        gen.add("target", self.target)
        gen.close()
        return gen.to_string()


class ShortestPathQuery:
    TYPE = TTuple(TString(), TString(), TInt(False, 4), TUserDef(PresetQuery))

    def __init__(self, source, target, max_hop, query):
        self.source = source
        self.target = target
        self.max_hop = max_hop
        self.query = query

    def to_msgpack(self):
        t = (self.source, self.target, self.max_hop, self.query)
        return self.__class__.TYPE.to_msgpack(t)

    @classmethod
    def from_msgpack(cls, arg):
        val = cls.TYPE.from_msgpack(arg)
        return ShortestPathQuery(*val)

    def __repr__(self):
        gen = jubatus.common.MessageStringGenerator()
        gen.open("shortest_path_query")
        gen.add("source", self.source)
        gen.add("target", self.target)
        gen.add("max_hop", self.max_hop)
        gen.add("query", self.query)
        gen.close()
        return gen.to_string()
