# Lokalise API v2 official Python interface

Official Python 3 interface for the Lokalise APIv2 that represents returned data as Python objects.

## Quick start

This plugin requires Python 3.6 and above. Install it:

    pip install python-lokalise-api

Obtain a Lokalise API token (in your *Personal profile*) and use it:

```python
import lokalise
client = lokalise.Client('YOUR_API_TOKEN')
project = client.project('123.abc')
print(project.title)
```

## Documentation

Find documentation at readthedocs.io.

## License

This plugin is licensed under the BSD 3 Clause License.

Copyright (c) [Lokalise team](https://lokalise.com), [Ilya Bodrov](http://bodrovis.tech)
