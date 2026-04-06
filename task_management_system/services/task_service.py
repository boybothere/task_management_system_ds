from task_management_system.models.queue import Queue
from task_management_system.models.task import Task
from task_management_system.models.stack import Stack
import logging

from task_management_system.utils.helpers import load_from_json, save_to_json

logger = logging.getLogger(__name__)

class Task_Service:
    def __init__(self):
        self.db_path = "task_management_system/data/tasks.json"
        self.tasks = load_from_json(self.db_path)
        self.task_queue = Queue()
        self.task_history = Stack()

    def create_task(self, id, title , description):
        try:
            task = Task(id, title, description)
            self.task_queue.enqueue(task)
            self.tasks[str(id)] = task.to_dict()
            save_to_json(self.db_path, self.tasks)
            return task
        except Exception as e:
            logger.error("Some error occurred", exc_info=True)

    def complete_tasks(self):
        if not self.task_queue.is_empty():
            task = self.task_queue.dequeue()
            self.task_history.push(task)
            return task.title
        return None

    def get_task_history(self):
        return self.task_history