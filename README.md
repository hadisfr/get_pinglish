# Get Pinglish
[![Travis (.com)](https://img.shields.io/travis/com/hadisfr/get_pinglish.svg?style=flat-square)](https://travis-ci.com/hadisfr/get_pinglish/)
[![Codecov](https://img.shields.io/codecov/c/github/hadisfr/get_pinglish.svg?style=flat-square)](https://codecov.io/gh/hadisfr/get_pinglish)

get Pinglish (فینگلیش) version of a Persian (فارسی) text using Virastyar's Taranevis (ترانویس ویراستیار)

## Usage

Install requirements by `pip install -r requirements.txt`, then:

```python
from get_pinglish import *

print(get_pinglish("گشتاسپ و گرشاسپ"))
print(get_pinglish_from_word("گنج"))
```

Or

```console
$ python get_pinglish
> رستم
Rostam
```

## Test

```bash
python -m pytest
```
