import logging
import aiohttp
from .request import request

class Node:
    def __init__(self, username: str, password: str, address: str) -> None:
        self.username = username
        self.password = password
        self.address = address
        self.panel = (username, password, address)

    async def info(self, node_id: int, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint=f'/node/{node_id}', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'get node info: {error}')
            return None
    
    async def add(self, name: str, ip: str, port: int = 62050, api_port: int = 62051, add_as_new_host: bool = False, usage_coefficient: float = 1.0, token: str = None) -> dict | None:
        try :
            data = {
                "name": name,   
                "address": ip,
                "port": port,
                "api_port": api_port,
                "add_as_new_host": add_as_new_host,
                "usage_coefficient": usage_coefficient
            }
            return await request(panel=self.panel, endpoint='/node', method='post', data=data, token=token)
        except aiohttp.ClientError as error:
            logging.error(f'add new node: {error}')
            return None
    
    async def edit(self, node_id: int, name: str = None, ip: int = None, status: str = None, port: int = None, api_port: int = None, usage_coefficient: float = None, token: str = None) -> dict | None:
        try :
            node_data = await self.info(node_id=node_id, token=token)
            if not node_data :
                return None
            name = name or node_data['name']
            ip = ip or node_data['address']
            port = port or node_data['port']
            api_port = api_port or node_data['api_port']
            status = status or node_data['status']
            usage_coefficient = usage_coefficient or node_data['usage_coefficient']
            data = {
                "name": name,   
                "address": ip,
                "port": port,
                "api_port": api_port,
                "status": status,
                "usage_coefficient": usage_coefficient
            }
            return await request(panel=self.panel, endpoint=f'/node/{node_id}', method='put', data=data, token=token)
        except aiohttp.ClientError as error:
            logging.error(f'edit node: {error}')
            return None
    
    async def delete(self, node_id: int, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint=f'/node/{node_id}', method='delete', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'delete node: {error}')
            return None
    
    async def list(self, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint='/nodes', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'get node list: {error}')
            return None
    
    async def settings(self, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint='/node/settings', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'get node settings: {error}')
            return None
    
    async def reconnect(self, node_id: int, token: str = None) -> dict | None:
        try :
            return await request(panel=self.panel, endpoint=f'/node/{node_id}/reconnect', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'reconnect node: {error}')
            return None
        
    async def disabled(self, node_id: int, token: str = None) -> dict | None:
        try :
            data = {"status": "disabled"}
            return await request(panel=self.panel, endpoint=f'/node/{node_id}', data=data, method='put', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'disabled node: {error}')
            return None

    async def activated(self, node_id: int, token: str = None) -> dict | None:
        try :
            data = {"status": "connected"}
            return await request(panel=self.panel, endpoint=f'/node/{node_id}', data=data, method='put', token=token)
        except aiohttp.ClientError as error:
            logging.error(f'activated node: {error}')
            return None
    
    async def status(self, node_id: int, token: str = None) -> str | None:
        try :
            node_data = await self.info(node_id=node_id, token=token)
            return node_data['status'] if node_data else None
        except aiohttp.ClientError as error:
            logging.error(f'node status: {error}')
            return None

    async def usage(self, start: str = None, end: str = None, token: str = None) -> dict | None:
        try:
            endpoint = '/nodes/usage'
            params = []
            if start:
                params.append(f'start={start}')
            if end:
                params.append(f'end={end}')
            if params:
                endpoint += '?' + '&'.join(params)  
            return await request(panel=self.panel, endpoint=endpoint, token=token)
        except aiohttp.ClientError as error:
            logging.error(f'node usage: {error}')
            return None