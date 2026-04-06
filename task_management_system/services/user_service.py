from task_management_system.models.user import User
import sys
import logging
from exception.exception import ProjectException
from task_management_system.utils.helpers import load_from_json, save_to_json

logger = logging.getLogger(__name__)

class User_Service:
    def __init__(self):
        self.db_path = "task_management_system/data/users.json"
        self.users = load_from_json(self.db_path)
        logger.info(f"Loaded {len(self.users)} users from database.")

    def add_user(self, id, name , email):
        try:
            str_id = str(id)
            if str_id in self.users:
                raise ValueError(f"{str_id} already exists")
            user = User(id, name, email)
            self.users[str_id] = user.to_dict()
            save_to_json(self.db_path, self.users)
            logger.info(f"Added user with id {id}")
            return user
        except Exception as e:
            custom_error = ProjectException(e, sys)
            logger.error(custom_error)
            raise custom_error
    
    def get_user(self, id):
        return self.users.get(id)
    
    