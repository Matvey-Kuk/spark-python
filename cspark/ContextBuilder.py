class ContextBuilder:

    def __init__(self, context_engine):
        self.context = None
        self.__context_engine = context_engine

    def build_context(self, update):
        print("context builder")

    def save_context(self, update):
        print("context save")
