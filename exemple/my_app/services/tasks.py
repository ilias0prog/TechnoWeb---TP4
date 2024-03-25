from my_app.schemas import TaskSchema
from my_app.database import database


def save_task(new_task: TaskSchema) -> TaskSchema:
    database["tasks"].append(new_task)
    return new_task


def get_all_tasks() -> list[TaskSchema]:
    tasks_data = database["tasks"]
    tasks = [TaskSchema.model_validate(data) for data in tasks_data]
    return tasks
    
