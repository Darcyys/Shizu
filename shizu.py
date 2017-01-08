import discord
from shizu_commands import *
import inspect


class Shizu(discord.Client):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.core = Core(self)
        self.cmd = ShizuCommands(self)

    def run(self, *args):
        self.loop.run_until_complete(self.start(*args))

    async def on_ready(self):
        #  Shizu is ready !! <3
        print(
            """
              ______ ______ ______ ______ ______ ______ ______ ______ ______
             |______|______|______|______|______|______|______|______|______|
              ______ ______ ______ ______ ______ ______ ______ ______ ______
             |______|______|______|______|______|______|______|______|______|
              / ____| |   (_)                              | |     | | |
             | (___ | |__  _ _____   _   _ __ ___  __ _  __| |_   _| | |
              \___ \| '_ \| |_  / | | | | '__/ _ \/ _` |/ _` | | | | | |
              ____) | | | | |/ /| |_| | | | |  __/ (_| | (_| | |_| |_|_|
             |_____/|_| |_|_/___|\__,_| |_|  \___|\__,_|\__,_|\__, (_|_)
                                                               __/ |
              ______ ______ ______ ______ ______ ______ ______|___/__ ______
             |______|______|______|______|______|______|______|______|______|
              ______ ______ ______ ______ ______ ______ ______ ______ ______
             |______|______|______|______|______|______|______|______|______|
            """
        )
        juegos = ["Pokémon Luna", "Pokémon Stars", "http://shizudx.xyz/", ";help"]
        await self.change_presence(game=discord.Game(name=random.choice(juegos)))

    async def on_message(self, message):
        """
            TODO:
            - Guardar en redis ♥ un conteo de las veces que llaman al bot
        """

        #  autor = message.author
        #  print("[{0}]: {1}. [{2}, {3}]".format(autor, message.content, message.channel, message.server))
        msg = message.content
        if msg and message.content[0] != ";":
            return

        # obtengo cada metodo de la clase de comandos y verifico si hay match de comandos.
        for name, method in inspect.getmembers(self.cmd, predicate=inspect.ismethod):
            if name == "__init__":
                continue

            call = await method(message)
            if call:
                break

    # Todos los eventos para referencia
    async def on_error(self, event, *args, **kwargs):
        pass

    async def on_resumed(self):
        pass

    async def on_message_delete(self, message):
        pass

    async def on_message_edit(self, before, after):
        pass

    async def on_reaction_add(self, reaction, user):
        pass

    async def on_reaction_remove(self, reaction, user):
        pass

    async def on_reaction_clear(self, message, reactions):
        pass

    async def on_channel_delete(self, channel):
        pass

    async def on_channel_create(self, channel):
        pass

    async def on_channel_update(self, before, after):
        pass

    async def on_member_join(self, member):
        pass

    async def on_member_remove(self, member):
        pass

    async def on_member_update(self, before, after):
        pass

    async def on_server_join(self, server):
        pass

    async def on_server_remove(self, server):
        pass

    async def on_server_update(self, before, after):
        pass

    async def on_server_role_create(self, role):
        pass

    async def on_server_role_delete(self, role):
        pass

    async def on_server_role_update(self, before, after):
        pass

    async def on_server_emojis_update(self, before, after):
        pass

    async def on_server_available(self, server):
        pass

    async def on_server_unavailable(self, server):
        pass

    async def on_voice_state_update(self, before, after):
        pass

    async def on_member_ban(self, member):
        pass

    async def on_member_unban(self, server, user):
        pass

    async def on_typing(self, channel, user, when):
        pass

    async def on_group_join(self, channel, user):
        pass

    async def on_group_remove(self, channel, user):
        pass

bot = Shizu()
bot.run(getpath("TOKEN"))
