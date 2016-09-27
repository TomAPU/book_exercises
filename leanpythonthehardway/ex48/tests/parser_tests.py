from nose.tools import *
from ex48 import parser

def test_parse_sentence():
    x = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(x.subject, 'player')
    assert_equal(x.verb, 'run')
    assert_equal(x.object, 'north')


    x = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), (
        'noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(x.subject, 'bear')
    assert_equal(x.verb, 'eat')
    assert_equal(x.object, 'bear')
