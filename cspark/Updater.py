

class Updater(object):

    MODE_INSANE_REQUESTS, MODE_WEBHOOK = range(2)

    def __init__(
            self,
            access_token,
            mode=MODE_INSANE_REQUESTS,
            context_engine_for_callbacks=None,
            context_engine_for_insane_requests_mode_support=None
    ):
        self.__access_token = access_token
        self.__mode = mode
        self.__context_engine_for_callbacks = context_engine_for_callbacks
        self.__context_engine_for_insane_requests_mode_support = context_engine_for_insane_requests_mode_support

    def run(self):
        pass

    def subscribe_new_message(self, callback):
        pass

    def idle(self):
        pass

    def add_router(self, class_name):
        pass

    def send_response(self, room_id, response):
        pass

    def add_new_message_listener(self, callback):
        pass

