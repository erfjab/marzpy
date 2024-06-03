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

>[!IMPORTANT]
>**about token:** we automatically generated token and use it :/


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

## Node\

### node info
```python
await panel.node.info(node_id=1)
```
### node add
```python
await panel.node.add(name='new_node_name', ip='8.0.0.8', port=62050, usage_coefficient=1.5)
```
### node edit
```python
await panel.node.edit(node_id=1, ip='4.4.4.4')
```
### node delete
```python
await panel.node.delete(node_id=1)
```
### node settings
```python
await panel.node.settings()
```
### node list
```python
await panel.node.list()
```
### node disabled
```python
await panel.node.disabled(node_id=1)
```
### node activated
```python
await panel.node.activated(node_id=1)
```
### node reconnect
```python
await panel.node.reconnect(node_id=1)
```
### node status
```python
await panel.node.status(node_id=1)
```
### node usage
```python
await panel.node.usage(node_id=1)
```
