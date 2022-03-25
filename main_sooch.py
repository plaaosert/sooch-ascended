import json
import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler, Formatter, DEBUG

import nextcord as discord

from sooch import path, command_actions

client = discord.Client()


with open("token", "r") as f:
    client.run(f.read())
