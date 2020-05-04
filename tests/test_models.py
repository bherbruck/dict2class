import pytest
from dict2class import DictClass


first_name = 'Foo'
last_name = 'Bar'
email = 'foo.bar@foobar.com'
age = 32

dc = DictClass({
    'first_name': 'Foo',
    'last_name': 'Bar',
    'email': 'foo.bar@foobar.com',
    'age': 32,
    'friends': ['Jane', 'John']
})

full_json = '''{"first_name": "Foo", "last_name": "Bar", "email": "foo.bar@foobar.com", "age": 32, "friends": ["Jane", "John"]}'''
name_json = '''{"first_name": "Foo", "last_name": "Bar"}'''


def test_DictClass():
    assert dc.first_name == first_name
    assert dc.last_name == last_name
    assert dc.email == email
    assert dc.age == age


def test_DictClass_to_json():
    assert dc.to_json() == full_json
    assert dc.to_json(['first_name', 'last_name']) == name_json
