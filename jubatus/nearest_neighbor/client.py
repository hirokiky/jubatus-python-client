# This file is auto-generated from nearest_neighbor.idl(0.6.4-33-gf65b203) with jenerator version 0.5.1-457-g49229fa/master
# *** DO NOT EDIT ***


import msgpackrpc
import jubatus.common
from .types import *
from jubatus.common.types import *


class NearestNeighbor(jubatus.common.ClientBase):

    def __init__(self, host, port, name, timeout=10):
        super(NearestNeighbor, self).__init__(host, port, name, timeout)

    def clear(self):
        return self.jubatus_client.call("clear", [], TBool(), [])

    def set_row(self, id, d):
        return self.jubatus_client.call("set_row", [id, d], TBool(), [TString(),
                                                                      TDatum()])

    def neighbor_row_from_id(self, id, size):
        return self.jubatus_client.call("neighbor_row_from_id", [id, size], TList(
            TUserDef(IdWithScore)), [TString(), TInt(False, 4)])

    def neighbor_row_from_datum(self, query, size):
        return self.jubatus_client.call("neighbor_row_from_datum", [query, size],
                                        TList(TUserDef(IdWithScore)), [TDatum(), TInt(False, 4)])

    def similar_row_from_id(self, id, ret_num):
        return self.jubatus_client.call("similar_row_from_id", [id, ret_num], TList(
            TUserDef(IdWithScore)), [TString(), TInt(True, 4)])

    def similar_row_from_datum(self, query, ret_num):
        return self.jubatus_client.call("similar_row_from_datum", [query, ret_num],
                                        TList(TUserDef(IdWithScore)), [TDatum(), TInt(True, 4)])

    def get_all_rows(self):
        return self.jubatus_client.call("get_all_rows", [], TList(TString()), [])
