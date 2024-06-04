import logging
import aiohttp
from .request import request

class Node:
    def __init__(self, username: str, password: str, address: str) -> None:
        self.username = username
        self.password = password
        self.address = address
        self.panel = (username, password, address)

    async def list(self, offest: int = None, limit: int = None, prefix: str = None, status: str = None, sort: str = None, token: str = None) -> dict | None:
        try :
            endpoint = '/users'
            params = []
            if offest:
                params.append(f'offest={offest}')
            if limit:
                params.append(f'limit={limit}')
            if prefix:
                params.append(f'prefix={prefix}')
            if status:
                params.append(f'status={status}')
            if sort:
                params.append(f'sort={sort}')
            if params:
                endpoint += '?' + '&'.join(params) 
            return await request(panel=self.panel, endpoint=endpoint, token=token)
        except aiohttp.ClientError as error:
            logging.error(f'get users list: {error}')
            return None
    
    async def reset_data_usage(self, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint='/users/reset', method='post' ,token=token)
        except aiohttp.ClientError as error:
            logging.error(f'reset users data: {error}')
            return None
    
    async def get_expired(self, start: str = None, end: str = None, token: str = None) -> dict | None:
        try:
            endpoint = '/users/expired'
            params = []
            if start:
                params.append(f'start={start}')
            if end:
                params.append(f'end={end}')
            if params:
                endpoint += '?' + '&'.join(params)  
            return await request(panel=self.panel, endpoint=endpoint, token=token)
        except aiohttp.ClientError as error:
            logging.error(f'users expired: {error}')
            return None

    async def delete_expired(self, start: str = None, end: str = None, token: str = None) -> dict | None:
        try:
            endpoint = '/users/expired'
            params = []
            if start:
                params.append(f'start={start}')
            if end:
                params.append(f'end={end}')
            if params:
                endpoint += '?' + '&'.join(params)  
            return await request(panel=self.panel, endpoint=endpoint, method='delete', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'users expired: {error}')
            return None