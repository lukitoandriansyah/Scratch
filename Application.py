from typing import Callable
from Router import router


def application(request_data: dict, make_response: Callable):
    path = request_data["PATH_INFO"]
    view_func = router(path=path)

    res = view_func(request_data)
    return res
