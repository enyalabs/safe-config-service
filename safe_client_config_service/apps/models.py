from django.contrib.postgres.fields import ArrayField
from django.db import models


class EthereumNetwork(models.IntegerChoices):
    MAINNET = 1
    MORDEN = 2
    ROPSTEN = 3
    RINKEBY = 4
    GOERLI = 5
    KOVAN = 42
    XDAI = 100
    ENERGY_WEB_CHAIN = 246
    LOCAL = 4447
    VOLTA = 73799
    UNKNOWN = 0


class Safe(models.Model):
    safeAddress = models.CharField


class App(models.Model):
    url = models.CharField()
    disabled = models.BooleanField()
    networks = ArrayField(models.IntegerField(choices=EthereumNetwork.choices))