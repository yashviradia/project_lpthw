from nose.tools import *
from ex48 import parser, lexicon

def test_subject():
    s1 = parser.Sentence(('noun', "cheese"),
                         ('verb', "eats"),
                         ('noun', "pigeon"))
    assert s1.verb == "eats"
    assert s1.subject == "cheese"
    assert s1.object == "pigeon"


def test_peek():
    word_list = []
    assert None == parser.peek(word_list)

    word_list = lexicon.scan("princess kill bear")
    assert "noun" == parser.peek(word_list)


def test_match():
    word_list = []
    assert None == parser.match(word_list, 'noun')

    word_list = lexicon.scan("bear eat princess")
    assert_equal(('noun', "bear"), parser.match(word_list, 'noun'))
    assert_equal(None, parser.match(word_list, 'noun'))

"""
def test_skip():
    word_list = lexicon.scan('bear eat door')
    assert_equal(word_list, [('noun', 'bear'), ('verb', 'eat'), ('noun', 'door')])
    parser.skip(word_list, 'noun')
    assert_equal(word_list, [('verb', 'eat'), ('noun', 'door')])

def test_parse_verb():
    word_list = lexicon.scan('it eat door')
    assert_equal(parser.parse_verb(word_list), ('verb', 'eat'))
    word_list = lexicon.scan('bear eat door')
    assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_object():
    word_list = lexicon.scan('the door')
    assert_equal(parser.parse_object(word_list), ('noun', 'door'))
    word_list = lexicon.scan('the east')
    assert_equal(parser.parse_object(word_list), ('direction', 'east'))
    word_list = lexicon.scan('the it')
    assert_raises(parser.ParserError, parser.parse_object, word_list)

def test_parse_subject():
    word_list = lexicon.scan('eat door')
    subj = ('noun', 'bear')
    s = parser.parse_subject(word_list, subj)
    assert_equal(s.to_tuple(), ('bear', 'eat', 1, 'door'))

def test_parse_sentence():
    word_list = lexicon.scan('the bear eat door')
    s = parser.parse_sentence(word_list)
    assert_equal(s.to_tuple(), ('bear', 'eat', 1, 'door'))
    word_list = lexicon.scan('in eat door')
    s = parser.parse_sentence(word_list)
    assert_equal(s.to_tuple(), ('player', 'eat', 1, 'door'))
    word_list = lexicon.scan('north eat door')
    assert_raises(parser.ParserError, parser.parse_sentence, word_list)

def test_unknown_words():
    word_list = lexicon.scan('xxx the xxx bear xxx eat xxx door xxx')
    s = parser.parse_sentence(word_list)
    assert_equal(s.to_tuple(), ('bear', 'eat', 1, 'door'))

def test_numbers():
    word_list = lexicon.scan('xxx the xxx bear xxx eat xxx 5 xxx door xxx')
    s = parser.parse_sentence(word_list)
    assert_equal(s.to_tuple(), ('bear', 'eat', 5, 'door'))
"""
