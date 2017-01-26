

class Updater(object):

    MODE_INSANE_REQUESTS, MODE_WEBHOOK = range(2)

    def __init__(self, access_token, mode=MODE_INSANE_REQUESTS):
        self.__access_token = access_token
        self.__mode = mode

    def run(self):
        pass

    def subscribe_new_message(self, callback):
        pass

    def idle(self):
        pass

    def add_router(self, class_name):
        pass
