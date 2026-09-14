from appium.options.android import UiAutomator2Options

from config.settings import (
    APPIUM_SERVER_URL,
      PLATFORM_NAME, 
      DEVICE_NAME, 
      APP_PACKAGE, 
      APP_ACTIVITY, 
      AUTOMATION_NAME)


def get_android_options() -> UiAutomator2Options:
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app_package = "com.neighborly.thinkfirst"
    options.app_activity = "com.neighborly.thinkfirst.MainActivity"
    options.automation_name = "UiAutomator2"
    return options