from .Router import Router
from .ContextBuilder import ContextBuilder


class ContextRouter(Router, ContextBuilder):

    def __init__(self, context_engine=None):
        super(ContextRouter, self).__init__(context_engine)

    def handle_update(self, update):
        self.build_context(update)
        handler_class = self.get_handler_class()
        handler = handler_class(context_engine=self.get_context_engine_for_handlers(handler_class))
        handler.handle_update(update)
        self.save_context(update)

    def get_context_engine_for_handlers(self, handler_class):
        return self.__context_engine
