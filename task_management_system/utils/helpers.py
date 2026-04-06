import json
import os
import logging

logger = logging.getLogger(__name__)

def load_from_json(filepath):
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return {}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        logger.error(f"Failed to read {filepath}. File might be corrupted.")
        return {}
    
def save_to_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)