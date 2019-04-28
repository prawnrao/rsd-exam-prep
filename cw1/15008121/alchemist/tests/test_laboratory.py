import yaml
from pytest import raises
from ..laboratory import Laboratory


fixtures = yaml.load(open("alchemist/tests/fixtures.yml"))

fixture0_answer = fixtures[0].pop('answer')
fixture1_answer = fixtures[1].pop('answer')

lab0 = Laboratory(fixtures[0]['lab'])


def test_run_full_experiment():
    assert lab0.run_full_experiment(True) == fixture0_answer


def test_can_react():
    assert Laboratory.can_react('antiA', 'A')


def test_cannot_react():
    assert not Laboratory.can_react('antiA', 'B')


def test_antianti():
    with raises(Exception):
        Laboratory.can_react('antiantiA', 'antiA')


def test_empty_shelf():
    with raises(Exception):
        Laboratory({'lower': [], 'upper': [A, B]})


def test_three_shelves():
    with raises(Exception):
        Laboratory({'lower': [A], 'middle': [B], 'upper': [C]})


def test_update_shelves():
    assert Laboratory.update_shelves(
        ['a', 'b', 'c'], ['a', 'antib', 'c'], 'b', 1) == (['a', 'c'], ['a', 'c'])


def test_do_a_reaction():
    assert Laboratory.do_a_reaction(
        ['a', 'b', 'c'], ['a', 'antib', 'antic']) == (['a', 'c'], ['a', 'antic'])
