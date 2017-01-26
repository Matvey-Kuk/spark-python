from cspark.Updater import Updater
from cspark.PeeweeContextEngine import PeeweeContextEngine
from cspark.MessageUpdate import MessageUpdate
from cspark.MessageResponse import MessageResponse


updater = Updater(
    access_token="",
    context_engine_for_callbacks=PeeweeContextEngine
)


def echo_with_counter(update, context):

    if type(update) is MessageUpdate:

        if 'counter' not in context.user:
            context.user['counter'] = 1
        else:
            context.user['counter'] += 1

        updater.send_response(
            update.room,
            MessageResponse("Message #" + str(context.user['counter']) + ": " + update.get_plain_text())
        )

    return context

updater.add_new_message_listener(echo_with_counter)
updater.idle()
