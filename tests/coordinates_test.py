#!/usr/bin/python3

import unittest
import numpy as np
import geoCV

class TestCoordinates(unittest.TestCase):
  """
  Unit test for coordinates.py.

  by Pavel Trutman, pavel.trutman@cvut.cz
  """


  def testa2h(self):
    """
    Test convertion to homogenous of some vectors.
    """

    a = np.array([[4, 6, 7], [0, 2, 7], [1, 9, 3]])
    h = np.array([[4, 6, 7], [0, 2, 7], [1, 9, 3], [1, 1, 1]])
    
    self.assertLessEqual(np.linalg.norm(h - geoCV.coordinates.a2h(a)), 1e-3)


  def testa2hRandom(self):
    """
    Test convertion to homogenous of some random vectors.
    """

    sizes = [2, 3, 10, 100]

    for i in range(len(sizes)):
      with self.subTest(i = i):
        a = np.random.normal(size=(sizes[i], sizes[i]))
        h = np.vstack((a, np.ones((1, sizes[i]))))
        self.assertLessEqual(np.linalg.norm(h - geoCV.coordinates.a2h(a)), 1e-3)


  def testh2a(self):
    """
    Test convertion to affine of some vectors
    """

    h = np.array([[3, 8, 9, 7], [2, 9, 5, 9], [0, 1, 1, 0], [5, 2, 3, 4]])
    a = np.array([[3/5, 8/2, 9/3, 7/4], [2/5, 9/2, 5/3, 9/4], [0/5, 1/2, 1/3, 0/4]])

    self.assertLessEqual(np.linalg.norm(a - geoCV.coordinates.h2a(h)), 1e-3)


  def testh2aRandom(self):
    """
    Test convertion to affine of some random vectors.
    """

    sizes = [2, 3, 10, 100]

    for i in range(len(sizes)):
      with self.subTest(i = i):
        h = np.random.normal(size=(sizes[i], sizes[i]))
        a = (h/np.matlib.repmat(h[-1, :], sizes[i], 1))[:-1, :]
        self.assertLessEqual(np.linalg.norm(a - geoCV.coordinates.h2a(h)), 1e-3)


  def testCalibrate(self):
    """
    Test calibrate on one example.
    """

    K = np.array([[1,  0,  2.73739e+03], [0, 1, 1.54825e+03], [0, 0, 1]])
    points = np.array([[3.55289e+03, 2.08543e+03, 2.17548e+03, 2.274e+03], [1.21907e+03, 1.11655e+03, 8.37526e+02, 1.33706e+03], [1, 1, 1, 1]])
    pointsCal = np.array([[815.5, -651.96, -561.91, -463.39 ], [-329.18, -431.7, -710.724, -211.19], [1, 1, 1, 1]])
    self.assertLessEqual(np.linalg.norm(pointsCal - geoCV.coordinates.calibrate(points, K)), 1e-3)


if __name__ == '__main__':
  unittest.main()