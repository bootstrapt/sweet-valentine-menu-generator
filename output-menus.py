from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import argparse

MENUS = ['menu-left', 'menu-right']
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# TCL 58S470G (58" S Class) native panel resolution: 4K UHD
OUTPUT_RESOLUTION = (3840, 2160)
# The HTML/CSS layouts are designed for a 1920x1080 viewport
LAYOUT_RESOLUTION = (1920, 1080)


def take_screenshot(html_file_path, output_file_path, output_resolution=OUTPUT_RESOLUTION,
                    shrink=1.0, stretch_bg=False):
    """Render the page and save a PNG at exactly output_resolution pixels.

    The page is laid out in a CSS viewport of LAYOUT_RESOLUTION / shrink and then
    scaled up so the final image is output_resolution. shrink < 1.0 gives the
    layout more room, so everything appears smaller.
    """
    css_width = round(LAYOUT_RESOLUTION[0] / shrink)
    css_height = round(LAYOUT_RESOLUTION[1] / shrink)
    scale = output_resolution[0] / css_width

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # headless so the window isn't limited by the Mac's screen
    chrome_options.add_argument("--hide-scrollbars")
    chrome_options.add_argument(f"--window-size={css_width},{css_height}")

    # Selenium Manager (built into selenium>=4.6) finds/downloads the matching chromedriver
    driver = webdriver.Chrome(options=chrome_options)
    try:
        # Force exact viewport size and pixel density regardless of the host display
        driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
            "width": css_width,
            "height": css_height,
            "deviceScaleFactor": scale,
            "mobile": False,
        })

        driver.get("file://" + html_file_path)

        if stretch_bg:
            driver.execute_script("document.body.style.backgroundSize = '100% 100%';")

        # Wait for the page (fonts, images) to load
        time.sleep(2)

        driver.save_screenshot(output_file_path)
    finally:
        driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate menu screenshots')
    parser.add_argument('--stretch-bg', action='store_true',
                        help='Stretch background image to fill viewport (sets background-size: 100%% 100%%)')
    parser.add_argument('--shrink-right', type=float, default=1.0,
                        help='Shrink menu-right content by a factor (e.g., 0.9 for 90%% size)')
    parser.add_argument('--shrink-left', type=float, default=1.0,
                        help='Shrink menu-left content by a factor (e.g., 0.85 for 85%% size)')
    parser.add_argument('--menu', choices=MENUS,
                        help='Generate only specific menu')

    args = parser.parse_args()

    menus_to_generate = [args.menu] if args.menu else MENUS

    for menu in menus_to_generate:
        shrink = args.shrink_left if menu == "menu-left" else args.shrink_right
        take_screenshot(f"{DIR_PATH}/html/{menu}.html", f"{DIR_PATH}/output-menus/{menu}.png",
                        shrink=shrink, stretch_bg=args.stretch_bg)

    print(f"Screenshots generated for: {', '.join(menus_to_generate)} "
          f"at {OUTPUT_RESOLUTION[0]}x{OUTPUT_RESOLUTION[1]}")
