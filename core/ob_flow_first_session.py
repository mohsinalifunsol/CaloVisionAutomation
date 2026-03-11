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

    # Onboarding Screen 4 - Gender Selection
    GENDER_MALE_XPATH = '//android.widget.ScrollView/android.view.View[2]'
    GENDER_FEMALE_XPATH = '//android.widget.ScrollView/android.view.View[3]'
    GENDER_NON_BINARY_XPATH = '//android.widget.ScrollView/android.view.View[4]'
    CONFIRM_IDENTITY_BTN_XPATH = '//android.widget.TextView[@text="Confirm Identity"]'

    # Onboarding Screen 5 - Date of Birth Selection
    DOB_DATE_PICKER_XPATH = '//android.widget.ScrollView/android.view.View[1]'
    DOB_MONTH_PICKER_XPATH = '//android.widget.ScrollView/android.view.View[2]'
    DOB_YEAR_PICKER_XPATH = '//android.widget.ScrollView/android.view.View[3]'
    CONFIRM_AGE_BTN_XPATH = '//android.widget.TextView[@text="Confirm Age"]'

    # Onboarding Screen 6 - Height Selection
    HEIGHT_PICKER_XPATH = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]'
    CONFIRM_HEIGHT_BTN_XPATH = '//android.widget.TextView[@text="Confirm Height"]'

    # Onboarding Screen 7 - Continue
    SCREEN_7_CONTINUE_BTN_XPATH = '//android.widget.TextView[@text="Continue"]'

    # Onboarding Screen 8 - Weight Selection
    WEIGHT_PICKER_XPATH = '//android.widget.ScrollView/android.view.View[4]'
    CONFIRM_WEIGHT_BTN_XPATH = '//android.widget.TextView[@text="Confirm Weight"]'

    # Onboarding Screen 9 - Fitness Goal Selection
    GOAL_LOSE_WEIGHT_XPATH = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]'
    GOAL_MAINTAIN_WEIGHT_XPATH = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]'
    GOAL_GAIN_WEIGHT_XPATH = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]'
    CONFIRM_GOAL_BTN_XPATH = '//android.widget.TextView[@text="Confirm Goal"]'

    # Onboarding Screen 10 - Target Weight Selection
    TARGET_WEIGHT_SCROLLABLE_XPATH = '//android.widget.ScrollView/android.view.View[4]'
    CONFIRM_TARGET_XPATH = '//android.widget.TextView[@text="Confirm Target"]'

    # Onboarding Screen 11 - Activity Level Selection
    ACTIVITY_NOT_VERY_ACTIVE_XPATH = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]'
    ACTIVITY_LIGHTLY_ACTIVE_XPATH = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]'
    ACTIVITY_ACTIVE_XPATH = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]'
    ACTIVITY_VERY_ACTIVE_XPATH = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[4]'
    CONFIRM_ACTIVITY_BTN_XPATH = '//android.widget.TextView[@text="Confirm Activity"]'

    # Onboarding Screen 12 - Meals Per Day Selection
    MEALS_2_PER_DAY_XPATH = '//android.widget.SeekBar[@text="2.0"]/android.view.View/android.view.View'
    MEALS_3_PER_DAY_XPATH = '//android.widget.SeekBar[@text="3.0"]/android.view.View/android.view.View'
    MEALS_4_PER_DAY_XPATH = '//android.widget.SeekBar[@text="4.0"]/android.view.View/android.view.View'
    MEALS_5_PER_DAY_XPATH = '//android.widget.SeekBar[@text="5.0"]/android.view.View/android.view.View'
    CONFIRM_PREFERENCE_BTN_XPATH = '//android.widget.TextView[@text="Confirm Preference"]'

    # Onboarding Screen 13 - Medical Condition Selection (Scrollable)
    MEDICAL_NONE_XPATH = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]'
    CONFIRM_CONDITION_BTN_XPATH = '//android.widget.TextView[@text="Confirm Condition"]'

    # Medical condition options using text-based locators (more reliable for scrollable content)
    MEDICAL_DIABETES_TEXT = "Diabetes"
    MEDICAL_PRE_DIABETES_TEXT = "Pre-Diabetes"
    MEDICAL_CHOLESTEROL_TEXT = "Cholesterol"
    MEDICAL_HYPERTENSION_TEXT = "Hypertension"
    MEDICAL_PCOS_TEXT = "PCOS"
    MEDICAL_THYROID_TEXT = "Thyroid"
    MEDICAL_PHYSICAL_INJURY_TEXT = "Physical Injury"

    # Onboarding Screen 14 - Goal Achievement Rate Selection
    GOAL_RATE_0_2_KG_XPATH = '//android.widget.SeekBar[@text="0.2"]/android.view.View'
    GOAL_RATE_0_4_KG_XPATH = '//android.widget.SeekBar[@text="0.4"]/android.view.View'
    GOAL_RATE_0_6_KG_XPATH = '//android.widget.SeekBar[@text="0.6"]/android.view.View'
    GOAL_RATE_0_8_KG_XPATH = '//android.widget.SeekBar[@text="0.8"]/android.view.View'
    GOAL_RATE_10_0_KG_XPATH = '//android.widget.SeekBar[@text="10.0"]/android.view.View'
    GOAL_RATE_CONTINUE_BTN_XPATH = '//android.widget.TextView[@text="Continue"]'

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



    # -----------------------Onboarding Screen 3 - Name Input------------------------#
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

    # -----------------------Onboarding Screen 4 - Gender Selection-----------------------#
    def is_gender_screen_visible(self, timeout=10):
        """Check if gender selection screen is visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.GENDER_MALE_XPATH)
                )
            )
            logger.info("✓ Gender selection screen is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Gender selection screen not found")
            return False

    def select_gender_male(self, timeout=10):
        """Select Male gender option"""
        try:
            logger.info("Attempting to select Male gender...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GENDER_MALE_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected Male gender")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ Male gender option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting Male gender: {str(e)}")
            return False

    def select_gender_female(self, timeout=10):
        """Select Female gender option"""
        try:
            logger.info("Attempting to select Female gender...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GENDER_FEMALE_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected Female gender")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ Female gender option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting Female gender: {str(e)}")
            return False

    def select_gender_non_binary(self, timeout=10):
        """Select Non-Binary gender option"""
        try:
            logger.info("Attempting to select Non-Binary gender...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GENDER_NON_BINARY_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected Non-Binary gender")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ Non-Binary gender option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting Non-Binary gender: {str(e)}")
            return False

    def click_confirm_identity(self, timeout=10):
        """Click Confirm Identity button"""
        try:
            logger.info("Attempting to click Confirm Identity button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONFIRM_IDENTITY_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Confirm Identity button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Confirm Identity button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Confirm Identity: {str(e)}")
            return False

    def verify_gender_screen(self):
        """Verify gender selection screen loaded successfully"""
        try:
            if self.is_gender_screen_visible(timeout=10):
                logger.info("✓ Onboarding screen 4 (Gender Selection) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 4 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying gender screen: {str(e)}")
            return False

    # -----------------------Onboarding Screen 5 - Date of Birth Selection-----------------------#
    def is_dob_screen_visible(self, timeout=10):
        """Check if date of birth screen is visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.DOB_DATE_PICKER_XPATH)
                )
            )
            logger.info("✓ Date of Birth screen is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Date of Birth screen not found")
            return False

    def scroll_picker(self, picker_xpath, direction="down", scrolls=1):
        """
        Scroll picker up or down

        Args:
            picker_xpath: XPath of the picker element
            direction: "up" or "down"
            scrolls: Number of scroll actions
        """
        try:
            element = self.driver.find_element(AppiumBy.XPATH, picker_xpath)

            # Get element bounds
            location = element.location
            size = element.size

            start_x = location['x'] + size['width'] // 2
            start_y = location['y'] + size['height'] // 2

            # Scroll distance
            scroll_distance = size['height'] // 3

            for _ in range(scrolls):
                if direction == "down":
                    end_y = start_y + scroll_distance
                else:  # up
                    end_y = start_y - scroll_distance

                self.driver.swipe(start_x, start_y, start_x, end_y, duration=500)
                time.sleep(0.3)

            logger.info(f"✓ Scrolled picker {direction} {scrolls} time(s)")
            return True

        except Exception as e:
            logger.error(f"✗ Error scrolling picker: {str(e)}")
            return False

    def select_date(self, date=9, timeout=10):
        """
        Select date by scrolling

        Args:
            date: Date to select (1-31)
        """
        try:
            logger.info(f"Attempting to select date: {date}")

            # Wait for picker to be present
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.DOB_DATE_PICKER_XPATH)
                )
            )

            # Default is around middle (15-16), scroll based on target
            # This is approximate - adjust based on your app's behavior
            if date < 15:
                scrolls = (15 - date)
                self.scroll_picker(self.DOB_DATE_PICKER_XPATH, "up", scrolls)
            elif date > 15:
                scrolls = (date - 15)
                self.scroll_picker(self.DOB_DATE_PICKER_XPATH, "down", scrolls)

            logger.info(f"✓ Selected date: {date}")
            time.sleep(0.5)
            return True

        except Exception as e:
            logger.error(f"✗ Error selecting date: {str(e)}")
            return False

    def select_month(self, month="Nov", timeout=10):
        """
        Select month by scrolling

        Args:
            month: Month name (Jan, Feb, Mar, etc.)
        """
        try:
            logger.info(f"Attempting to select month: {month}")

            # Wait for picker to be present
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.DOB_MONTH_PICKER_XPATH)
                )
            )

            # Month mapping (assuming Oct is default/middle)
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

            try:
                current_index = 9  # Oct (0-based index)
                target_index = months.index(month)

                if target_index < current_index:
                    scrolls = current_index - target_index
                    self.scroll_picker(self.DOB_MONTH_PICKER_XPATH, "up", scrolls)
                elif target_index > current_index:
                    scrolls = target_index - current_index
                    self.scroll_picker(self.DOB_MONTH_PICKER_XPATH, "down", scrolls)
            except ValueError:
                logger.warning(f"Invalid month: {month}, using default")

            logger.info(f"✓ Selected month: {month}")
            time.sleep(0.5)
            return True

        except Exception as e:
            logger.error(f"✗ Error selecting month: {str(e)}")
            return False

    def select_year(self, year=2000, timeout=10):
        """
        Select year by scrolling

        Args:
            year: Year to select (e.g., 2000)
        """
        try:
            logger.info(f"Attempting to select year: {year}")

            # Wait for picker to be present
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.DOB_YEAR_PICKER_XPATH)
                )
            )

            # Assuming default is 1999, target is 2000
            current_year = 1999

            if year < current_year:
                scrolls = (current_year - year)
                self.scroll_picker(self.DOB_YEAR_PICKER_XPATH, "up", scrolls)
            elif year > current_year:
                scrolls = (year - current_year)
                self.scroll_picker(self.DOB_YEAR_PICKER_XPATH, "down", scrolls)

            logger.info(f"✓ Selected year: {year}")
            time.sleep(0.5)
            return True

        except Exception as e:
            logger.error(f"✗ Error selecting year: {str(e)}")
            return False

    def set_date_of_birth(self, date=9, month="Nov", year=2000):
        """
        Set complete date of birth

        Args:
            date: Date (1-31)
            month: Month name (Jan, Feb, etc.)
            year: Year (e.g., 2000)
        """
        try:
            logger.info(f"Setting date of birth: {date} {month} {year}")

            if not self.select_date(date):
                return False

            if not self.select_month(month):
                return False

            if not self.select_year(year):
                return False

            logger.info(f"✓ Date of birth set successfully: {date} {month} {year}")
            return True

        except Exception as e:
            logger.error(f"✗ Error setting date of birth: {str(e)}")
            return False

    def click_confirm_age(self, timeout=10):
        """Click Confirm Age button"""
        try:
            logger.info("Attempting to click Confirm Age button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONFIRM_AGE_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Confirm Age button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Confirm Age button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Confirm Age: {str(e)}")
            return False

    def verify_dob_screen(self):
        """Verify date of birth screen loaded successfully"""
        try:
            if self.is_dob_screen_visible(timeout=10):
                logger.info("✓ Onboarding screen 5 (Date of Birth) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 5 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying DOB screen: {str(e)}")
            return False

    # -----------------------Onboarding Screen 6 - Height Selection-----------------------#
    def is_height_screen_visible(self, timeout=10):
        """Check if height selection screen is visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.HEIGHT_PICKER_XPATH)
                )
            )
            logger.info("✓ Height selection screen is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Height selection screen not found")
            return False

    def scroll_height_picker(self, direction="down", scrolls=1):
        """
        Scroll height picker up or down

        Args:
            direction: "up" or "down"
            scrolls: Number of scroll actions
        """
        try:
            element = self.driver.find_element(AppiumBy.XPATH, self.HEIGHT_PICKER_XPATH)

            # Get element bounds
            location = element.location
            size = element.size

            start_x = location['x'] + size['width'] // 2
            start_y = location['y'] + size['height'] // 2

            # Scroll distance
            scroll_distance = size['height'] // 4

            for _ in range(scrolls):
                if direction == "down":
                    end_y = start_y + scroll_distance
                else:  # up
                    end_y = start_y - scroll_distance

                self.driver.swipe(start_x, start_y, start_x, end_y, duration=400)
                time.sleep(0.2)

            logger.info(f"✓ Scrolled height picker {direction} {scrolls} time(s)")
            return True

        except Exception as e:
            logger.error(f"✗ Error scrolling height picker: {str(e)}")
            return False

    def select_height(self, height=185, timeout=10):
        """
        Select height by scrolling

        Args:
            height: Height in cm (e.g., 185)
        """
        try:
            logger.info(f"Attempting to select height: {height} cm")

            # Wait for picker to be present
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.HEIGHT_PICKER_XPATH)
                )
            )

            # Assuming default/starting height is around 170 cm
            # Adjust this based on your app's default value
            default_height = 170

            if height < default_height:
                scrolls = (default_height - height)
                self.scroll_height_picker("up", scrolls)
            elif height > default_height:
                scrolls = (height - default_height)
                self.scroll_height_picker("down", scrolls)

            logger.info(f"✓ Selected height: {height} cm")
            time.sleep(0.5)
            return True

        except Exception as e:
            logger.error(f"✗ Error selecting height: {str(e)}")
            return False

    def click_confirm_height(self, timeout=10):
        """Click Confirm Height button"""
        try:
            logger.info("Attempting to click Confirm Height button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONFIRM_HEIGHT_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Confirm Height button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Confirm Height button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Confirm Height: {str(e)}")
            return False

    def verify_height_screen(self):
        """Verify height selection screen loaded successfully"""
        try:
            if self.is_height_screen_visible(timeout=10):
                logger.info("✓ Onboarding screen 6 (Height Selection) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 6 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying height screen: {str(e)}")
            return False

    # -----------------------Onboarding Screen 7 - Continue-----------------------#
    def is_screen_7_continue_visible(self, timeout=10):
        """Check if screen 7 continue button is visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.SCREEN_7_CONTINUE_BTN_XPATH)
                )
            )
            logger.info("✓ Screen 7 Continue button is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Screen 7 Continue button not found")
            return False

    def click_screen_7_continue(self, timeout=10):
        """Click Continue button on screen 7"""
        try:
            logger.info("Attempting to click Continue button (Screen 7)...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.SCREEN_7_CONTINUE_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Continue button (Screen 7)")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Continue button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Continue: {str(e)}")
            return False

    def verify_screen_7(self):
        """Verify screen 7 loaded successfully"""
        try:
            if self.is_screen_7_continue_visible(timeout=10):
                logger.info("✓ Onboarding screen 7 loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 7 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying screen 7: {str(e)}")
            return False

    # -----------------------Onboarding Screen 8 - Weight Selection-----------------------#
    def is_weight_screen_visible(self, timeout=10):
        """Check if weight selection screen is visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.WEIGHT_PICKER_XPATH)
                )
            )
            logger.info("✓ Weight selection screen is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Weight selection screen not found")
            return False

    def scroll_weight_picker(self, direction="right", scrolls=1):
        """
        Scroll weight picker left or right

        Args:
            direction: "left" or "right"
            scrolls: Number of scroll actions
        """
        try:
            element = self.driver.find_element(AppiumBy.XPATH, self.WEIGHT_PICKER_XPATH)

            # Get element bounds
            location = element.location
            size = element.size

            start_x = location['x'] + size['width'] // 2
            start_y = location['y'] + size['height'] // 2

            # Horizontal scroll distance
            scroll_distance = size['width'] // 4

            for _ in range(scrolls):
                if direction == "right":
                    end_x = start_x + scroll_distance
                else:  # left
                    end_x = start_x - scroll_distance

                self.driver.swipe(start_x, start_y, end_x, start_y, duration=400)
                time.sleep(0.2)

            logger.info(f"✓ Scrolled weight picker {direction} {scrolls} time(s)")
            return True

        except Exception as e:
            logger.error(f"✗ Error scrolling weight picker: {str(e)}")
            return False

    def select_weight(self, weight=70, timeout=10):
        """
        Select weight by scrolling horizontally

        Args:
            weight: Weight in kg (e.g., 70)
        """
        try:
            logger.info(f"Attempting to select weight: {weight} kg")

            # Wait for picker to be present
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.WEIGHT_PICKER_XPATH)
                )
            )

            # Assuming default/starting weight is around 70 kg
            # Adjust this based on your app's default value
            default_weight = 70

            if weight < default_weight:
                scrolls = (default_weight - weight)
                self.scroll_weight_picker("left", scrolls)
            elif weight > default_weight:
                scrolls = (weight - default_weight)
                self.scroll_weight_picker("right", scrolls)

            logger.info(f"✓ Selected weight: {weight} kg")
            time.sleep(0.5)
            return True

        except Exception as e:
            logger.error(f"✗ Error selecting weight: {str(e)}")
            return False

    def click_confirm_weight(self, timeout=10):
        """Click Confirm Weight button"""
        try:
            logger.info("Attempting to click Confirm Weight button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONFIRM_WEIGHT_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Confirm Weight button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Confirm Weight button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Confirm Weight: {str(e)}")
            return False

    def verify_weight_screen(self):
        """Verify weight selection screen loaded successfully"""
        try:
            if self.is_weight_screen_visible(timeout=10):
                logger.info("✓ Onboarding screen 8 (Weight Selection) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 8 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying weight screen: {str(e)}")
            return False

    # -----------------------Onboarding Screen 9 - Fitness Goal Selection-----------------------#
    def is_fitness_goal_screen_visible(self, timeout=10):
        """Check if fitness goal selection screen is visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.GOAL_LOSE_WEIGHT_XPATH)
                )
            )
            logger.info("✓ Fitness Goal selection screen is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Fitness Goal selection screen not found")
            return False

    def select_goal_lose_weight(self, timeout=10):
        """Select Lose Weight goal"""
        try:
            logger.info("Attempting to select 'Lose Weight' goal...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GOAL_LOSE_WEIGHT_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected 'Lose Weight' goal")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ 'Lose Weight' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting 'Lose Weight': {str(e)}")
            return False

    def select_goal_maintain_weight(self, timeout=10):
        """Select Maintain Weight goal"""
        try:
            logger.info("Attempting to select 'Maintain Weight' goal...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GOAL_MAINTAIN_WEIGHT_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected 'Maintain Weight' goal")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ 'Maintain Weight' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting 'Maintain Weight': {str(e)}")
            return False

    def select_goal_gain_weight(self, timeout=10):
        """Select Gain Weight goal"""
        try:
            logger.info("Attempting to select 'Gain Weight' goal...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GOAL_GAIN_WEIGHT_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected 'Gain Weight' goal")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ 'Gain Weight' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting 'Gain Weight': {str(e)}")
            return False

    def select_fitness_goal(self, goal="lose", timeout=10):
        """
        Select fitness goal based on parameter

        Args:
            goal: "lose", "maintain", or "gain"
        """
        try:
            logger.info(f"Selecting fitness goal: {goal}")

            if goal.lower() == "lose":
                return self.select_goal_lose_weight(timeout)
            elif goal.lower() == "maintain":
                return self.select_goal_maintain_weight(timeout)
            elif goal.lower() == "gain":
                return self.select_goal_gain_weight(timeout)
            else:
                logger.error(f"Invalid goal: {goal}. Use 'lose', 'maintain', or 'gain'")
                return False

        except Exception as e:
            logger.error(f"✗ Error selecting fitness goal: {str(e)}")
            return False

    def click_confirm_goal(self, timeout=10):
        """Click Confirm Goal button"""
        try:
            logger.info("Attempting to click Confirm Goal button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONFIRM_GOAL_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Confirm Goal button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Confirm Goal button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Confirm Goal: {str(e)}")
            return False


    def verify_fitness_goal_screen(self):
        """Verify fitness goal screen loaded successfully"""
        try:
            if self.is_fitness_goal_screen_visible(timeout=10):
                logger.info("✓ Onboarding screen 9 (Fitness Goal) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 9 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying fitness goal screen: {str(e)}")
            return False

    # -----------------------Onboarding Screen 10 - Target Weight-----------------------#
    def is_target_weight_screen_visible(self, timeout=10):
        """Check if target weight screen is visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.TARGET_WEIGHT_SCROLLABLE_XPATH)
                )
            )
            logger.info("✓ Target weight screen is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Target weight screen not found")
            return False

    def select_target_weight(self, swipe_count=3, direction="left"):
        """
        Select target weight by swiping on scrollable scale

        Args:
            swipe_count: Number of times to swipe (default: 3)
            direction: Swipe direction - 'left' to decrease, 'right' to increase weight
        """
        try:
            logger.info(f"Selecting target weight (Swipe {direction} {swipe_count} times)...")

            # Wait for scrollable element
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.TARGET_WEIGHT_SCROLLABLE_XPATH)
                )
            )

            # Get element location and size
            location = element.location
            size = element.size

            # Calculate swipe coordinates
            start_x = location['x'] + (size['width'] * 0.7)  # Start from 70%
            end_x = location['x'] + (size['width'] * 0.3)  # End at 30%
            y = location['y'] + (size['height'] / 2)  # Middle height

            # Reverse coordinates for right swipe
            if direction == "right":
                start_x, end_x = end_x, start_x

            # Perform swipes
            for i in range(swipe_count):
                self.driver.swipe(start_x, y, end_x, y, duration=500)
                logger.info(f"✓ Swipe {i + 1}/{swipe_count} completed ({direction})")
                time.sleep(0.5)

            logger.info(f"✓ Target weight selection completed")
            time.sleep(1)
            return True

        except Exception as e:
            logger.error(f"✗ Error selecting target weight: {str(e)}")
            return False

    def click_confirm_target(self, timeout=10):
        """Click Confirm Target button"""
        try:
            logger.info("Attempting to click Confirm Target button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONFIRM_TARGET_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Confirm Target button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Confirm Target button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Confirm Target: {str(e)}")
            return False

    def verify_target_weight_screen(self):
        """Verify target weight screen loaded successfully"""
        try:
            if self.is_target_weight_screen_visible(timeout=10):
                logger.info("✓ Onboarding screen 10 (Target Weight) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 10 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying target weight screen: {str(e)}")
            return False

    # -----------------------Onboarding Screen 10 - Activity Level Selection-----------------------#
    def is_activity_screen_visible(self, timeout=10):
        """Check if activity level selection screen is visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.ACTIVITY_NOT_VERY_ACTIVE_XPATH)
                )
            )
            logger.info("✓ Activity Level selection screen is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Activity Level selection screen not found")
            return False

    def select_activity_not_very_active(self, timeout=10):
        """Select Not Very Active option"""
        try:
            logger.info("Attempting to select 'Not Very Active' option...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.ACTIVITY_NOT_VERY_ACTIVE_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected 'Not Very Active'")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ 'Not Very Active' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting 'Not Very Active': {str(e)}")
            return False

    def select_activity_lightly_active(self, timeout=10):
        """Select Lightly Active option"""
        try:
            logger.info("Attempting to select 'Lightly Active' option...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.ACTIVITY_LIGHTLY_ACTIVE_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected 'Lightly Active'")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ 'Lightly Active' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting 'Lightly Active': {str(e)}")
            return False

    def select_activity_active(self, timeout=10):
        """Select Active option"""
        try:
            logger.info("Attempting to select 'Active' option...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.ACTIVITY_ACTIVE_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected 'Active'")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ 'Active' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting 'Active': {str(e)}")
            return False

    def select_activity_very_active(self, timeout=10):
        """Select Very Active option"""
        try:
            logger.info("Attempting to select 'Very Active' option...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.ACTIVITY_VERY_ACTIVE_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected 'Very Active'")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ 'Very Active' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting 'Very Active': {str(e)}")
            return False

    def select_activity_level(self, level="lightly_active", timeout=10):
        """
        Select activity level based on parameter

        Args:
            level: "not_very_active", "lightly_active", "active", or "very_active"
        """
        try:
            logger.info(f"Selecting activity level: {level}")

            level_lower = level.lower().replace(" ", "_")

            if level_lower == "not_very_active":
                return self.select_activity_not_very_active(timeout)
            elif level_lower == "lightly_active":
                return self.select_activity_lightly_active(timeout)
            elif level_lower == "active":
                return self.select_activity_active(timeout)
            elif level_lower == "very_active":
                return self.select_activity_very_active(timeout)
            else:
                logger.error(f"Invalid activity level: {level}")
                logger.error("Use: 'not_very_active', 'lightly_active', 'active', or 'very_active'")
                return False

        except Exception as e:
            logger.error(f"✗ Error selecting activity level: {str(e)}")
            return False

    def click_confirm_activity(self, timeout=10):
        """Click Confirm Activity button"""
        try:
            logger.info("Attempting to click Confirm Activity button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONFIRM_ACTIVITY_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Confirm Activity button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Confirm Activity button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Confirm Activity: {str(e)}")
            return False

    def verify_activity_screen(self):
        """Verify activity level screen loaded successfully"""
        try:
            if self.is_activity_screen_visible(timeout=10):
                logger.info("✓ Onboarding screen 10 (Activity Level) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 10 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying activity screen: {str(e)}")
            return False

    def is_meals_screen_visible(self, timeout=10):
        """Check if meals per day screen is visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.MEALS_3_PER_DAY_XPATH)
                )
            )
            logger.info("✓ Meals per day screen is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Meals per day screen not found")
            return False

    def select_meals_per_day(self, meals=3, timeout=10):
        """
        Select number of meals per day

        Args:
            meals: Number of meals (2, 3, 4, or 5)
        """
        try:
            logger.info(f"Selecting {meals} meals per day...")

            # Map meals to XPath
            meals_xpath_map = {
                2: self.MEALS_2_PER_DAY_XPATH,
                3: self.MEALS_3_PER_DAY_XPATH,
                4: self.MEALS_4_PER_DAY_XPATH,
                5: self.MEALS_5_PER_DAY_XPATH
            }

            if meals not in meals_xpath_map:
                logger.error(f"✗ Invalid meals count: {meals}. Must be 2, 3, 4, or 5")
                return False

            xpath = meals_xpath_map[meals]

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, xpath)
                )
            )

            element.click()
            logger.info(f"✓ Successfully selected {meals} meals per day")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ Meals option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting meals: {str(e)}")
            return False

    def click_confirm_preference(self, timeout=10):
        """Click Confirm Preference button"""
        try:
            logger.info("Attempting to click Confirm Preference button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONFIRM_PREFERENCE_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Confirm Preference button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Confirm Preference button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Confirm Preference: {str(e)}")
            return False

    def verify_meals_screen(self):
        """Verify meals per day screen loaded successfully"""
        try:
            if self.is_meals_screen_visible(timeout=10):
                logger.info("✓ Onboarding screen 12 (Meals Per Day) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 12 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying meals screen: {str(e)}")
            return False

    # -----------------------Onboarding Screen 12 - Medical Condition Selection-----------------------#
    def is_medical_condition_screen_visible(self, timeout=10):
        """Check if medical condition screen is visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.MEDICAL_NONE_XPATH)
                )
            )
            logger.info("✓ Medical condition screen is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Medical condition screen not found")
            return False

    def select_medical_none(self, timeout=10):
        """Select None (no medical condition)"""
        try:
            logger.info("Attempting to select 'None' medical condition...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.MEDICAL_NONE_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected 'None'")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ 'None' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting 'None': {str(e)}")
            return False

    def select_medical_condition_by_text(self, condition_text, timeout=10):
        """
        Select medical condition by text (works for scrollable content)

        Args:
            condition_text: Text of the condition (e.g., "Diabetes", "PCOS")
        """
        try:
            logger.info(f"Attempting to select medical condition: {condition_text}")

            # Use UiAutomator to find and click element by text
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR,
                     f'new UiSelector().text("{condition_text}")')
                )
            )

            element.click()
            logger.info(f"✓ Successfully selected '{condition_text}'")
            time.sleep(0.5)
            return True

        except TimeoutException:
            logger.warning(f"✗ '{condition_text}' not visible, attempting to scroll...")
            # Try scrolling to find the element
            return self.scroll_and_select_medical_condition(condition_text)
        except Exception as e:
            logger.error(f"✗ Error selecting '{condition_text}': {str(e)}")
            return False

    def scroll_and_select_medical_condition(self, condition_text, max_scrolls=5):
        """
        Scroll down to find and select medical condition

        Args:
            condition_text: Text of the condition to find
            max_scrolls: Maximum number of scroll attempts
        """
        try:
            logger.info(f"Scrolling to find: {condition_text}")

            for scroll_attempt in range(max_scrolls):
                # Check if element is now visible
                try:
                    element = self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiSelector().text("{condition_text}")'
                    )
                    element.click()
                    logger.info(f"✓ Found and selected '{condition_text}' after {scroll_attempt} scrolls")
                    time.sleep(0.5)
                    return True
                except:
                    # Element not found, scroll down
                    logger.info(f"Scroll attempt {scroll_attempt + 1}/{max_scrolls}")
                    self.scroll_medical_conditions_down()

            logger.error(f"✗ Could not find '{condition_text}' after {max_scrolls} scrolls")
            return False

        except Exception as e:
            logger.error(f"✗ Error scrolling for medical condition: {str(e)}")
            return False

    def scroll_medical_conditions_down(self):
        """Scroll down on medical conditions screen"""
        try:
            # Get screen dimensions
            size = self.driver.get_window_size()

            # Calculate scroll coordinates (middle of screen, swipe from 70% to 30%)
            start_x = size['width'] // 2
            start_y = int(size['height'] * 0.7)
            end_y = int(size['height'] * 0.3)

            # Perform swipe
            self.driver.swipe(start_x, start_y, start_x, end_y, duration=500)
            time.sleep(0.5)
            logger.info("✓ Scrolled down on medical conditions screen")
            return True

        except Exception as e:
            logger.error(f"✗ Error scrolling: {str(e)}")
            return False

    def select_medical_diabetes(self):
        """Select Diabetes condition"""
        return self.select_medical_condition_by_text(self.MEDICAL_DIABETES_TEXT)

    def select_medical_pre_diabetes(self):
        """Select Pre-Diabetes condition"""
        return self.select_medical_condition_by_text(self.MEDICAL_PRE_DIABETES_TEXT)

    def select_medical_cholesterol(self):
        """Select Cholesterol condition"""
        return self.select_medical_condition_by_text(self.MEDICAL_CHOLESTEROL_TEXT)

    def select_medical_hypertension(self):
        """Select Hypertension condition"""
        return self.select_medical_condition_by_text(self.MEDICAL_HYPERTENSION_TEXT)

    def select_medical_pcos(self):
        """Select PCOS condition"""
        return self.select_medical_condition_by_text(self.MEDICAL_PCOS_TEXT)

    def select_medical_thyroid(self):
        """Select Thyroid condition"""
        return self.select_medical_condition_by_text(self.MEDICAL_THYROID_TEXT)

    def select_medical_physical_injury(self):
        """Select Physical Injury condition"""
        return self.select_medical_condition_by_text(self.MEDICAL_PHYSICAL_INJURY_TEXT)

    def select_multiple_medical_conditions(self, conditions_list):
        """
        Select multiple medical conditions

        Args:
            conditions_list: List of condition texts (e.g., ["Diabetes", "PCOS"])
        """
        try:
            logger.info(f"Selecting multiple conditions: {conditions_list}")

            for condition in conditions_list:
                if not self.select_medical_condition_by_text(condition):
                    logger.warning(f"Failed to select: {condition}")
                    return False

            logger.info(f"✓ Successfully selected all conditions: {conditions_list}")
            return True

        except Exception as e:
            logger.error(f"✗ Error selecting multiple conditions: {str(e)}")
            return False

    def click_confirm_condition(self, timeout=10):
        """Click Confirm Condition button"""
        try:
            logger.info("Attempting to click Confirm Condition button...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.CONFIRM_CONDITION_BTN_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully clicked Confirm Condition button")

            time.sleep(SCREEN_TRANSITION_DELAY)
            return True

        except TimeoutException:
            logger.error(f"✗ Confirm Condition button not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error clicking Confirm Condition: {str(e)}")
            return False

    def verify_medical_condition_screen(self):
        """Verify medical condition screen loaded successfully"""
        try:
            if self.is_medical_condition_screen_visible(timeout=10):
                logger.info("✓ Onboarding screen 12 (Medical Condition) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 12 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying medical condition screen: {str(e)}")
            return False

    # -----------------------Onboarding Screen 13 - Goal Achievement Rate-----------------------#
    def is_goal_rate_screen_visible(self, timeout=10):
        """Check if goal achievement rate screen is visible"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, self.GOAL_RATE_0_2_KG_XPATH)
                )
            )
            logger.info("✓ Goal achievement rate screen is visible")
            return True
        except TimeoutException:
            logger.warning("✗ Goal achievement rate screen not found")
            return False

    def select_goal_rate_0_2_kg(self, timeout=10):
        """Select 0.2 Kg/Week rate"""
        try:
            logger.info("Attempting to select '0.2 Kg/Week' goal rate...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GOAL_RATE_0_2_KG_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected '0.2 Kg/Week'")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ '0.2 Kg/Week' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting '0.2 Kg/Week': {str(e)}")
            return False

    def select_goal_rate_0_4_kg(self, timeout=10):
        """Select 0.4 Kg/Week rate"""
        try:
            logger.info("Attempting to select '0.4 Kg/Week' goal rate...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GOAL_RATE_0_4_KG_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected '0.4 Kg/Week'")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ '0.4 Kg/Week' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting '0.4 Kg/Week': {str(e)}")
            return False

    def select_goal_rate_0_6_kg(self, timeout=10):
        """Select 0.6 Kg/Week rate"""
        try:
            logger.info("Attempting to select '0.6 Kg/Week' goal rate...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GOAL_RATE_0_6_KG_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected '0.6 Kg/Week'")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ '0.6 Kg/Week' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting '0.6 Kg/Week': {str(e)}")
            return False

    def select_goal_rate_0_8_kg(self, timeout=10):
        """Select 0.8 Kg/Week rate"""
        try:
            logger.info("Attempting to select '0.8 Kg/Week' goal rate...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GOAL_RATE_0_8_KG_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected '0.8 Kg/Week'")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ '0.8 Kg/Week' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting '0.8 Kg/Week': {str(e)}")
            return False

    def select_goal_rate_10_0_kg(self, timeout=10):
        """Select 10.0 Kg/Week rate"""
        try:
            logger.info("Attempting to select '10.0 Kg/Week' goal rate...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GOAL_RATE_10_0_KG_XPATH)
                )
            )

            element.click()
            logger.info("✓ Successfully selected '10.0 Kg/Week'")
            time.sleep(1)
            return True

        except TimeoutException:
            logger.error(f"✗ '10.0 Kg/Week' option not clickable within {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"✗ Error selecting '10.0 Kg/Week': {str(e)}")
            return False

    def select_goal_achievement_rate(self, rate=0.4, timeout=10):
        """
        Select goal achievement rate based on kg/week value

        Args:
            rate: Weight loss rate in kg/week (0.2, 0.4, 0.6, 0.8, or 10.0)
        """
        try:
            logger.info(f"Selecting goal achievement rate: {rate} Kg/Week")

            if rate == 0.2:
                return self.select_goal_rate_0_2_kg(timeout)
            elif rate == 0.4:
                return self.select_goal_rate_0_4_kg(timeout)
            elif rate == 0.6:
                return self.select_goal_rate_0_6_kg(timeout)
            elif rate == 0.8:
                return self.select_goal_rate_0_8_kg(timeout)
            elif rate == 10.0:
                return self.select_goal_rate_10_0_kg(timeout)
            else:
                logger.error(f"Invalid rate: {rate}. Use 0.2, 0.4, 0.6, 0.8, or 10.0")
                return False

        except Exception as e:
            logger.error(f"✗ Error selecting goal achievement rate: {str(e)}")
            return False

    def click_goal_rate_continue(self, timeout=10):
        """Click Continue button on goal rate screen"""
        try:
            logger.info("Attempting to click Continue button (Goal Rate)...")

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (AppiumBy.XPATH, self.GOAL_RATE_CONTINUE_BTN_XPATH)
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

    def verify_goal_rate_screen(self):
        """Verify goal achievement rate screen loaded successfully"""
        try:
            if self.is_goal_rate_screen_visible(timeout=10):
                logger.info("✓ Onboarding screen 13 (Goal Achievement Rate) loaded successfully")
                return True
            else:
                logger.error("✗ Onboarding screen 13 not loaded")
                return False
        except Exception as e:
            logger.error(f"✗ Error verifying goal rate screen: {str(e)}")
            return False

    # -----------------------Complete Flow-----------------------#
    def complete_onboarding_flow(self):
        """Complete onboarding flow from splash to Get Started"""
        try:
            # Step 1: Handle splash screen
            logger.info("────── Starting Onboarding Flow ──────")
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

            # Step 5 Select Gender and Confirm Identity
            if not self.verify_gender_screen():
                logger.error("Failed to verify gender screen 4")
                return False

            if not self.select_gender_male():
                logger.error("Failed to select gender male")
                return False

            if not self.click_confirm_identity():
                logger.error("Failed to click confirm identity")
                return False

            # Step 6: Set date of birth and confirm
            if not self.verify_dob_screen():
                logger.error("Failed to load onboarding screen 5 (Date of Birth)")
                return False

            if not self.set_date_of_birth(date=9, month="Nov", year=2000):
                logger.error("Failed to set date of birth")
                return False

            if not self.click_confirm_age():
                logger.error("Failed to click Confirm Age")
                return False

            # Step 7: Select height and confirm
            if not self.verify_height_screen():
                logger.error("Failed to load onboarding screen 6 (Height Selection)")
                return False

            if not self.select_height(height=185):
                logger.error("Failed to select height")
                return False

            if not self.click_confirm_height():
                logger.error("Failed to click Confirm Height")
                return False

            # Step 8: Click continue on screen 7
            if not self.verify_screen_7():
                logger.error("Failed to load onboarding screen 7")
                return False

            if not self.click_screen_7_continue():
                logger.error("Failed to click Continue on screen 7")
                return False

            # Step 9: Select weight and confirm
            if not self.verify_weight_screen():
                logger.error("Failed to load onboarding screen 8 (Weight Selection)")
                return False

            if not self.select_weight(weight=70):
                logger.error("Failed to select weight")
                return False

            if not self.click_confirm_weight():
                logger.error("Failed to click Confirm Weight")
                return False

            # Step 10: Select fitness goal and confirm
            if not self.verify_fitness_goal_screen():
                logger.error("Failed to load onboarding screen 9 (Fitness Goal)")
                return False

            if not self.select_fitness_goal(goal="lose"):  # or "maintain" or "gain"
                logger.error("Failed to select fitness goal")
                return False

            if not self.click_confirm_goal():
                logger.error("Failed to click Confirm Goal")
                return False

            # Step 10.5: Select target weight and confirm
            if not self.verify_target_weight_screen():
                logger.error("Failed to load onboarding screen 10 (Target Weight)")
                return False

            if not self.select_target_weight(swipe_count=5, direction="left"):
                logger.error("Failed to select target weight")
                return False

            if not self.click_confirm_target():
                logger.error("Failed to click Confirm Target")
                return False

            # Step 11.5: Select meals per day and confirm preference
            if not self.verify_meals_screen():
                logger.error("Failed to load onboarding screen 12 (Meals Per Day)")
                return False

            if not self.select_meals_per_day(meals=3):  # Ya 2, 4, 5
                logger.error("Failed to select meals per day")
                return False

            if not self.click_confirm_preference():
                logger.error("Failed to click Confirm Preference")
                return False

            # Step 11: Select medical condition and confirm
            if not self.verify_medical_condition_screen():
                logger.error("Failed to load onboarding screen 12 (Medical Condition)")
                return False

            if not self.select_medical_none():
                logger.error("Failed to select medical condition")
                return False

            # OR Option 2: Select specific conditions
            # if not self.select_medical_diabetes():
            #     logger.error("Failed to select Diabetes")
            #     return False

            # OR Option 3: Select multiple conditions
            # if not self.select_multiple_medical_conditions(["Diabetes", "PCOS"]):
            #     logger.error("Failed to select medical conditions")
            #     return False

            if not self.click_confirm_condition():
                logger.error("Failed to click Confirm Condition")
                return False

            # Step 12: Select goal achievement rate and continue
            if not self.verify_goal_rate_screen():
                logger.error("Failed to load onboarding screen 13 (Goal Achievement Rate)")
                return False

            if not self.select_goal_achievement_rate(rate=0.4):
                logger.error("Failed to select goal achievement rate")
                return False

            if not self.click_goal_rate_continue():
                logger.error("Failed to click Continue on goal rate screen")
                return False

            logger.info("────── Onboarding Flow Completed Successfully ──────")
            return True

        except Exception as e:
            logger.error(f"✗ Error in onboarding flow: {str(e)}")
            return False