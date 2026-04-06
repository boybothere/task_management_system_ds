import os
import logging
from datetime import datetime

current_time = datetime.now().strftime('%d_%m_%Y')

LOG_FOLDER = os.path.join(os.getcwd(), "logs", current_time)

os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_FOLDER, "system.log")

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)