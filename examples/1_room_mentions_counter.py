from cspark.Updater import Updater
from cspark.EventTypeRouter import EventTypeRouter
from cspark.UpdateHandler import UpdateHandler
from cspark.PeeweeContextStorage import PeeweeContextStorage
from cspark.MessageResponse import MessageResponse


# Updater handles main event loop. At first, need to setup Updater with your access_token
updater = Updater(
    access_token="",
)


class RoomMentionsCounterUpdateHandler(UpdateHandler, PeeweeContextStorage):
    """
    This class inherited from UpdateHandler and PeeweeContextStorage.

    UpdateHandler is a simple handler. You need it to use "handle_update" method.

    PeeweeContextStorage gives you "self.context" which is dictionare.
    You can save your data there for future. It's stateful container.
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
    This router is inherited from EventTypeRouter which divide updates by their type.
    For example this router set RoomMentionsCounterUpdateHandler for updates which are messages.
    """
    new_message_handler = RoomMentionsCounterUpdateHandler

# Now we need to register router
updater.add_router(Router)

# And start "event loop"
updater.idle()
