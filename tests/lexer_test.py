from nose.tools import *
from whitepy.lexerconstants import *
import unittest
import whitepy.lexer as lexer


class TestLexer(unittest.TestCase):

    def _get_lexer(self, line):
        return lexer.Lexer(line=line)

    def _sample_ws(self, ws_type):
        ws_samples = {
            'valid': "   \t\n",
            'invalid_int': "   \t"
        }
        return self._get_lexer(ws_samples[ws_type])

    def test_get_int(self):
        lexer = self._sample_ws('valid')
        r = lexer._get_int()
        assert r.get_type() == 'INT' and r.get_value() == 'POSITIVE 001'

    @raises(lexer.IntError)
    def test_invalid_int(self):
        lexer = self._sample_ws('invalid_int')
        lexer._get_int()

    def test_get_token(self):
        lexer = self._sample_ws('valid')
        lexer.pos = 1
        r = lexer._get_token(IMP_CONST)
        assert r.get_type() == 'STACK_MANIPULATION'

    def test_get_all_tokens(self):
        lexer = self._sample_ws('valid')
        lexer.get_all_tokens()
        t = lexer.tokens
        assert t[0].get_type() is 'STACK_MANIPULATION' and \
            t[1].get_type() is 'PUSH' and t[2].get_type() is 'INT'
