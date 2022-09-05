from driver import Driver
import os
import pytest

redis_driver = Driver()

@pytest.fixture
def driver_instance():
    return redis_driver.get_instance()