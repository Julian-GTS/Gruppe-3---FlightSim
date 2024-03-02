from django.utils import timezone

class APIResponse:
    def __init__(self, success, data):
        print(data)
        self.success = success
        self.message = "The request was successful." if success else "Failure"
        self.errors = [] if success else data
        self.data = data
        self.timestamp = timezone.localtime().strftime("%d.%m.%Y %H:%M:%S")

    @classmethod
    def from_errors(cls, errors):
        return cls(success=False, errors=errors)


    def to_json(self):
        return {
            "success": self.success,
            "message": self.message,
            "errors": self.errors,
            "data": self.data,
            "timestamp": self.timestamp
        }