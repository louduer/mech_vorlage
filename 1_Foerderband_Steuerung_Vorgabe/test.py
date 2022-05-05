# Copyright 2022 Hochschule Luzern - Informatik
# Author: Silvan Wegmann <silvan.wegmann@hslu.ch>
import sys
from tests.utils import is_raspberrypi
if not is_raspberrypi():
    sys.path.append("tests/mocks")

import unittest
from tests.EncoderTest import EncoderTest
# uncomment the following line when you have matplotlib installed
#from tests.LoggerTest import LoggerTest
from tests.PIDControllerTest import PIDControllerTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(EncoderTest))
    #suite.addTest(unittest.makeSuite(LoggerTest))
    suite.addTest(unittest.makeSuite(PIDControllerTest))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
