import re
import os
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    return value.lower() in ["true", "yes", "1", "enable", "y"] if isinstance(value, str) else default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '26649585'))
API_HASH = environ.get('API_HASH', '588a3ea6fd01ae88bd2e10fed7d55b2c')
BOT_TOKEN = environ.get('BOT_TOKEN')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', "False"), False)
PICS = environ.get('PICS', 'https://envs.sh/ykQ.jpg').split()
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/b860e8d8a234384950587.jpg")
WVD = environ.get("WVD", "https://telegra.ph/file/b735f93c8eeef4167c6a1.mp4")
NO_IMDB = environ.get("NO_IMDB", "https://graph.org/file/5c94a977943ac2b777d93.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7945551029').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1002323154734')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rahat")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Rahat')

# AI
HORRI_API_KEY = environ.get('HORRI_API_KEY', 'horridapi_Uwk1YJbLSibv2rf88EBPOQ_free_key')  
BOT_USERNAME = environ.get('BOT_USERNAME', 'MoviesMake_rbot')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002316472437')) if environ.get('LOG_CHANNEL') else None
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+FHPsQEnXiA8xMGI1')
UPDATE_CHANNEL = environ.get('UPDATE_CHANNEL', 'https://t.me/FILME_MAKER')

P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', "False"), False)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
PORT = environ.get("PORT", "8080")
NO_RESULTS_MSG = is_enabled(environ.get("NO_RESULTS_MSG", "False"), False)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = int(environ.get("MAX_LIST_ELM", 10)) if environ.get("MAX_LIST_ELM") else None
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL)) if environ.get('INDEX_REQ_CHANNEL') else LOG_CHANNEL
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '-1002316472437').split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += "IMDB Results are enabled.\n" if IMDB else "IMDB Results are disabled.\n"
LOG_STR += "P_TTI_SHOW_OFF enabled.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF disabled.\n"
LOG_STR += "SINGLE_BUTTON is enabled.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled.\n"
LOG_STR += f"CUSTOM_FILE_CAPTION: {CUSTOM_FILE_CAPTION}\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION found.\n"
LOG_STR += "Long IMDB storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "Short IMDB storyline enabled.\n"
LOG_STR += "Spell Check Mode is enabled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n"
LOG_STR += f"MAX_LIST_ELM: {MAX_LIST_ELM}\n" if MAX_LIST_ELM else "Full list will be shown.\n"
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}\n"

print(LOG_STR)
