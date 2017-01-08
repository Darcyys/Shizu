import random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap
from bot_vars import getpath
import string
import aiohttp
import async_timeout
import json


class Core:

    def __init__(self, shizu):
        self.shizu = shizu
        self.session = aiohttp.ClientSession(loop=shizu.loop)

    @staticmethod
    def random_hex(digits):
        return ''.join([random.choice(string.hexdigits) for x in range(digits)])

    async def random_cat(self):
        # agregar timeout y mejorar un poquito esto
        url = 'http://random.cat/meow'
        response = await self.session.get(url)
        assert response.status == 200  # ...
        response = await response.text()
        try:
            url = json.loads(response)
            return url["file"]
        except json.decoder.JSONDecodeError:
            return

    def rip(self, text):
        if not text:
            return
        if len(text) > 50:
            text = text[:50]
        para = textwrap.wrap(text, width=15)
        font = ImageFont.truetype(getpath("FONT_FOLDER") + "arial-bold.ttf", 20)
        img = Image.open(getpath("IMG_FOLDER") + 'RIP.jpg')
        draw = ImageDraw.Draw(img)

        current_h, pad = 200, 10
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text(((290 - w) / 2, current_h), line, (0, 0, 0), font=font)
            current_h += h + pad

        # checkear si existe ese archivo antes de retornarlo..
        url = getpath("TEMP_FOLDER") + self.random_hex(20) + ".png"
        img.save(url)
        return url
