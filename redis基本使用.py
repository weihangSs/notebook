from redis import Redis
'''
redis有5种数据类型有5种函数
'''

# 1、连接数据库
redis_client = Redis(host='localhost', port=6379, db=1)
'''
2、添加数据
    set('key', 'value')
        如果数据库中没有key，则新建
        有则覆盖
'''
redis_client.set('name', '小明')

# 3、获取数据
    # get('key')
get_data = redis_client.get('name')
print(get_data.decode())

# 4、删除
    # delete('key')
    # 如果没有key不存在回报错
redis_client.delete('name')

# 5、获取所有的键
print(redis_client.keys())