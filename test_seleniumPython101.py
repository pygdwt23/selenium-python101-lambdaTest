import pytest
import logging
from scenarios import TestScenarios

def testscenario001(conftest):
    sc001 = TestScenarios(conftest)
    sc001.test_001()

def testscenario002(conftest):
    sc002 = TestScenarios(conftest)
    sc002.test_002()

def testscenario003(conftest):
    sc003 = TestScenarios(conftest)
    sc003.test_003()
