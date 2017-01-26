#########################################################
# Check examples/1_room_mentions_counter.py for basics! #
#########################################################

from cspark.Updater import Updater
from cspark.PeeweeContextRouter import PeeweeContextRouter
from cspark.MessageResponse import MessageResponse
from cspark.PeeweeContextStorage import PeeweeContextStorage
from cspark.UpdateHandler import UpdateHandler


updater = Updater(
    access_token="",
)


class RegistrationUpdateHandler(UpdateHandler, PeeweeContextStorage):

    STEPS_REQUIRED = 2
    REG_CONTEXT_KEY = 'registration_scenario_step_number'

    def handle_update(self):

        if self.context[RegistrationUpdateHandler.REG_CONTEXT_KEY] == 2:
            self.context.user["last_name"] = self.update.get_plain_text()
            self.send_response(MessageResponse("Good. Now let me greet you!"))

        if self.context[RegistrationUpdateHandler.REG_CONTEXT_KEY] == 1:
            self.context.user["first_name"] = self.update.get_plain_text()
            self.send_response(MessageResponse("What's your last name?"))

        elif self.context[RegistrationUpdateHandler.REG_CONTEXT_KEY] == 0:
            self.send_response(MessageResponse("Hi! What's your first name?"))

        self.context[RegistrationUpdateHandler.REG_CONTEXT_KEY] += 1


class GreetingUpdateHandler(UpdateHandler):
    def handle_update(self):
        self.send_response(
            MessageResponse("Hello, " + self.context.user["first_name"] + self.context.user["last_name"] + "!")
        )


class MyRouter(PeeweeContextRouter):
    """
    Inherited from PeeweeContextRouter so we can use "self.context" again.
    Here we use it to define handler class
    """

    def get_handler_class(self):

        # User should be registered. So if his "context.user" has no data about registration,
        # let's send him to registration.

        if RegistrationUpdateHandler.REG_CONTEXT_KEY not in self.context.user:
            self.context['registration_scenario_step'] = 0
            return RegistrationUpdateHandler

        # If he didn't finish all registration steps, go to continue registration

        if self.context.user[RegistrationUpdateHandler.REG_CONTEXT_KEY] < RegistrationUpdateHandler.STEPS_REQUIRED:
            return RegistrationUpdateHandler

        # Otherwise, greet him!
        return GreetingUpdateHandler


updater.add_router(MyRouter)
updater.idle()
