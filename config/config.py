"""Configuration settings for the automation framework."""
import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
APK_DIR = BASE_DIR / "CaloVision-debug.apk"

# Appium Server Configuration
APPIUM_SERVER_URL = "http://127.0.0.1:4723"

# App Configuration
APP_PATH = str(APK_DIR) if APK_DIR.exists() else r"C:\Users\Mohsin Ali\Documents\Apk\CaloVision-1.0.7.apk"
PLATFORM_NAME = "Android"
AUTOMATION_NAME = "UiAutomator2"

# Wait Configuration
DEFAULT_TIMEOUT = 15
SHORT_TIMEOUT = 8
LONG_TIMEOUT = 30
IMPLICIT_WAIT = 10

# Screen Transition Delays (in seconds)
SPLASH_SCREEN_MIN_WAIT = 4  # Minimum wait for splash screen
SCREEN_TRANSITION_DELAY = 2  # Delay between screen transitions
ELEMENT_INTERACTION_DELAY = 1  # Delay after element interactions

# Screenshot Configuration
SCREENSHOT_DIR = BASE_DIR / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

# Logging Configuration
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_LEVEL = "INFO"