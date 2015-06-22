# This file is auto-generated from recommender.idl(0.6.4-33-gcc8d7ca) with jenerator version 0.5.1-457-g49229fa/master
# *** DO NOT EDIT ***


import msgpackrpc
import jubatus.common
from .types import *
from jubatus.common.types import *


class Recommender(jubatus.common.ClientBase):

    def __init__(self, host, port, name, timeout=10):
        super(Recommender, self).__init__(host, port, name, timeout)

    def clear_row(self, id):
        return self.jubatus_client.call("clear_row", [id], TBool(), [TString()])

    def update_row(self, id, row):
        return self.jubatus_client.call("update_row", [id, row], TBool(), [TString(
        ), TDatum()])

    def clear(self):
        return self.jubatus_client.call("clear", [], TBool(), [])

    def complete_row_from_id(self, id):
        return self.jubatus_client.call("complete_row_from_id", [id], TDatum(),
                                        [TString()])

    def complete_row_from_datum(self, row):
        return self.jubatus_client.call("complete_row_from_datum", [row], TDatum(),
                                        [TDatum()])

    def similar_row_from_id(self, id, size):
        return self.jubatus_client.call("similar_row_from_id", [id, size], TList(
            TUserDef(IdWithScore)), [TString(), TInt(False, 4)])

    def similar_row_from_datum(self, row, size):
        return self.jubatus_client.call("similar_row_from_datum", [row, size],
                                        TList(TUserDef(IdWithScore)), [TDatum(), TInt(False, 4)])

    def decode_row(self, id):
        return self.jubatus_client.call("decode_row", [id], TDatum(), [TString()])

    def get_all_rows(self):
        return self.jubatus_client.call("get_all_rows", [], TList(TString()), [])

    def calc_similarity(self, lhs, rhs):
        return self.jubatus_client.call("calc_similarity", [lhs, rhs], TFloat(),
                                        [TDatum(), TDatum()])

    def calc_l2norm(self, row):
        return self.jubatus_client.call("calc_l2norm", [row], TFloat(), [TDatum()])
