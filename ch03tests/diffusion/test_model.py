from .model import energy
from pytest import raises

def test_energy():
	""" Optional description for pytest reporting """
	# Test something
	assert energy([0, 0, 0]) == 0
	assert energy([0, 0, 1]) == 0
	assert energy([1, 1, 1]) == 0
	assert energy([0, 0, 1, 2, 3]) == 8
	assert energy([0, 0, 1, 2, 3]) == 8


def test_energy_correct_input():
	with raises(TypeError):
		energy([1.0, 2, 3])
	with raises(TypeError):
		energy(['a', 'a', 'a'])
	with raises(TypeError):
		energy('a')