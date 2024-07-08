from typing import Callable, Any, Dict, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class TestMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]
                       ) -> Any:
        print('Действия до оброботчика')
        result = await handler(event, data)
        print('Действия после оброботчика')
        return result

