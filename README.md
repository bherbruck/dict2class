# dict2class

[license-image]: https://img.shields.io/npm/l/make-coverage-badge.svg
[license-url]: https://opensource.org/licenses/MIT


[![License][license-image]][license-url]
![Python package](https://github.com/bherbruck/dict2class/workflows/Python%20package/badge.svg)

 Create an object from a dict

## Installation
```bash
$ pip install git+https://github.com/bherbruck/dict2class
```
or
```bash
$ pip install dict2class
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
