# 用Redis实现AI上下文所需要的格式数据

**Author:** @rivalhw  
**Permlink:** redis-ai  
**Created:** 2023-10-09T02:40:42  
**Category:** hive-105017  
**Tags:** {
  "tags": [
    "ai",
    "redis",
    "db"
  ],
  "image": [
    "https://images.hive.blog/DQmQC4XFgxkmtMGBu63naacNuLuRt74Jvc8pZ4uVLKandt6/gannet-8281303_1280.jpg",
    "https://images.hive.blog/DQmXbaeidQREbZmmpqfzM2Ryegq1PajhBCQBdEBdmaa2TmQ/image.png",
    "https://images.hive.blog/DQmZn52EZev9meTJtUPNVLcM8MtxeL64YoKutrKosMEhfpT/image.png",
    "https://images.hive.blog/DQmcRse4A5JuLWDyWvHqddX6WPkXtC21i52rGEU6YntTnA4/image.png",
    "https://images.hive.blog/DQmQm7f7jMugp6o4aHbVTkPXD1ea94PP8wXqqBrbC6iiZKu/image.png",
    "https://images.hive.blog/DQmR1AUE18yrbX5HeD6eVMA7tLPQHkoiEQu5HzQacNkweEn/image.png"
  ],
  "links": [
    "https://blog.larkneer.com/trend/@lemooljiang/twr9x3bp"
  ],
  "app": "hiveblog/0.1",
  "format": "markdown"
}

---

AI对话里常常需要用到上下文场景，而之前所做的客服里，每次的请求都是独立的，也就是没有提供上下文内容，这样用户每次对话，相当于独立的问答，很不友好。

　　有没有个方法可以解决这个问题？

　　我想到用Redis来实现，主要理由有两点：

　　一是Redis是基于内存的数据存储，相比较传统数据库，速度非常快；

　　二是Redis的存储读取非常方便，无需像传统数据库那般比较繁琐。

　　关于AI的上下文格式， lemooljiang之前写过一篇文章[《ChatGPT如何获取上下文》](https://blog.larkneer.com/trend/@lemooljiang/twr9x3bp)，有提到如下格式，

>messages =  [
	{ 'role': 'user', 'content': '你好。 今天是多云天气' },
	{ 'role': 'assistant', 'content': '你好。 我很抱歉听到不幸的天气' },
	{ 'role': 'user', 'content': '是的，是这样。 不过我很好。' },
	{ 'role': 'assistant', 'content': '我希望如此。 让我们继续今天的工作吧！' },
	{ 'role': 'user', 'content': '是的。 哦，顺便问一下，我是怎么说今天的天气的？' },
	{ 'role': 'assistant', 'content': '今天是阴天' }
] 

于是我就根据自己的需求，来最后生成如上所需要的格式数据。

思考了下，除了AI必须得两个参数：role(角色)和 content(对话内容)之外，实际需要的参数还包括，企业ID，用户ID以及时间戳。

那么定义如下：

　　corp_id(企业ID)

　　user_id(用户ID)

　　timestamp(时间戳)

准备用三个函数来实现我的需求，包括 存储对话、查询对话以及删除相关对话。

当然，删除相关对话主要是方便我测试，实际中比较少用。

首先来完成存储对话，代码实现如下，


    def store_chat(self, corp_id, user_id, role, content, timestamp):
        # 构建存储键名
        chat_key = f"chat:{corp_id}:{user_id}"
        
        # 构建存储值
        chat_data = {
            "role": role,
            "content": content
        }
        
        # 将聊天内容存储到Redis中
        self.redis_client.lpush(chat_key, json.dumps(chat_data))

<p>

　　我用"chat:{corp_id}:{user_id}"当做ID作为key键，存储该企业用户的所有聊天记录。

　　存储的内容格式用数据JSON来完成，符合AI上下文messages的要求。

　　最后存储用lpush来实现存储。

查询对话时，需要传入对话的ID，代码实现如下,
 
    def get_chats(self, corp_id, user_id):
        # 构建查询键名
        chat_key = f"chat:{corp_id}:{user_id}"
        
        # 获取聊天记录
        chat_records = self.redis_client.lrange(chat_key, 0, -1)
        
        # 将记录反序列化为字典对象
        sorted_chats = [json.loads(chat) for chat in chat_records]
        
        # 按照时间戳顺序排序
        # sorted_chats = sorted(sorted_chats, key=lambda x: x['timestamp'])
        
        return sorted_chats

其中"corp_id, user_id"前边提前，用于做数据记录的ID存储，这里查询也同样用途。

删除对话

这个就很简单了，代码实现如下，

    def delete_chats(self, corp_id, user_id):
        # 构建删除键名
        chat_key = f"chat:{corp_id}:{user_id}"
        
        # 删除相关聊天记录
        self.redis_client.delete(chat_key)


最后封装成Class对象，调用起来就方便了。

完整的代码实现，如下图，

![image.png](https://images.hive.blog/DQmXbaeidQREbZmmpqfzM2Ryegq1PajhBCQBdEBdmaa2TmQ/image.png)


![image.png](https://images.hive.blog/DQmZn52EZev9meTJtUPNVLcM8MtxeL64YoKutrKosMEhfpT/image.png)


哦，为了防止上下文超过长度，我单独写了个函数，防止判断上下文聊天记录超过一定长度，


![image.png](https://images.hive.blog/DQmcRse4A5JuLWDyWvHqddX6WPkXtC21i52rGEU6YntTnA4/image.png)

模拟添加一些数据，试下效果如何？

测试代码如下，



>chat_storage = ChatStorageRedis()
>
>chat_storage.store_chat('corp_id_1', 'example_userid', 'assistant', 'Hello, how can I help you?', '2022-01-01 12:00:00')
>
>chat_storage.store_chat('corp_id_1', 'example_userid', 'user', 'I have a question about our product.', '2022-01-01 12:05:00')
>
>chat_storage.store_chat('corp_id_1', 'example_userid', 'assistant', 'are you OK?', '2022-01-01 12:06:00')
>chat_storage.store_chat('corp_id_1', 'example_userid', 'user', 'Yes!', '2022-01-01 12:07:00')
>chat_storage.store_chat('corp_id_1', 'example_userid', 'assistant', 'aaaaaaaaa', '2022-01-01 12:07:15')
>chat_storage.store_chat('corp_id_1', 'example_userid', 'user', 'bbbbbbbb!', '2022-01-01 12:07:30')
>chat_storage.store_chat('corp_id_1', 'example_userid', 'assistant', 'CCCCCCCCCCCCCCCCCCCCCCC', '2022-01-01 12:08:15')
>
>chat_storage.store_chat('corp_id_1', 'example_userid', 'user', 'DDDDDDDDDDDDDDDDDD!', '2022-01-01 12:08:30')
>
>chat_storage.store_chat('corp_id_1', 'example_userid', 'assistant', 'EEEEEEEEEEEEEEEEEEEEEEEE', '2022-01-01 12:09:15')
>
>
>chat_storage.store_chat('corp_id_1', 'example_userid', 'user', 'FFFFFFFFFF!', '2022-01-01 12:09:30')
chats = chat_storage.get_chats('corp_id_1', 'example_userid')
>
>content = getContent(chats,200)
>print("query content:"+ content)
>print("完整的记录如下："+str(chats))
>
>chat_storage.delete_chats('corp_id_1', 'example_userid')


![image.png](https://images.hive.blog/DQmQm7f7jMugp6o4aHbVTkPXD1ea94PP8wXqqBrbC6iiZKu/image.png)

控制台打印测试结果如下，

![image.png](https://images.hive.blog/DQmR1AUE18yrbX5HeD6eVMA7tLPQHkoiEQu5HzQacNkweEn/image.png)

NICE! 果然是我想要的数据格式了。:)


![gannet-8281303_1280.jpg](https://images.hive.blog/DQmQC4XFgxkmtMGBu63naacNuLuRt74Jvc8pZ4uVLKandt6/gannet-8281303_1280.jpg)
Image by <a href="https://pixabay.com/users/aidansemmens-5096137/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=8281303">Aidan Semmens</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=8281303">Pixabay</a>
