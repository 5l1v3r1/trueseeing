import os
import unittest
from hypothesis import given
from hypothesis.strategies import text

from trueseeing import smali

class SmaliDBTest(unittest.TestCase):
  def test_000(self):
    with open(os.path.join(os.path.dirname(__file__), "fixture_0.smali"), "r") as f:
      clazz = smali.Smali().parsed(f.read())
      print(clazz, [m for m in clazz.methods])
    assert True
