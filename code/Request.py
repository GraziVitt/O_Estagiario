import random


class Request:

    def __init__(self):

        self.all_items = [
            "cafe",
            "caneta",
            "documentos",
            "copo",
            "grampeador",
            "pasta"
        ]

        self.completed = 0

        self.current_request = ""

        self.new_request()

    def new_request(self):
        self.current_request = random.choice(self.all_items)

    def check(self, item_name):

        if item_name == self.current_request:

            self.completed += 1

            self.new_request()

            return True

        return False