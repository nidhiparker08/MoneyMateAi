from abc import ABC, abstractmethod

class BaseProvider(ABC):

    @property
    @abstractmethod
    def bank_name(self):
        ...

    @property
    @abstractmethod
    def short_name(self):
        ...

    @property
    @abstractmethod
    def ifsc_prefix(self):
        ...

    @property
    @abstractmethod
    def swift_prefix(self):
        ...

    @property
    @abstractmethod
    def account_prefix(self):
        ...

    @property
    @abstractmethod
    def branches(self):
        ...

    @abstractmethod
    def generate_account(self):
        ...

    @abstractmethod
    def generate_transactions(self):
        ...

    @abstractmethod
    def generate_investments(self):
        ...