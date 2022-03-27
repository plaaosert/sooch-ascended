import time
from enum import Enum

import nextcord as discord

from player import Player


class CommandScope(Enum):
    Always = 0
    ServerAdmin = 1
    GlobalAdmin = 2


async def claim_cmd(interaction: discord.Interaction, embed: discord.Embed, params, contexts):
    player_in_context: Player = contexts.player




async def invalid_server_cmd(interaction: discord.Interaction, embed: discord.Embed, params, contexts):
    pass


async def admin_ping_cmd(interaction: discord.Interaction, embed: discord.Embed, params, contexts):
    embed.add_field(name="Pong!", value="Hello. The time is {}.".format(time.time()))
    await interaction.send(content="This is an ephemeral response.", ephemeral=True)


command_dict = (
    # Always
    {"s!claim": claim_cmd, "s!stats": invalid_cmd},

    # ServerAdmin
    {"s.nothing": invalid_server_cmd},

    # GlobalAdmin
    {"s$ping": admin_ping_cmd}
)


# Pass a custom command into the bot. Very similar but a slight convenience function.
# probably not required... lol
async def pass_custom_command(scope: CommandScope,
                              cmd, interaction, embed, params, contexts, components):
    await call_cmd_function(
        scope, cmd, interaction, embed, params, contexts, components
    )

    return components


async def call_cmd_function(scope: CommandScope,
                            cmd, interaction, embed, params, contexts, components):
    if cmd in command_dict[scope.value]:
        component = await command_dict[scope.value][cmd](
            interaction, embed, params, contexts
        )

        if isinstance(component, dict):
            for key in component:
                print(key, component[key])
                components[key] = component[key]
        elif component:
            components[component[0]] = component[1]
