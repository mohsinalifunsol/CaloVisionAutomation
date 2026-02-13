from core.driver_manager import start_driver, quit_driver
from core.ob_flow_first_session import OBFlowsFirstSession
from utils.logger import setup_logger

logger = setup_logger(__name__)


def launch_app():
    """Launch the app and handle all onboarding screens.

    Returns:
        WebDriver instance ready for testing
    """
    logger.info("Starting app launch sequence...")

    try:
        driver = start_driver()
        logger.info("✓ Driver initialized successfully")

        onboarding = OBFlowsFirstSession(driver)

        # Flow complete hone ka verification
        if onboarding.complete_onboarding_flow():
            logger.info("✓ App launch sequence completed successfully")
            return driver
        else:
            logger.error("✗ Onboarding flow failed")
            quit_driver(driver)
            return None

    except Exception as e:
        logger.error(f"✗ Error during app launch: {str(e)}")
        if 'driver' in locals():
            quit_driver(driver)
        raise


if __name__ == '__main__':
    driver = None
    try:
        driver = launch_app()

        if driver:
            logger.info("App launched successfully. Keeping it open for 5 seconds...")
            import time

            time.sleep(5)
        else:
            logger.error("Driver is None, app launch failed")

    except Exception as e:
        logger.error(f"Failed to launch app: {str(e)}")
    finally:
        if driver:
            logger.info("Closing driver...")
            quit_driver(driver)