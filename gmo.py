import logging

from cryptofeed.feed import Feed
from cryptofeed.connection import AsyncConnection, RestEndpoint, Routes, WebsocketEndpoint
# from cryptofeed.defines import GMO

LOG = logging.getLogger('feedhandler')

class Gmo(Feed):
    id = 'GMO' #to be changed to GMO after

    def __init__(self, **kwargs):
        super().__init__('wss://api.coin.z.com/ws', **kwargs)
        self.__reset()

    def __reset(self):
        pass

    async def subscribe(self, conn: AsyncConnection):
        self.__reset()
        for chan in self.subscription: #throwing TypeError: 'NotImplementedType' object is not iterable
            print(chan)


test = Gmo()
test.subscribe()
