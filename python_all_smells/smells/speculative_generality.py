from abc import ABC, abstractmethod

class AbstractLegacyProcessor(ABC):
    @abstractmethod
    def process(self, value):
        raise NotImplementedError

class LoggingMixin:
    def log(self, message):
        return f"LOG:{message}"

class BaseFutureExtension:
    def extension_point(self):
        return None
