import sys

if sys.version_info >= (3, 0):
    int_types = (int, )  # NOQA
    string_types = (str, )  # NOQA
    binary_types = (bytes, )  # NOQA

    def u(s):
        return s

    def b(s):
        return s.encode()  # NOQA

else:
    int_types = (int, long)  # NOQA
    string_types = (str, unicode)  # NOQA
    binary_types = (str, )  # NOQA

    def u(s):
        return unicode(s)  # NOQA

    def b(s):
        return s
