import unittest
from travis_demo import task
import numpy as np


class TestTask(unittest.TestCase):

    def test_task_scalar(self):
        a = 2
        b = 10
        exp = 20
        obs = brandon_task.product(a, b)
        self.assertEqual(exp,obs)

    def test_task_vectors(self):
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        exp = 32
        obs = brandon_task.product(a,b)
        self.assertEqual(exp,obs)
