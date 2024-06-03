import logging
import aiohttp
from .request import request

class Node:
    def __init__(self, username: str, password: str, address: str) -> None:
        self.username = username
        self.password = password
        self.address = address
        self.panel = (username, password, address)

    async def info(self, username: str, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint=f'/user/{username}', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'get user info: {error}')
            return None
    
    async def delete(self, username: str, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint=f'/user/{username}', method='delete' ,token=token)
        except aiohttp.ClientError as error:
            logging.error(f'delete user: {error}')
            return None
    
    async def add(self, username: str, status: str, proxies: dict, inbounds: dict, expire: int, data_limit: int, on_hold_timeout: str, on_hold_expire_duration: int, data_limit_reset_strategy: str = 'no_reset', note: str = '', token: str = None) -> dict | None:
        try :
            data = {
                'username' : username,
                'status' : status,
                'proxies' : proxies,
                'inbounds' : inbounds,
                'expire' : expire,
                'data_limit' : data_limit,
                'data_limit_reset_strategy' : data_limit_reset_strategy,
                'note' : note
            }
            if status == 'active':
                data['expire'] = expire
            if status == 'on_hold':
                data['on_hold_timeout'] = on_hold_timeout
                data['on_hold_expire_duration'] = on_hold_expire_duration
            return await request(panel=self.panel, endpoint='/user', method='post', data=data ,token=token)
        except aiohttp.ClientError as error:
            logging.error(f'delete user: {error}')
            return None

    async def edit(self, username: str = None, status: str = None, proxies: dict = None, inbounds: dict = None, expire: int = None, data_limit: int = None, on_hold_timeout: str = None, on_hold_expire_duration: int = None, data_limit_reset_strategy: str = None, note: str = None, token: str = None) -> dict | None:
        try :
            data = {}
            params = locals()
            for key, value in params.items():
                if key not in ['self', 'username', 'token'] and value is not None:
                    data[key] = value
            return await request(panel=self.panel, endpoint=f'/user/{username}', method='put', data=data ,token=token)
        except aiohttp.ClientError as error:
            logging.error(f'delete user: {error}')
            return None
