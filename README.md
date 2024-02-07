# Anime Downloader

## Description
This Python script automates the process of downloading episodes from [anime-sama.fr](https://anime-sama.fr/). It uses the Selenium library to interact with the website and PyAutoGUI to simulate mouse clicks. The script is designed for the Firefox browser and supports the Mint Linux distribution with a screen resolution of 1920x1080.

## Usage
1. Ensure you have Python 3.x installed.
2. Install the required Python libraries:
   ```bash
   sudo apt install python3-pip
   sudo dnf install python3-pip
   pip3 install selenium pyautogui clipboard json
   ```
3. Download the [Firefox browser](https://www.mozilla.org/en-US/firefox/new/).
4. Install Adblock and XDM browser extensions:
   - Adblock: [Adblock](https://addons.mozilla.org/en-US/firefox/addon/adblock-for-firefox/)
   - XDM: [Xtreme Download Manager](https://addons.mozilla.org/en-US/firefox/addon/xdm-helper/)

5. Clone the repository and navigate to the project directory.
6. Download the Adblock and XDM XPI files and place them in the project directory.
7. Create a `db.json` file with the necessary coordinates for your Linux distribution and screen resolution.
   ```json
   {
     "mint": {
       "1920x1080": {
         "accept-cookies": {"x": 100, "y": 200},
         "serv-list": {"x": 150, "y": 250},
         "serv1": {"x": 200, "y": 300},
         "serv2": {"x": 250, "y": 350},
         "serv3": {"x": 300, "y": 400},
         "serv4": {"x": 350, "y": 450},
         "next-ep": {"x": 400, "y": 500},
         // Add more coordinates as needed
       }
     }
   }
   ```
8. Run the script:
   ```bash
   python anime_downloader.py
   ```
9. Follow the prompts to enter the anime link, server number, and the number of episodes to download.

## Disclaimer
This script is for educational purposes only. Make sure to comply with the terms of service of the website you are scraping.

Feel free to customize the script and coordinates according to your needs. Happy anime downloading!
