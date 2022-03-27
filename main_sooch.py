import json
import logging
import os
import sys
import traceback
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler, Formatter, DEBUG

import nextcord as discord

from sooch import path, command_actions, database


async def run_command(interaction, name, params, scopes):
    try:
        embed = discord.Embed(title="SOOCH PROMPT")

        # Every command requires different contexts of information.
        # This information is loaded here.
        contexts = database.load_contexts(scopes)

        components = {"view": discord.interactions.MISSING}

        # Determine the scope of the command. Call the function for all valid scopes.
        await command_actions.call_cmd_function(
            command_actions.CommandScope.Always,
            name, interaction, embed, params, contexts, {}
        )

        # noinspection PyUnreachableCode
        if False:  # Server admin
            await command_actions.call_cmd_function(
                command_actions.CommandScope.ServerAdmin,
                name, interaction, embed, params, contexts, {}
            )

        if interaction.user.id == 221222294767403008:
            await command_actions.call_cmd_function(
                command_actions.CommandScope.GlobalAdmin,
                name, interaction, embed, params, contexts, {}
            )

        if embed and embed.description != "DO NOT SEND":
            if len(embed.fields) == 0:
                embed.add_field(
                    name="Unrecognised command",
                    value="You either can't use this command right now or it doesn't exist."
                )

                await interaction.send(embed=embed, view=components["view"], ephemeral=True)
            else:
                await interaction.channel.send(embed=embed, view=components["view"])

    except Exception as e:
        integrity_channel = client.get_channel(956982790593839154)
        await integrity_channel.send(
            "Command issue: original message in server ID `{}`. Author: {}. Command: `{} {}`.\n\n{}\n\n{}".format(
                interaction.guild.id if interaction.guild else "(DM)",
                interaction.user.mention,
                name,
                params,
                str(e),
                traceback.format_exc())
        )


client = discord.Client()


@client.slash_command(name="ping", description="Pong!", guild_ids=[803997808809607179])
async def slashcmd_ping(
    interaction: discord.Interaction
):
    await run_command(interaction, "s$ping", [], database.Scopes.NONE)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print("Connected to {} guilds".format(len(client.guilds)))

    # client.loop.create_task(minute_timer())
    # client.loop.create_task(minute_timer_checker())


@client.event
async def on_message(message: discord.Message):
    # Message content is no longer supported.
    pass


with open("token", "r") as f:
    client.run(f.read())
