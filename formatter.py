import glob
import os
import re
import pandas as pd
from datetime import datetime
import constants
from constants import SOURCE_FOLDER, CLEANED_SOURCE_FOLDER


def clean_folders():
    for game_folder, dirs, files in os.walk(SOURCE_FOLDER):
        print("Cleaning folders!")
        for source_file in files:
            # Get server/region info, output_path, from filename.
            filename = source_file.split('_', maxsplit=1)
            print("Cleaning: {}".format(source_file))
            server = filename[0]
            region = filename[1].split('.')[0]

            dt = datetime.now()

            # Get game folder from folder name.
            # TODO: keep an eye on regex errors.
            game_folder_regex = re.compile(r'\w+$')
            game_name = game_folder_regex.search(game_folder)
            game_name = game_name.group()

            # Create output path for cleaned file.
            output_path = "{0}\\{1}\\{2}_{3}_Clean.csv".format(CLEANED_SOURCE_FOLDER, game_name, server, region)

            # Read source file into a dataframe.
            source_file = pd.read_csv("{0}\\{1}".format(game_folder, source_file))

            # Rename columns
            source_file["Seller"] = source_file["0"]
            source_file["Price"] = source_file["5"]

            # Create new dataframe, removing copied columns
            sell_orders = source_file[['Seller', "Price"]].copy()
            sell_orders = sell_orders.drop(0, axis=0)
            sell_orders = sell_orders.drop(1, axis=0)

            # Drop any rows that do not hold numerical price values
            sell_orders.drop(sell_orders[sell_orders['Price'].str.get(1) != '.'].index, inplace=True)

            # Parse seller name
            sell_orders['Seller'] = sell_orders['Seller'].apply(lambda x: x.split('(')[0])

            # Parse numerical price value and convert to float
            sell_orders['Price'] = sell_orders['Price'].str[:-4].astype(float)

            # Add new column for price in USD
            # 1 chinese yuan equals 0.1433 USD https://www.currency.me.uk/convert/cny/usd
            sell_orders['USD'] = sell_orders['Price'] * 0.1434

            # Add new column for today's date (time)
            sell_orders['Date'] = dt

            # Add new server/region columns
            sell_orders['Server'] = server
            sell_orders['Region'] = region

            sell_orders.Date = pd.to_datetime(sell_orders.Date)

            # Reorder columns for cleaned output
            output = sell_orders[['Date', 'Region', 'Server', 'Seller', 'Price', 'USD']]

            # Always overwrite previous cleaned file.
            output.to_csv(output_path, header=True, index=False)

            log_entry = "{} has been formatted and saved to: {}".format(server, output_path)
            print("({0}) {1}".format(datetime.utcnow(), log_entry))
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def update_clean_master_files():
    new_world_files = glob.glob("{0}*.csv".format(constants.NEW_WORLD_CLEANED_FOLDER))
    lost_ark_files = glob.glob("{0}*.csv".format(constants.LOST_ARK_CLEANED_FOLDER))

    for file in new_world_files:
        df = pd.read_csv(file)
        if not os.path.isfile(constants.NEW_WORLD_CLEANED_MASTER_FILE):
            df.to_csv(constants.NEW_WORLD_CLEANED_MASTER_FILE, header=True, index=False)
            print("Created new master file!!!!")
        else:
            df.to_csv(constants.NEW_WORLD_CLEANED_MASTER_FILE, mode='a', header=False, index=False)
            print("Appended to master file....")
        # df.to_csv(constants.LOST_ARK_CLEANED_MASTER_FILE, header=True, index=False)


    for file in lost_ark_files:
        df = pd.read_csv(file)
        if not os.path.isfile(constants.LOST_ARK_CLEANED_MASTER_FILE):
            df.to_csv(constants.LOST_ARK_CLEANED_MASTER_FILE, header=True, index=False)
            print("Created new master file!!!!")
        else:
            df.to_csv(constants.LOST_ARK_CLEANED_MASTER_FILE, mode='a', header=False, index=False)
            print("Appended to master file....")
        # df.to_csv(constants.LOST_ARK_CLEANED_MASTER_FILE, header=True, index=False)
