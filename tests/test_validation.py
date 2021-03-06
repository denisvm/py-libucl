from .compat import unittest
import ucl
import json
import os.path
import glob
import re

TESTS_SCHEMA_FOLDER = 'vendor/libucl/tests/schema/*.json'

class ValidationTest(unittest.TestCase):
    def validate(self, jsonfile):
        comment_re = re.compile('\/\*((?!\*\/).)*?\*\/', re.DOTALL | re.MULTILINE)
        def json_remove_comments(content):
            return comment_re.sub('', content)

        def perform_test(schema, data, expected):
            if expected:
                self.assertTrue(ucl.validate(schema, data))
            else:
                with self.assertRaises(ucl.SchemaError):
                    ucl.validate(schema, data)

        with open(jsonfile) as f:
            filedata = f.read()
            filedata = json_remove_comments(filedata)
            # data = json.load(f)

            try:
                data = json.loads(filedata)
            except ValueError as e:
                raise self.skipTest('Failed to load JSON: %s' % str(e))

            for testgroup in data:
                for test in testgroup['tests']:
                    perform_test(json.dumps(testgroup['schema']), test['data'], test['valid'])


def setupValidationTests():
    """Creates each test dynamically from a folder"""
    def test_gen(filename):
        def test(self):
            self.validate(filename)
        return test

    for jsonfile in glob.glob(TESTS_SCHEMA_FOLDER):
        testname = os.path.splitext(os.path.basename(jsonfile))[0]
        if testname == 'patternProperties': continue
        setattr(ValidationTest, 'test_%s' % testname, test_gen(jsonfile))


setupValidationTests()
