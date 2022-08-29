import factory
import logging
from faker import Faker
from django.contrib.auth.models import User
from tr_ars import models

logger = logging.getLogger('faker')
logger.setLevel(logging.INFO)
fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'

class AgentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Agent
        django_get_or_create = ("name",)
    name = 'agent_default'
    uri = 'ara-example/api/'

class ChannelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Channel
    name = 'general'
    description = fake.text()

class ActorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Actor

    agent = factory.SubFactory(AgentFactory)
    channel = 'general'
    path = 'runquery'
    inforesid = fake.word()
    active = 'True'

class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Message

    id = fake.uuid4()
    name = 'default_message'
    status = 'D'
    actor = factory.SubFactory(ActorFactory)


