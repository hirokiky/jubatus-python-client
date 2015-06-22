from .message_string_generator import MessageStringGenerator  # NOQA
from .datum import Datum  # NOQA
from .types import TInt, TFloat, TBool, TString, TRaw, TNullable, TList, TMap, TTuple, TUserDef, TObject  # NOQA
from .client import Client, ClientBase, TypeMismatch, UnknownMethod  # NOQA

from contextlib import contextmanager


@contextmanager
def connect(cls, host, port, name, timeout=10):
    client = cls(host, port, name, timeout)
    try:
        yield(client)
    finally:
        client.get_client().close()
