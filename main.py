import os
import logger.logger_setup
import logging

logger = logging.getLogger(__name__)


from task_management_system.services.task_service import Task_Service
from task_management_system.services.user_service import User_Service


def main():
    try: 
        logger.info("--- TASK MANAGEMENT SYSTEM BOOT SEQUENCE INITIATED ---")
        task_service = Task_Service()
        user_service = User_Service()

        user_service.add_user(123, "Adrian", "adrian@gmail.com")

        task_service.create_task(1, "Setup capstone project", "From scratch")
        task_service.create_task(2, "Add project pipeline script", "After Setup")

        completed_task = task_service.complete_tasks()
        logger.info(f"Task completed: {completed_task}")
    except Exception as e:
        logger.error("Error Message", exc_info=True)

if __name__ == "__main__":
    main()