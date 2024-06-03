import logging
from .request import request
import aiohttp

class Admin:
    def __init__(self, username: str, password: str, address: str) -> None:
        self.username = username
        self.password = password
        self.address = address
        self.panel = (username, password, address)

    async def token(self, username: str = None, password: str = None, address: str = None):
        try :
            username = username or self.username
            password = password or self.password
            address = address or self.address
            async with aiohttp.ClientSession() as session:
                url = f'{self.address}/api/admin/token'
                data = {'username': username, 'password': password}
                async with session.post(url=url, data=data, raise_for_status=True) as response:
                    result = await response.json()
                    return result['access_token']
        except aiohttp.ClientError as error:
            logging.error(f'we have a error in generate token: {error}')
            return None
    
    async def list(self , token: dict = None):
        try :
            return await request(panel=self.panel, endpoint='/admins', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'we have a error in get admins list: {error}')
            return None
    
    async def info(self, username: str = None, password: str = None, token: dict = None):
        username = username or self.username
        password = password or self.password
        panel = (username, password, self.address)
        try :
            return await request(panel=panel, endpoint='/admin', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'we have a error in get currect admin info: {error}')
            return None
            
    async def add(self, username: str, password: str, is_sudo: bool = False, telegram_id: int = None, discord_webhook: str = None, token: dict = None):
        try :
            data = {
                "username": username,
                "is_sudo": is_sudo,
                "telegram_id": telegram_id,
                "discord_webhook": discord_webhook,
                "password": password
                }
            return await request(panel=self.panel, endpoint='/admin', method='post', data=data, token=token)
        except aiohttp.ClientError as error:
            logging.error(f'we have a error in add admin: {error}')
            return None
        
    async def edit(self, username: str, password: str, is_sudo: bool = None, telegram_id: int = None, discord_webhook: str = None, token: dict = None):
        try :
            admin_data = await self.info(username=username, password=password)
            if not admin_data :
                return None
            is_sudo = is_sudo or admin_data['is_sudo']
            telegram_id = telegram_id or admin_data['telegram_id']
            discord_webhook = discord_webhook or admin_data['discord_webhook']
            data = {
                "is_sudo": is_sudo,
                "telegram_id": telegram_id,
                "discord_webhook": discord_webhook,
                "password": password
                }
            return await request(panel=self.panel, endpoint=f'/admin/{username}', method='put', data=data, token=token)
        except aiohttp.ClientError as error:
            logging.error(f'we have a error in edit admin: {error}')
            return None

    async def delete(self, username: str, token: dict = None):
        try :
            return await request(panel=self.panel, endpoint=f'/admin/{username}', method='delete', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'we have a error in delete admin: {error}')
            return None
    
