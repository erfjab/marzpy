import aiohttp
import json

async def request(panel: str, endpoint: str, token: dict = None, method: str = 'get', data: dict = None) -> dict:
    """
    This is for creating requests with aiohttp and async.
    
    Parameters :
        `address` (str - required) : Marzban panel address
        `endpoint` (str - required) : Marzban api endpoint
        `token` (str - required) : Marzban panel access token 
        `method` (str - optional) : Request methods (like get, delete, put, post) default is get. 
        `data` (dict - optional) : The data you want to send, default is None.
    returns :
        `Response` : Return the response with status code and data
    """
    # create a session
    async with aiohttp.ClientSession() as session:
        # set requireds
        username, password, address = panel
        # check token
        if not token: 
            url = f'{address}/api/admin/token'
            token_data = {'username': username, 'password': password}
            async with session.post(url=url, data=token_data, raise_for_status=True) as response:
                result = await response.json()
                token = result['access_token']
        # set url
        url = f'{address}/api{endpoint}'
        # set header & dumps data
        headers = {'accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': f"Bearer {token}"}
        compressed_data = json.dumps(data).encode('utf-8') if data else None
        # get request as response
        async with session.request(
            method=method,
            url=url,
            headers=headers,
            data=compressed_data,
            raise_for_status=True
        ) as response:
            # read response result & return
            result = await response.json()
            result['status_code'] = response.status
            return result

