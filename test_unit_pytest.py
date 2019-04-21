class hello:
    message = "test_message"

    def __init__(self):
        pass

    def set(self, message):
        self.message = message

    def show(self):
        print(self.message)


def test_hello_world():
    h = hello()
    h.set("test")
    assert h.message == "test"
