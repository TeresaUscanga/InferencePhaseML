class Logger:
    def log(self, message: str):
        print("Logger: " + message)

class MathBoy:
    def __init__(self, logger: Logger, operadorYee):
        self.logger = logger
        self.operadorYee = operadorYee

    def greetings(self, message: str):
        self.logger.log('Hi ' + message)

    def jump(self):
        self.operadorYee.saltar()
