>[!IMPORTANT]
>**Status:** Working on new update :/

well, some examples tests

## Start

```python
from marzpy import Marzban
import asyncio

panel = Marzban('username', 'password', 'https://sub.domain.com:port')

async def mainer():
    pass

asyncio.run(mainer())
```

## Admins

### admin token
```python
# for me
await panel.admin.token()
# for another admin
await panel.admin.token('admin_username', 'admin_password')
```
### admin info
```python
# for me
await panel.admin.info()
# for another admin
await panel.admin.info('admin_username', 'admin_password')
```
### admin list
```python
await panel.admin.list()
```
### admin add
```python
await panel.admin.add(username='new_admin_username', password='new_admin_password', is_sudo=True)
```
### admin edit
```python
await panel.admin.edit(username='admin_username', password='admin_password', is_sudo=False)
```
### admin delete
```python
await panel.admin.delete('admin_username')
```

## Node -> coming soon...
