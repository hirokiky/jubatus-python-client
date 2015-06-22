# This file is auto-generated from burst.idl(0.6.4-96-g66ed74d) with jenerator version 0.5.1-457-g49229fa/master
# *** DO NOT EDIT ***


import msgpackrpc
import jubatus.common
from .types import *
from jubatus.common.types import *


class Burst(jubatus.common.ClientBase):

    def __init__(self, host, port, name, timeout=10):
        super(Burst, self).__init__(host, port, name, timeout)

    def add_documents(self, data):
        return self.jubatus_client.call("add_documents", [data], TInt(True, 4),
                                        [TList(TUserDef(Document))])

    def get_result(self, keyword):
        return self.jubatus_client.call("get_result", [keyword], TUserDef(Window),
                                        [TString()])

    def get_result_at(self, keyword, pos):
        return self.jubatus_client.call("get_result_at", [keyword, pos], TUserDef(
            Window), [TString(), TFloat()])

    def get_all_bursted_results(self):
        return self.jubatus_client.call("get_all_bursted_results", [], TMap(TString(
        ), TUserDef(Window)), [])

    def get_all_bursted_results_at(self, pos):
        return self.jubatus_client.call("get_all_bursted_results_at", [pos], TMap(
            TString(), TUserDef(Window)), [TFloat()])

    def get_all_keywords(self):
        return self.jubatus_client.call("get_all_keywords", [], TList(TUserDef(
            KeywordWithParams)), [])

    def add_keyword(self, keyword):
        return self.jubatus_client.call("add_keyword", [keyword], TBool(),
                                        [TUserDef(KeywordWithParams)])

    def remove_keyword(self, keyword):
        return self.jubatus_client.call("remove_keyword", [keyword], TBool(),
                                        [TString()])

    def remove_all_keywords(self):
        return self.jubatus_client.call("remove_all_keywords", [], TBool(), [])

    def clear(self):
        return self.jubatus_client.call("clear", [], TBool(), [])
