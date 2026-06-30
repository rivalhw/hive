# 大模型不止聊天，用AI来实现一个类似苹果下"hello siri"的多面助手

**Author:** @rivalhw  
**Permlink:** ai-hello-siri  
**Created:** 2024-03-15T03:58:36  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "format": "markdown",
  "image": [
    "https://images.hive.blog/DQmT3PM7UpgDE6pveFiAT5KE98aJArmGvhTtF1KMimZ4n4y/004.png",
    "https://images.hive.blog/DQmWGBW4vgc24p8VhXYDYq5W5gC3sXRihjN9o8bb1PVbvMZ/000.png",
    "https://images.hive.blog/DQmWqGo2HhfUQpbK7XEwCugas9N59Px9ceXN7z92AVEdhZE/001.png",
    "https://images.hive.blog/DQmapEGo5r4gvhGFDvtE1GNypjb9LsCKcMSbjNb5G2xxfuS/002.png",
    "https://images.hive.blog/DQmcq7aHnMk69ksyr75Ty4dxQtQD4djZRz2F3v3nD96YzMw/003.png",
    "https://images.hive.blog/DQmQrHxCvqCa8BwqFsA3TL7GzbwENxYpRZb82oYjhLt28M6/005.png"
  ],
  "tags": [
    "ai",
    "openai",
    "coze",
    "life",
    "cn-reader",
    "cn"
  ]
}

---

几个月前时候，我看到有人用openAI来制作了个适合儿童的学习游戏，感觉非常有意思。我当时还研究了下那个游戏的思路和方法，其中有一点用到了openAI的function call，这个功能非常好，就是可以根据实际情况调用你自己的本地API，大模型和这个功能结合起来，可以应用到实践中严谨的场合，避免了大模型有时候说话给人有些不靠谱的感觉。

　　但是遗憾的是，当时我转了一圈，发现当时国内的大模型都没有提供这个function call,简单讲，当时国内的大模型只适合一些非正式场合，或者对实际应用场景要求不那么严格的情况下。

　　前阵子，听说国内的智谱大模型已经开始提供了这个功能，跑上去看了下，果然，如下图，

　　![000.png](https://images.hive.blog/DQmWGBW4vgc24p8VhXYDYq5W5gC3sXRihjN9o8bb1PVbvMZ/000.png)

　　非常棒，看来很快可以将大模型跟实际的场景结合起来使用了。

　　之前用大模型，总觉得像个万花筒，如果只是把大模型当做一个工具用，那很难发挥出它的作用和威力，而实际的工作中，我们所做的工作有时候不一定很难，但是涉及多任务，或者多个工作的协同才能完成，而多态代理大模型，则很好的能够帮我们完成这样的工作任务。

　　比如coze，切换到多态代理大模型下，如下图，

　　![001.png](https://images.hive.blog/DQmWqGo2HhfUQpbK7XEwCugas9N59Px9ceXN7z92AVEdhZE/001.png)

　　我们可以在这下边，根据我们的实际需求工作，创建相应的需求助手，比如，我们试着创建一个类似苹果系统下的“hello siri”的助理工具。

　　![002.png](https://images.hive.blog/DQmapEGo5r4gvhGFDvtE1GNypjb9LsCKcMSbjNb5G2xxfuS/002.png)

　　主要有三个选项，

　　名称，介绍这个工具主要是做什么用；

　　技能，简单理解就是这个助理主要擅长处理哪方面的事情，比如收发邮件，比如天气预报，今日头条新闻，或者twitter等

　　跳转条件：就是在什么情况下触发该条件，比如当你喊：hello siri ！自动返回主菜单。

　　![003.png](https://images.hive.blog/DQmcq7aHnMk69ksyr75Ty4dxQtQD4djZRz2F3v3nD96YzMw/003.png)

　　比如第一个是帮我们用来收发邮件，或者帮我们阅读下邮件，将有用的信息提炼出来，简要说明等。

　　![004.png](https://images.hive.blog/DQmT3PM7UpgDE6pveFiAT5KE98aJArmGvhTtF1KMimZ4n4y/004.png)

　　我试着让它帮我发送一封邮件，内容让大模型根据我的想法自己去完善，结果如下图，

　　![005.png](https://images.hive.blog/DQmQrHxCvqCa8BwqFsA3TL7GzbwENxYpRZb82oYjhLt28M6/005.png)

　　可以看到，这个对面助手，很好的理解了我的指令，每次我对着它说：“你好助理！”时，它便会自动返回主菜单，然后再根据我具体的指令，分配对应的专业助理去完成相应的专业技能任务。

　　有了这样的多态代理大模型，我们可以将自己日常工作细分下，将不同的细分任务交给它分别去完成，不但完成的很好，更主要的是，这样的大模型，才真正解放了我们的双手和大脑呀！
