from cspark.Update import Update


class MessageUpdate(Update):

    def __init__(self, message, room):
        self.__message = message
        self.__room = room

    def get_plain_text(self):
        return self.__message['text']

    def get_room(self):
        return self.__room