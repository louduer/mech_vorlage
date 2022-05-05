# Copyright 2022 Hochschule Luzern - Informatik
# Author: Silvan Wegmann <silvan.wegmann@hslu.ch>
import unittest
from PIDController import PIDController


class PIDControllerTest(unittest.TestCase):
    def setUp(self):
        self.pid = PIDController()

    def tearDown(self):
        del self.pid

    def test_init(self):
        self.assertEqual(self.pid.errorLinear, self.pid.refposition,
                         "linear error and reference position should be equal at initialisation")
        self.assertEqual(self.pid.errorIntegral, 0,
                         "integral error should be 0 at initialisation")

    def test_7steps(self):
        self.assertEqual(self.pid.calculateTargetValue(0)[0], 207)
        self.assertEqual(self.pid.calculateTargetValue(100)[0], 107)
        self.assertEqual(self.pid.calculateTargetValue(200)[0], 57)
        self.assertEqual(self.pid.calculateTargetValue(300)[0], 8)
        self.assertEqual(self.pid.calculateTargetValue(400)[0], -41)
        self.assertEqual(self.pid.calculateTargetValue(430)[0], -21)
        self.assertEqual(self.pid.calculateTargetValue(415)[0], 8)
        self.assertEqual(self.pid.calculateTargetValue(415)[0], 0)

        self.assertAlmostEqual(self.pid.errorIntegral, 10.6, 3)
