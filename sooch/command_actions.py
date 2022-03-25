from enum import Enum

import nextcord as discord


class CommandScope(Enum):
    Always = 0
    ServerAdmin = 1
    GlobalAdmin = 2


async def invalid_cmd(embed, message, params, player_in_context, server_in_context):
    pass


async def invalid_server_cmd(embed, message, params, player_in_context, server_in_context):
    pass


async def invalid_admin_cmd(embed, message, params, player_in_context, server_in_context):
    pass


command_dict = (
    # Always
    {"s!claim": invalid_cmd, "s!stats": invalid_cmd},

    # ServerAdmin
    {"b.nothing": invalid_server_cmd},

    # GlobalAdmin
    {"b$ping": invalid_admin_cmd}
)


# Pass a custom command into the bot. Very similar but a slight convenience function.
# probably not required... lol
async def pass_custom_command(scope: CommandScope,
                              cmd, message, embed, params, player_in_context, server_in_context, components):
    await call_cmd_function(
        scope, cmd, message, embed, params, player_in_context, server_in_context, components
    )

    return components


async def call_cmd_function(scope: CommandScope,
                            cmd, message, embed, params, player_in_context, server_in_context, components):
    if cmd in command_dict[scope.value]:
        component = await command_dict[scope.value][cmd](
            cmd, message, embed, params, player_in_context, server_in_context
        )

        if isinstance(component, dict):
            for key in component:
                print(key, component[key])
                components[key] = component[key]
        elif component:
            components[component[0]] = component[1]
