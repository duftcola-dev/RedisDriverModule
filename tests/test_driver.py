from driver import Driver
def test_driver_exists(driver_instance:Driver):
    """Basic testing to check if the test can access the driver module

    Args:
        driver_instance (Driver): Redis self made Driver class
    """
    assert driver_instance is not None


def test_connection_failed(driver_instance:Driver):
    """Check how the driver handles connection failure

    Args:
        driver_instance (Driver): Redis self made Driver class
    """
    assert driver_instance.connect(password="wrong_password_for_test") is False


def test_driver_connection(driver_instance:Driver):
    """Check if the driver can connect to a redis database

    Args:
        driver_instance (Driver): Redis self made Driver class
    """
    assert driver_instance.connect(password="test") is True
    assert driver_instance.close() is True