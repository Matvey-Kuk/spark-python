from cspark.Updater import Updater
from cspark.SQLiteContextEngine import SQLiteContextEngine
from cspark.MessageResponse import MessageResponse

# Updater handles main event loop. At first, you need
# to setup Updater with your access_token.
updater = Updater(
    access_token="YTNjMjVjMjQtZGJkNS00ZWUzLTg5NjMtZWI1NGY2NjYwMTQ0NTExOTYwMTktMWQw",
    context_engine_class=SQLiteContextEngine
)


def echo_with_counter(update, context):
    """
    :param update: message from user
    :param context: persistent container for your data
    :return: context, don't forget
    """
    updater.send_response(
        update.get_room(),
        MessageResponse(update.get_plain_text())
    )
    return context

# Now we need to register callback
updater.add_new_message_listener(echo_with_counter)

# And start "event loop"
updater.idle()
