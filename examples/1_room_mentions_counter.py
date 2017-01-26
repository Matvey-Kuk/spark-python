##########################################
# Check examples/0_simple_echo.py before #
##########################################

from cspark.Updater import Updater
from cspark.EventTypeRouter import EventTypeRouter
from cspark.UpdateHandler import UpdateHandler
from cspark.SQLiteContextEngine import SQLiteContextEngine
from cspark.MessageResponse import MessageResponse


updater = Updater(
    access_token="",
)


class RoomMentionsCounterUpdateHandler(UpdateHandler, SQLiteContextEngine):
    """
    Handler should process messages from user and response with answers.

    This class inherited from UpdateHandler and PeeweeContextStorage.

    UpdateHandler gives you "self.send_response" to send answers.

    PeeweeContextStorage gives you "self.context" which is a dictionary.
    You can save your data there for future. It's stateful container,
    which stores your data in Peewee ORM (SQLite by default).
    """

    def handle_update(self):
        if 'counter' not in self.context.room:
            self.context.room['counter'] = 1
        else:
            self.context.room['counter'] += 1

        self.send_response(
            MessageResponse("Room counter: " + str(self.context.room['counter']))
        )


class Router(EventTypeRouter):
    """
    Router should decide which message should be processed by which handler.

    This router is inherited from EventTypeRouter which divide updates by their type.
    For example this router set RoomMentionsCounterUpdateHandler for updates which are messages.
    """
    new_message_handler = RoomMentionsCounterUpdateHandler

# Now we need to register router
updater.add_router(Router)

# And start "event loop"
updater.idle()
