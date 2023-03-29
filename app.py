"""
Program navigates to bijiaqi.com and scrapes current gold sell orders for Lost Ark and New World online games.
Data is formatted and displayed in web-based dashboard.
This file handles web interactivity and data collection via webdriver.
"""
import os
import formatter
import database
import scraper
import constants

# If project folders don't exist create them.
if not os.path.isdir(constants.SOURCE_FOLDER):
    # Create folders
    os.mkdir(constants.SOURCE_FOLDER)
    os.mkdir(constants.CLEANED_SOURCE_FOLDER)
else:
    # If there are folders continue.
    # Scrape price data from target site for both games.
    scraper.get_data(constants.LOST_ARK_SERVER_LIST, constants.NEW_WORLD_SERVER_LIST)

    # Format scraped data for dashboard.
    formatter.clean_folders()

    # If there isn't a master file continue.
    if not os.path.isfile(constants.NEW_WORLD_CLEANED_MASTER_FILE):
        # Aggregate cleaned documents into master for each game.
        formatter.update_clean_master_files()
    else:
        # If there is a master we assume both exist and delete.
        os.remove(constants.NEW_WORLD_CLEANED_MASTER_FILE)
        os.remove(constants.LOST_ARK_CLEANED_MASTER_FILE)
        formatter.update_clean_master_files()

    # Aggregate cleaned documents into master for each game.
    formatter.update_clean_master_files()

    # Dump our new documents in mongodb.
    database.upload_csv_to_mongo('PROD')


