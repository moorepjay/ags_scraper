"""
Program navigates to bijiaqi.com and scrapes current gold sell orders for Lost Ark and New World online games.
Data is formatted and displayed in web-based dashboard.
This file handles web interactivity and data collection via webdriver
"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import constants
import pandas as pd
import time

# TODO: Duplicate code for each of our scrapers.
def get_data(lost_ark_server_list, new_world_server_list):
    # Set selenium options
    options = Options()
    options.add_argument('disable-infobars')
    options.add_argument('--incognito')
    options.add_argument("start-maximized")

    # Start selenium browser
    service = Service(constants.LOCAL_WEBDRIVER)
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(constants.TARGET_SITE)

    # Page load
    time.sleep(5)

    for server in lost_ark_server_list:
        server_string = server.split('-')
        server_name = server_string[0]
        server_region = server_string[1].replace(' ', '_')
        output_path = "{0}{1}_{2}.csv".format(constants.LA_SOURCE_FOLDER, server_name, server_region)

        # Get and select input box and enter server name from list
        search_box = browser.find_element(By.XPATH, '//*[@id="speedhostname"]')
        search_box.send_keys(Keys.CONTROL, 'a')
        search_box.send_keys(Keys.BACKSPACE)
        search_box.send_keys(server)

        # Page load
        time.sleep(5)

        # Scrape seller table
        html = browser.page_source
        tables = pd.read_html(html)
        seller_table = tables[10]

        seller_table.to_csv(output_path)

        log_entry = "{} has been scraped for prices and saved to: {}".format(server, output_path)
        print("({0}) {1}".format(datetime.utcnow(), log_entry))

    for server in new_world_server_list:
        server_string = server.split('-')
        server_name = server_string[0]
        server_region = server_string[1].replace(' ', '_')

        output_path = "{0}{1}_{2}.csv".format(constants.NW_SOURCE_FOLDER, server_name, server_region)

        # Get and select input box and enter server name from list
        search_box = browser.find_element(By.XPATH, '//*[@id="speedhostname"]')
        search_box.send_keys(Keys.CONTROL, 'a')
        search_box.send_keys(Keys.BACKSPACE)
        search_box.send_keys(server)

        # Page load
        time.sleep(5)

        # Scrape seller table
        html = browser.page_source
        tables = pd.read_html(html)
        seller_table = tables[10]

        seller_table.to_csv(output_path)

        log_entry = "{} has been scraped for prices and saved to: {}".format(server, output_path)
        print("({0}) {1}".format(datetime.utcnow(), log_entry))

    browser.quit()




