# dict2class

[license-image]: https://img.shields.io/npm/l/make-coverage-badge.svg
[license-url]: https://opensource.org/licenses/MIT
[travis-image]: https://travis-ci.org/bherbruck/
[travis-url]: https://travis-ci.org/bherbruck/

[![License][license-image]][license-url]
<!-- [![Build Status][travis-image]][travis-url] -->

 Create an object from a dict

## Installation
```bash
$ pip install git+https://github.com/bherbruck/dict2class
```

<!-- ```bash
$ pip install dict2class
``` -->

## Example
```python
dc = DictClass({
    'first_name': 'Foo',
    'last_name': 'Bar',
    'email': 'foo.bar@foobar.com',
    'age': 32,
    'friends': ['Jane', 'John']
})
```
