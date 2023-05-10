# Lokalise API v2 official Python interface

![PyPI](https://img.shields.io/pypi/v/python-lokalise-api)
![CI](https://github.com/lokalise/python-lokalise-api/actions/workflows/ci.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/lokalise/python-lokalise-api/badge.svg?branch=master)](https://coveralls.io/github/lokalise/python-lokalise-api?branch=master)
[![Downloads](https://pepy.tech/badge/python-lokalise-api)](https://pepy.tech/project/python-lokalise-api)
[![Docs](https://readthedocs.org/projects/python-lokalise-api/badge/?version=latest&style=flat)](https://python-lokalise-api.readthedocs.io)

Official Python 3 interface for the [Lokalise APIv2](https://developers.lokalise.com/reference/lokalise-rest-api) that represents returned data as Python objects.

## Quick start

This plugin requires Python 3.7 and above. Install it:

    pip install python-lokalise-api

Obtain a Lokalise API token (in your *Personal profile*) and use it:

```python
import lokalise
client = lokalise.Client('YOUR_API_TOKEN')
project = client.project('123.abc')
print(project.name)

client.upload_file(project.project_id, {
    "data": 'ZnI6DQogIHRlc3Q6IHRyYW5zbGF0aW9u',
    "filename": 'python_upload.yml',
    "lang_iso": 'en'
})

translation_keys = client.keys(project.project_id, {"page": 2,
    "limit": 3,
    "disable_references": "1"})
translation_keys.items[0].key_name['web'] # => "sign_up"
```

You can also use [OAuth 2 tokens](https://python-lokalise-api.readthedocs.io/en/latest/additional_info/oauth2_flow.html):

```python
client = lokalise.OAuthClient('YOUR_OAUTH2_API_TOKEN')

project = client.project('123.abc')
```

## Documentation

Find detailed documentation at [python-lokalise-api.readthedocs.io](https://python-lokalise-api.readthedocs.io).

## License

This plugin is licensed under the [BSD 3 Clause License](https://github.com/lokalise/python-lokalise-api/blob/master/LICENSE).

Copyright (c) [Lokalise group](https://lokalise.com) and [Ilya Krukowski](http://bodrovis.tech)
