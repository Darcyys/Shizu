from functools import wraps
from bot_vars import getpath


def commands(agregarweasaquiparaqueestotengamassentidoxd=None):
    def decor(func):
        func_name = func.__name__
        command_prefix = getpath("COMMAND_PREFIX")  # change this for a better wea?
        command_name = command_prefix + func_name

        @wraps(func)
        async def wrapper(self, message):
            """
                Este wrapper sera el encargado de verificar que todo vaya bien (?
                Mas que todo para verificar comandos, cooldowns y otra cosa que se me vaya ocurriendo ~
            """
            match = message.content.startswith(command_name)
            if not match:
                return
            message.content = message.content.replace(command_name, '').strip()  # obtengo el mensaje virgen sin comandos

            await func(self, message)

        return wrapper
    return decor

