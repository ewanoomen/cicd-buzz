from buzz import generator


def test_sample_single_word():
    wordlist = ('foo', 'bar', 'foobar')
    word = generator.sample(wordlist)
    assert word in wordlist


def test_sample_multiple_words():
    wordlist = ('foo', 'bar', 'foobar')
    words = generator.sample(wordlist, 2)
    assert len(words) == 2
    assert words[0] in wordlist
    assert words[1] in wordlist
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
