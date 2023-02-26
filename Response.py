import dataclasses
from typing import Callable


@dataclasses.dataclass
class Response:
    data: str
    status_code: int = 200
    content_type: str = "text/plain"

    def __call__(self, make_response: Callable):
        status = {
            200: "200 OK",
            404: "404 NOT FOUND"
        }
        resp = bytes(self.data, "utf8")
        headers = [
            ("Content-Type", self.content_type),
            ("Content-Length", str(len(resp))),
        ]
        make_response(status[self.status_code], headers)
        return [resp]
