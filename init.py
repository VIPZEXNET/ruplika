"""
Ruplika - Python Library for Rubika Bot API
Version: 3.1.2
"""

from .bot import Bot
from .client import Client
from .models import *
from .enums import *
from .exceptions import *
from .utils import *

__version__ = "3.1.2"
__author__ = "Ruplika Team"
__email__ = "support@ruplika.com"

__all__ = [
    "Bot",
    "Client",
    "RubikaException",
    "APIException",
    "NetworkException",
    "AuthenticationException",
]