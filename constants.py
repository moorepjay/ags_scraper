import os


TARGET_SITE = 'https://www.bijiaqi.com/'
LOCAL_WEBDRIVER = '<Directory_For_Your_ChomeDriver>/chromedriver.exe'
CONNECTION_STRING = "mongodb+srv://user:password@server.at.mongodb.net/?retryWrites=true&w=majority"
PROD_DB = "PROD"

# Relative paths.
PROJECT_ROOT_PATH = os.path.dirname(__file__)
SOURCE_FOLDER = "{0}\\source\\".format(PROJECT_ROOT_PATH)
LA_SOURCE_FOLDER = "{0}\\source\\lost_ark\\".format(PROJECT_ROOT_PATH)
NW_SOURCE_FOLDER = "{0}\\source\\new_world\\".format(PROJECT_ROOT_PATH)
CLEANED_SOURCE_FOLDER = "{0}\\cleaned_source\\".format(PROJECT_ROOT_PATH)
NEW_WORLD_CLEANED_FOLDER = "{0}new_world\\".format(CLEANED_SOURCE_FOLDER)
LOST_ARK_CLEANED_FOLDER = "{0}lost_ark\\".format(CLEANED_SOURCE_FOLDER)
NEW_WORLD_CLEANED_MASTER_FILE = "{0}new_world\\master.csv".format(CLEANED_SOURCE_FOLDER)
LOST_ARK_CLEANED_MASTER_FILE = "{0}lost_ark\\master.csv".format(CLEANED_SOURCE_FOLDER)

NEW_WORLD_SERVER_LIST = [
    "Aaru-EU Central",
    "Abaton-EU Central",
    "Amarah-US East",
    "Artemis-EU Central",
    "Artorius-SA East",
    "Asgard-EU Central",
    "Barri-EU Central",
    "Castle of Steel-US East",
    "Cleopatra-EU Central",
    "Crassus-EU Central",
    "Delos-AP Southeast",
    "Devaloka-SA East",
    "El Dorado-US West",
    "Gaea-SA East",
    "Isabella-US West",
    "Kronos-EU Central",
    "Lilith-US East",
    "Maramma-US East",
    "Nysa-EU Central",
    "Nyx-EU Central",
    "Orofena-US East",
    "Seer-US East",
    "Sutekh-AP Southeast",
    "Valhalla-US East"
]

LOST_ARK_SERVER_LIST = [
    "Adrinne-US East",
    "Akkan-US West",
    "Aldebaran-US East",
    "Antares-EU Central",
    "Armen-EU Central",
    "Arthetine-South America",
    "Asta-EU Central",
    "Avesta-US East",
    "Azena-US East",
    "Bergstrom-US West",
    "Blackfang-South America",
    "Calvasus-EU Central",
    "Danube-US East",
    "Ealyn-EU West",
    "Elzowin-US East",
    "Enviska-US West",
    "Evergrace-EU Central",
    "Ezrebet-EU Central",
    "Galatur-US East",
    "Kadan-EU Central",
    "Karta-US East",
    "Kazeros-South America",
    "Kharmine-US East",
    "Ladon-US East",
    "Lazenith-EU Central",
    "Mari-US West",
    "Mokoko-EU Central",
    "Neria-EU Central",
    "Nia-EU West",
    "Regulus-US East",
    "Rohendel-US West",
    "Sasha-US East",
    "Shandi-US West",
    "Slen-EU Central",
    "Thirain-EU Central",
    "Trixion-EU Central",
    "Una-US East",
    "Valtan-US West",
    "Vykas-US East",
    "Wei-EU Central",
    "Zinnervale-EU Central",
    "Zosma-US East"
]