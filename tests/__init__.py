import unittest

# Python 3.2+
if hasattr(unittest.TestCase, 'assertRaisesRegex'):
    pass
# Python 2.7 - 3.1
elif hasattr(unittest.TestCase, 'assertRaisesRegexp'):
    unittest.TestCase.assertRaisesRegex = unittest.TestCase.assertRaisesRegexp
# Python 2.6-
else:
    import re
    def assert_raises_regex(self, exception, regexp, callable, *args, **kwds):
        try:
            callable(*args, **kwds)
        except exception as e:
            if isinstance(regexp, basestring):
                regexp = re.compile(regexp)
            if not regexp.search(str(e)):
                raise self.failureException('"%s" does not match "%s"' %
                         (regexp.pattern, str(e)))
        else:
            if hasattr(exception,'__name__'): excName = exception.__name__
            else: excName = str(exception)
            raise AssertionError("%s not raised" % excName)
    unittest.TestCase.assertRaisesRegex = assert_raises_regex

# Python 2.6-
if not hasattr(unittest.TestCase, 'assertIn'):
    def assert_in(self, member, container, msg=None):
        if member not in container:
            standardMsg = '%s not found in %s' % (safe_repr(member),
                                                  safe_repr(container))
            self.fail(self._formatMessage(msg, standardMsg))
    unittest.TestCase.assertIn = assert_in
