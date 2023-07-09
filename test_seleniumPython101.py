import pytest
import logging
from scenarios import scenariosDef

def testscenarios(conftest):
    sc = scenariosDef(conftest)
    sc.test_001()
    sc.test_002()
    sc.test_003()
