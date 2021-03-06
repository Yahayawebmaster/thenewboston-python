from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from ..constants.network import PROTOCOL_CHOICES, VERIFY_KEY_LENGTH
from ..models.network_node import NetworkNode


class NetworkNodeFactory(DjangoModelFactory):
    account_number = Faker('text', max_nb_chars=VERIFY_KEY_LENGTH)
    default_transaction_fee = Faker('pyfloat', left_digits=16, right_digits=16)
    ip_address = Faker('ipv4')
    node_identifier = Faker('text', max_nb_chars=VERIFY_KEY_LENGTH)
    port = Faker('random_int', min=0, max=65535)
    protocol = FuzzyChoice([p[1] for p in PROTOCOL_CHOICES])
    version = Faker('text', max_nb_chars=32)

    class Meta:
        model = NetworkNode
        abstract = True
