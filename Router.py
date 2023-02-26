import Views


def router(path: str):
    if path in ["/tasks", "/tasks/"]:
        return Views.tasks_list
    elif "/tasks/" in path:
        return Views.task_detail
    elif path == "/":
        return Views.hello_world
    else:
        return Views.not_found()
