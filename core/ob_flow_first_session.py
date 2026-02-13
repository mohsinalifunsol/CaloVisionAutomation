"""OB 1st session flow for handling app initialization and onboarding screens."""
import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

from config.config import SPLASH_SCREEN_MIN_WAIT, SCREEN_TRANSITION_DELAY
from utils.logger import setup_logger

logger = setup_logger(__name__)


class OBFlowsFirstSession:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ============ LOCATORS ============
    # Splash Screen
    SPLASH_SCREEN_INDICATOR = None  # Add if there's a specific splash element

    # Onboarding Screen 1 - Get Started
    GET_STARTED_BTN_TEXT = "Get Started"
    GET_STARTED_BTN_XPATH = '//android.widget.TextView[@text="Get Started"]'

    # Onboarding Screen 2 - Continue
    CONTINUE_BTN_TEXT = "Continue"
    CONTINUE_BTN_XPATH = '//android.widget.TextView[@text="Continue"]'

    # Onboarding Screen 3 - Name Input
    NAME_INPUT_XPATH = '//android.widget.EditText'
    NAME_INPUT_CLASS = "android.widget.EditText"
    NAME_CONTINUE_BTN_XPATH = '//android.widget.TextView[@text="Continue"]'



    # -----------------------Splash Screen-----------------------#
    def handel_splash_screen(self):
        """Handle splash screen with proper wait"""

        logger.info(f"Waiting for splash screen (minimum {SPLASH_SCREEN_MIN_WAIT} seconds)...")

        # Wait for app to initialize - ensure current_activity is available
        start_time = time.time()
        try:
            WebDriverWait(self.driver, 4).until(
                lambda d: d.current_activity is not None
            )
            elapsed = time.time() - start_time
            logger.info(f"App activity detected after {elapsed:.2f} seconds.")
        except TimeoutException:
            logger.warning("Activity not detected, but continuing...")

        # Ensure minimum wait time for splash screen
        elapsed = time.time() - start_time
        if elapsed < SPLASH_SCREEN_MIN_WAIT:
            remaining_wait = SPLASH_SCREEN_MIN_WAIT - elapsed
            logger.info(f"Waiting additional {remaining_wait:.2f} seconds for splash screen...")
            time.sleep(remaining_wait)

        logger.info("Splash Screen wait completed.")

        # Wait a bit more for UI to stabilize
        logger.info(f"Waiting {SCREEN_TRANSITION_DELAY} seconds for UI to stabilize...")
        time.sleep(SCREEN_TRANSITION_DELAY)



    # -----------------------Onboarding Screen 1-----------------------#
    def is_get_started_visible(self, timeout=10):
        """Check if Get Started button is visible"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.GET_STARTED_BTN_XPATH)
                )
            )
            logger.info("✓ Get Started button is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Get Started button not found")
            return False

    def click_get_started(self, timeout=10):
        """Click Get Started button"""
        try:
            logger.info("Attempting to click Get Started button...")

            # Wait for element to be clickable
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GET_STARTED_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Get Started button")

            # Wait for screen transition
            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Get Started button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Get Started: {str(e)}")
            return False

    def verify_onboarding_screen(self):
        """Verify onboarding screen loaded successfully"""
        try:
            if self.is_get_started_visible(timeout=10):
                logger.info("✓ Onboarding screen loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying onboarding screen: {str(e)}")
            return False



    # -----------------------Onboarding Screen 2-----------------------#
    def is_continue_visible(self, timeout=10):
        """Check if continue button is visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.CONTINUE_BTN_XPATH)
                )
            )
            logger.info("✓ Continue button is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Continue button not found")
            return False

    def click_continue(self, timeout=10):
        """Click Continue button"""
        try:
            logger.info("Attempting to click Continue button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONTINUE_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Continue button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Continue button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Continue: {str(e)}")
            return False

    def verify_continue_screen(self):
        """Verify continue screen loaded successfully"""
        try:
            if self.is_continue_visible(timeout=10):
                logger.info("✓ Onboarding screen 2 (Continue) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 2 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying continue screen: {str(e)}")
            return False



    # -----------------------Onboarding Screen 3 - Name Input-----------------------#
    def is_name_input_visible(self, timeout=10):
        """Check if name input field visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.NAME_INPUT_XPATH)
                )
            )
            logger.info("✓ Name input field is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Name input field not found")
            return False

    def enter_name(self, name="Mohsin", timeout=10):
        """Enter name in the input field"""
        try:
            logger.info(f"Attempting to enter name: {name}")

            # Wait for input field
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.NAME_INPUT_XPATH)
                )
            )

            # Clear existing text (if any)
            element.clear()
            logger.info("✓ Cleared existing text")
            time.sleep(0.5)

            #Click on input field
            element.click()
            logger.info("✓ Clicked on name input field")
            time.sleep(1)

            # Type name
            element.send_keys(name)
            logger.info(f"✓ Successfully entered name: {name}")
            return True

        except TimeoutException:
            logger.error(f"✗ Name input field not found within {timeout} seconds")
            return False

        except Exception as e:
            logger.error(f"✗ Error entering name: {str(e)}")
            return False

    def hide_keyboard(self):
        """Hide keyboard using back press"""
        try:
            logger.info("Attempting to hide keyboard...")

            # Press back button to hide keyboard
            self.driver.press_keycode(4)  # 4 = KEYCODE_BACK
            logger.info("✓ Keyboard hidden successfully")

            time.sleep(1)
            return True

        except Exception as e:
            logger.error(f"✗ Error hiding keyboard: {str(e)}")
            return False

    def click_name_continue(self, timeout=10):
        """Click Continue button after entering name"""
        try:
            logger.info("Attempting to click Continue button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONTINUE_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Continue button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True
        except TimeoutException:
            logger.error(f"✗ Continue button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Continue: {str(e)}")
            return False

    def verify_name_input_screen(self):
        """Verify onboarding screen loaded successfully"""
        try:
            if self.is_name_input_visible(timeout=10):
                logger.info("✓ Onboarding screen 3 (Name Input) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 3 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying name input screen: {str(e)}")
            return False



    # -----------------------Complete Flow-----------------------#
    def complete_onboarding_flow(self):
        """Complete onboarding flow from splash to Get Started"""
        try:
            # Step 1: Handle splash screen
            logger.info("=== Starting Onboarding Flow ===")
            self.handel_splash_screen()

            # Step 2: Verify and click Get Started
            if not self.verify_onboarding_screen():
                logger.error("Failed to load onboarding screen 1")
                return False

            if not self.click_get_started():
                logger.error("Failed to click Get Started")
                return False

            # Step 3 verify and click Continue
            if not self.verify_continue_screen():
                logger.error("Failed to click Continue Screen 2")
                return False

            if not self.click_continue():
                logger.error("Failed to click Continue")
                return False

            # Step 4 Enter name and continue
            if not self.verify_name_input_screen():
                logger.error("Failed to load onboarding screen 3 (Name Input)")
                return False

            if not self.enter_name(name="Mohsin"):
                logger.error("Failed to enter name")
                return False

            if not self.hide_keyboard():
                logger.error("Failed to hide keyboard")
                return False

            if not self.click_name_continue():
                logger.error("Failed to click Continue Button after entering name")
                return False

            logger.info("======== Onboarding Flow Completed Successfully ========")
            return True

        except Exception as e:
            logger.error(f"✗ Error in onboarding flow: {str(e)}")
            return False




