import requests
import json
from random import randint


def _call_api(text):
    endpoint = "http://www.virastlive.com/trans.php"
    res = requests.post(
        endpoint,
        headers={"Accept": "application/json", "charset": "UTF-8"},
        data={"json": json.dumps({
            "id": randint(1, 99),
            "method": "Transliterate",
            "params": {
                "text": repr(text)[1:-1],
                "option": {
                    "SourceAlphabet": "Persian",
                    "DestinationAlphabet": "2OM",
                    "Diacritic": False
                }
            }
        })}
    )
    if res.status_code == 200:
        if not res.text or res.text == "VirexTransError":
            raise RuntimeError(res.text)
        else:
            return res.json()["result"][1]
    else:
        raise RuntimeError("%d: %s" % (res.status_code, res.text))


def get_pinglish_from_word(word, full_res=True):
    """get Pinglish form of a single word."""
    suggestions = _call_api(word)[0]["suggestions"]
    return suggestions if full_res else suggestions[0]


def get_pinglish(text):
    """get Pinglish form of a text."""
    return "".join([word["suggestions"][0] for word in _call_api(text)])
