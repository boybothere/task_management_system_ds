import os
from pathlib import Path

project_title="task_management_system"

list_of_files=[
    "main.py",
    f"{project_title}/models/task.py",
    f"{project_title}/models/user.py",
    f"{project_title}/models/graph.py",
    f"{project_title}/models/stack.py",
    f"{project_title}/models/queue.py",
    f"{project_title}/services/task_service.py",
    f"{project_title}/services/user_service.py",
    f"{project_title}/utils/helpers.py",
    f"{project_title}/data/tasks.json",
    f"{project_title}/data/users.json"
]

for path in list_of_files:
    filepath = Path(path)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,  "w") as f:
            pass
