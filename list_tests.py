import unittest
import sys
sys.path.append('src')
sys.path.append('tests')

loader = unittest.TestLoader()
suite = loader.discover('tests')

def list_tests(suite):
    tests = []
    for test in suite:
        if isinstance(test, unittest.TestCase):
            tests.append(test.id())
        elif isinstance(test, unittest.TestSuite):
            tests.extend(list_tests(test))
    return tests

print("Total tests:", len(list_tests(suite)))
