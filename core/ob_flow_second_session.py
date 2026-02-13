"""OB 2nd session flows for handling app initialization and onboarding screens."""
import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from config.config import SPLASH_SCREEN_MIN_WAIT
from utils.logger import setup_logger

logger = setup_logger(__name__)

class OBFlows2ndSession:

    # -----------------------Splash Screen-----------------------#
    def handel_splash_screen(driver):

        logger.info(f"Waiting for splash screen (minimum {SPLASH_SCREEN_MIN_WAIT} seconds)...")

        # Wait for app to initialize -  ensure current_activity is available
        start_time = time.time()
        try:
            WebDriverWait(driver, 15).until(
                lambda d: d.current_activity is not None
            )
            elapsed = time.time() - start_time
            logger.info(f"App activity detected after {elapsed:.2f} seconds.")
        except TimeoutException:
            logger.warning("Activity not detected, bot continuing...")

        # Ensure minimum wait time for splash screen
        elapsed = time.time() - start_time
        if elapsed < SPLASH_SCREEN_MIN_WAIT:
            remaining_wait = SPLASH_SCREEN_MIN_WAIT - elapsed
            logger.info(f"Waiting additional {remaining_wait:.2f} seconds for splash screen...")
            time.sleep(remaining_wait)

        logger.info("Splash Screen wait completed.")

