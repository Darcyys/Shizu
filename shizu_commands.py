from decorators import commands
import os
"""
    TODO:
    - Cambiar respuestas del bot en español por dependiendo del lenguaje seleccionado.
    - Pensar otro nombre para esta clase y archivo que no me gusta el actual.
"""


class ShizuCommands:

    def __init__(self, shizu):
        self.shizu = shizu
        self.core = self.shizu.core

    @commands()
    async def test(self, message):
        await self.shizu.send_message(message.channel, "tost")

    @commands()
    async def ping(self, message):
        await self.shizu.send_message(message.channel, "pong")

    @commands()
    async def rip(self, message):
        msg = message.content
        if not msg:
            return

        url = self.core.rip(msg)
        await self.shizu.send_file(message.channel, url)
        assert os.remove(url)

    @commands()
    async def randomcat(self, message):
        url = await self.core.random_cat()
        if not url:
            # agregar error a un futuro log
            return
        await self.shizu.send_message(message.channel, url)
