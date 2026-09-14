from driver.driver_factory import create_driver

def test_thinkfirst_launch(driver):
    # driver = create_driver()
    # print("Current Activity:", driver.current_activity)
    # print("Current Package:", driver.current_package)
    # driver.quit()

    assert driver.current_package=="com.neighborly.thinkfirst"
    