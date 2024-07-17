import pytest
from mvd import MultiValueDictionary

@pytest.fixture
def mvd():
    return MultiValueDictionary()

def test_keys(mvd):
    assert mvd.keys() == "(empty set)"
    mvd.add("foo", "bar")
    assert "foo" in mvd.keys()
    mvd.add("baz", "bang")
    keys = mvd.keys().split("\n")
    assert len(keys) == 2
    assert "foo" in keys[0] or "foo" in keys[1]
    assert "baz" in keys[0] or "baz" in keys[1]

def test_members(mvd):
    assert mvd.members("foo") == ") ERROR, key does not exist."
    mvd.add("foo", "bar")
    members = mvd.members("foo").split("\n")
    assert len(members) == 1
    assert "1) bar" in members
    mvd.add("foo", "baz")
    members = mvd.members("foo").split("\n")
    assert len(members) == 2
    assert "1) bar" in members or "2) bar" in members
    assert "1) baz" in members or "2) baz" in members

def test_add(mvd):
    assert mvd.add("foo", "bar") == ") Added"
    assert mvd.add("foo", "bar") == ") ERROR, member already exists for key"
    assert mvd.add("foo", "baz") == ") Added"
    assert mvd.members("foo") == "1) bar\n2) baz" or mvd.members("foo") == "1) baz\n2) bar"

def test_remove(mvd):
    assert mvd.remove("foo", "bar") == ") ERROR, key does not exist"
    mvd.add("foo", "bar")
    mvd.add("foo", "baz")
    assert mvd.remove("foo", "bar") == ") Removed"
    assert mvd.members("foo") == "1) baz"
    assert mvd.remove("foo", "bar") == ") ERROR, member does not exist"
    assert mvd.remove("foo", "baz") == ") Removed"
    assert mvd.keys() == "(empty set)"

def test_remove_all(mvd):
    assert mvd.remove_all("foo") == ") ERROR, key does not exist"
    mvd.add("foo", "bar")
    mvd.add("foo", "baz")
    assert mvd.remove_all("foo") == ") Removed"
    assert mvd.keys() == "(empty set)"

def test_clear(mvd):
    mvd.add("foo", "bar")
    mvd.add("baz", "bang")
    assert mvd.keys() != "(empty set)"
    assert mvd.clear() == ") Cleared"
    assert mvd.keys() == "(empty set)"

def test_key_exists(mvd):
    assert mvd.key_exists("foo") == ") false"
    mvd.add("foo", "bar")
    assert mvd.key_exists("foo") == ") true"

def test_member_exists(mvd):
    assert mvd.member_exists("foo", "bar") == ") false"
    mvd.add("foo", "bar")
    assert mvd.member_exists("foo", "bar") == ") true"
    assert mvd.member_exists("foo", "baz") == ") false"

def test_all_members(mvd):
    assert mvd.all_members() == "(empty set)"
    mvd.add("foo", "bar")
    mvd.add("foo", "baz")
    all_members = mvd.all_members().split("\n")
    assert len(all_members) == 2
    assert "1) bar" in all_members or "2) bar" in all_members
    assert "1) baz" in all_members or "2) baz" in all_members

def test_items(mvd):
    assert mvd.items() == "(empty set)"
    mvd.add("foo", "bar")
    mvd.add("foo", "baz")
    items = mvd.items().split("\n")
    assert len(items) == 2
    assert "foo: bar" in items
    assert "foo: baz" in items
    mvd.add("baz", "bang")
    items = mvd.items().split("\n")
    assert len(items) == 3
    assert "foo: bar" in items
    assert "foo: baz" in items
    assert "baz: bang" in items

if __name__ == "__main__":
    pytest.main()