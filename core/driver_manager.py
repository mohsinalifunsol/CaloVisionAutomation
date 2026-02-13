"""Driver management for Appium automation."""
from appium import webdriver
from appium.options.android import UiAutomator2Options

import time
from config.config import (
    APPIUM_SERVER_URL,
    APP_PATH,
    PLATFORM_NAME,
    AUTOMATION_NAME,
    IMPLICIT_WAIT
)
from utils.logger import setup_logger

logger = setup_logger(__name__)


def start_driver():
    """Initialize and return Appium WebDriver instance.

    Returns:
        Configured WebDriver instance
    """
    options = UiAutomator2Options()
    options.platform_name = PLATFORM_NAME
    options.automation_name = AUTOMATION_NAME
    options.app = APP_PATH
    options.auto_grant_permissions = True

    logger.info(f"Starting app: {APP_PATH}")
    logger.info(f"Connecting to Appium server: {APPIUM_SERVER_URL}")

    try:
        driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
        driver.implicitly_wait(IMPLICIT_WAIT)
        logger.info("Driver initialized successfully")

        # Wait for app to start loading
        logger.info("Waiting for app to initialize...")
        time.sleep(2)

        return driver
    except Exception as e:
        logger.error(f"Failed to initialize driver: {str(e)}")
        raise


def quit_driver(driver):
    """Safely quit the driver.

    Args:
        driver: WebDriver instance to quit
    """
    if driver:
        try:
            driver.quit()
            logger.info("Driver closed successfully")
        except Exception as e:
            logger.warning(f"Error closing driver: {str(e)}")