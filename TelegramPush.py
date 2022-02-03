import toml
import logging
from telegram.ext import Updater

updater = Updater(token=toml.load("./config.toml")["tg_bot"]["token"], use_context=True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

