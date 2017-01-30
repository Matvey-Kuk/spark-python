import requests

from cspark.Update import Update


class MessageUpdate(Update):

    def __init__(self, message, room, headers):
        self.__message = message
        self.__room = room
        self.__headers = headers

    def get_raw_message(self):
        return self.__message

    def get_plain_text(self):
        if 'text' in self.__message:
            return self.__message['text']

    def get_room(self):
        return self.__room

    def get_files_list(self):
        if 'files' in self.__message:
            return self.__message['files']
        else:
            return []

    def download_file(self, number, file_distanation):
        file = self.__message['files'][number]
        response = requests.get(file, headers=self.__headers)

        if response.status_code == 200:
            with open(file_distanation, 'wb') as buffer:
                buffer.write(response.content)
