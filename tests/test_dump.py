from .compat import unittest
import ucl
import sys

class DumpTest(unittest.TestCase):
    def test_no_args(self):
        with self.assertRaises(TypeError):
            ucl.dump()

    def test_multi_args(self):
        with self.assertRaises(TypeError):
            ucl.dump(0, 0)

    def test_none(self):
        self.assertEqual(ucl.dump(None), None)

    def test_int(self):
        self.assertEqual(ucl.dump({ "a" : 1 }), "a = 1;\n")

    def test_nested_int(self):
        self.assertEqual(ucl.dump({ "a" : { "b" : 1 } }), "a {\n    b = 1;\n}\n")

    def test_int_array(self):
        self.assertEqual(ucl.dump({ "a" : [1,2,3,4]}), "a [\n    1,\n    2,\n    3,\n    4,\n]\n")

    def test_str(self):
        self.assertEqual(ucl.dump({"a" : "b"}), "a = \"b\";\n")

    @unittest.skipIf(sys.version_info[0] > 2, "Py3k uses only unicode")
    def test_unicode(self):
        self.assertEqual(ucl.dump({unicode("a") : unicode("b")}), unicode("a = \"b\";\n"))

    def test_float(self):
        self.assertEqual(ucl.dump({"a" : 1.1}), "a = 1.100000;\n")

    def test_boolean(self):
        totest = {"a" : True, "b" : False}
        correct = ["a = true;\nb = false;\n", "b = false;\na = true;\n"]
        self.assertIn(ucl.dump(totest), correct)

    def test_empty_ucl(self):
        self.assertEqual(ucl.dump({}), "")

    def test_json(self):
        totest = { "a" : 1, "b": "bleh;" }
        correct = ['{\n    "a": 1,\n    "b": "bleh;"\n}',
                   '{\n    "b": "bleh;",\n    "a": 1\n}']
        self.assertIn(ucl.dump(totest, ucl.UCL_EMIT_JSON), correct)
