from cribl.lib.http_operations import *


def lib_tests():
    response = get("http://www.yahoo.com", None, None)
    print("Response: %s" % response.text)
