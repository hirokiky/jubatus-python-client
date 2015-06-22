# This file is auto-generated from graph.idl(0.6.4-33-gcc8d7ca) with jenerator version 0.5.1-457-g49229fa/master
# *** DO NOT EDIT ***


import msgpackrpc
import jubatus.common
from .types import *
from jubatus.common.types import *


class Graph(jubatus.common.ClientBase):

    def __init__(self, host, port, name, timeout=10):
        super(Graph, self).__init__(host, port, name, timeout)

    def create_node(self):
        return self.jubatus_client.call("create_node", [], TString(), [])

    def remove_node(self, node_id):
        return self.jubatus_client.call("remove_node", [node_id], TBool(), [TString(
        )])

    def update_node(self, node_id, property):
        return self.jubatus_client.call("update_node", [node_id, property], TBool(),
                                        [TString(), TMap(TString(), TString())])

    def create_edge(self, node_id, e):
        return self.jubatus_client.call("create_edge", [node_id, e], TInt(False, 8),
                                        [TString(), TUserDef(Edge)])

    def update_edge(self, node_id, edge_id, e):
        return self.jubatus_client.call("update_edge", [node_id, edge_id, e], TBool(
        ), [TString(), TInt(False, 8), TUserDef(Edge)])

    def remove_edge(self, node_id, edge_id):
        return self.jubatus_client.call("remove_edge", [node_id, edge_id], TBool(),
                                        [TString(), TInt(False, 8)])

    def get_centrality(self, node_id, centrality_type, query):
        return self.jubatus_client.call("get_centrality", [node_id, centrality_type,
                                                           query], TFloat(), [TString(), TInt(True, 4), TUserDef(PresetQuery)])

    def add_centrality_query(self, query):
        return self.jubatus_client.call("add_centrality_query", [query], TBool(),
                                        [TUserDef(PresetQuery)])

    def add_shortest_path_query(self, query):
        return self.jubatus_client.call("add_shortest_path_query", [query], TBool(),
                                        [TUserDef(PresetQuery)])

    def remove_centrality_query(self, query):
        return self.jubatus_client.call("remove_centrality_query", [query], TBool(),
                                        [TUserDef(PresetQuery)])

    def remove_shortest_path_query(self, query):
        return self.jubatus_client.call("remove_shortest_path_query", [query],
                                        TBool(), [TUserDef(PresetQuery)])

    def get_shortest_path(self, query):
        return self.jubatus_client.call("get_shortest_path", [query], TList(TString(
        )), [TUserDef(ShortestPathQuery)])

    def update_index(self):
        return self.jubatus_client.call("update_index", [], TBool(), [])

    def clear(self):
        return self.jubatus_client.call("clear", [], TBool(), [])

    def get_node(self, node_id):
        return self.jubatus_client.call("get_node", [node_id], TUserDef(Node),
                                        [TString()])

    def get_edge(self, node_id, edge_id):
        return self.jubatus_client.call("get_edge", [node_id, edge_id], TUserDef(
            Edge), [TString(), TInt(False, 8)])

    def create_node_here(self, node_id):
        return self.jubatus_client.call("create_node_here", [node_id], TBool(),
                                        [TString()])

    def remove_global_node(self, node_id):
        return self.jubatus_client.call("remove_global_node", [node_id], TBool(),
                                        [TString()])

    def create_edge_here(self, edge_id, e):
        return self.jubatus_client.call("create_edge_here", [edge_id, e], TBool(),
                                        [TInt(False, 8), TUserDef(Edge)])
