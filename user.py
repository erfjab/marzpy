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
    
    async def add(self, username: str, status: str, proxies: dict, inbounds: dict, data_limit: int, expire: int = None, on_hold_timeout: str = None, on_hold_expire_duration: int = None, data_limit_reset_strategy: str = 'no_reset', note: str = '', token: str = None) -> dict | None:
        try :
            data = {
                'username' : username,
                'status' : status,
                'proxies' : proxies,
                'inbounds' : inbounds,
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
            logging.error(f'add user: {error}')
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
            logging.error(f'edit user: {error}')
            return None

    async def reset_data_usage(self, username: str, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint=f'/user/{username}/reset', method='post', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'reset data usage: {error}')
            return None
    
    async def revoke_sub(self, username: str, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint=f'/user/{username}/revoke_sub', method='post', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'revoke sub: {error}')
            return None
    
    async def set_owner(self, username: str, admin_username: str, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint=f'/user/{username}/set-owner?admin_username={admin_username}', method='put', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'set owner: {error}')
            return None
    
    async def usage(self, username: str, start: str = None, end: str = None, token: str = None) -> dict | None:
        try:
            endpoint = f'/user/{username}/usage'
            params = []
            if start:
                params.append(f'start={start}')
            if end:
                params.append(f'end={end}')
            if params:
                endpoint += '?' + '&'.join(params)  
            return await request(panel=self.panel, endpoint=endpoint, token=token)
        except aiohttp.ClientError as error:
            logging.error(f'user usage: {error}')
            return None
        
    async def disabled(self, username: str, token: str = None) -> dict | None:
        try :
            data = { 'status' : 'disabled' }
            return await request(panel=self.panel, endpoint=f'/user/{username}', method='put', data=data, token=token)
        except aiohttp.ClientError as error:
            logging.error(f'set owner: {error}')
            return None

    async def activated(self, username: str, token: str = None) -> dict | None:
        try :
            data = { 'status' : 'active' }
            return await request(panel=self.panel, endpoint=f'/user/{username}', method='put', data=data, token=token)
        except aiohttp.ClientError as error:
            logging.error(f'set owner: {error}')
            return None