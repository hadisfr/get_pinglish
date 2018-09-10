from get_pinglish import get_pinglish_from_word


def test_get_pinglish():
    res = get_pinglish_from_word("گنج")
    assert "Ganj" in res
    assert "Gonj" in res
