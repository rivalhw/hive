# 一款(AI)儿童游戏给我的启发

**Author:** @rivalhw  
**Permlink:** 6nnnir-ai  
**Created:** 2023-12-22T03:37:12  
**Category:** hive-105017  
**Tags:** {
  "tags": [
    "kids",
    "game",
    "life",
    "cn-reader",
    "cn"
  ],
  "image": [
    "https://images.hive.blog/DQmYB2fXELZ91PewACTUg99B68nAFQVspkFbQN7cGCJv6Dq/image.png",
    "https://images.hive.blog/DQmXyFSvUt7LnrD5GwJrSLpKZ9cGBaDdEga3cogaEz8A86K/image.png",
    "https://images.hive.blog/DQmVVK86b1Hh8WbKu1vtUJ6YfJhrVFwXgRBDTtVFVT9hbEU/image.png",
    "https://images.hive.blog/DQmeBZv7y3udFvWbSnJtfeyzSatwa2sEVirbxovdZSKkARu/image.png",
    "https://images.hive.blog/DQmbX5Fs6YJ868BobUmZxBrtSKLJcZTCudCgugQfzaDTiSG/image.png"
  ],
  "links": [
    "http://animos.ai/"
  ],
  "app": "hiveblog/0.1",
  "format": "markdown"
}

---

一般来说，大多数人使用AI的习惯，就是直接询问AI一些问题，AI收到后给予回答。这个方法适用于各个行业。

　　稍微深入一些，便是利用AI的prompt，让AI模拟一些身份，来回答我们的问题，比如让对方：

　　你是一名专业的IT工程师；

　　你是一名专业的医生，在XX科方面有很深入的研究。。。

　　你叫XX，是XX公司的企业客服，擅长售前销售，根据企业资料回答用户的一些问题。。。

　　我先前也是这般认识，直到昨天看到有个网站[animos](http://animos.ai/)，如下图，


![image.png](https://images.hive.blog/DQmYB2fXELZ91PewACTUg99B68nAFQVspkFbQN7cGCJv6Dq/image.png)


　　这个网站是做什么呢？网站给出的一些介绍如下，


![image.png](https://images.hive.blog/DQmXyFSvUt7LnrD5GwJrSLpKZ9cGBaDdEga3cogaEz8A86K/image.png)

　　我看了下，主要是给儿童提供一些益智游戏，让儿童通过这些游戏达到学习的目的。

　　这跟市面上一些儿童游戏有什么不同呢？

　　嗯，最大的不同，就是这些游戏是同AI的结合来完成。简单说，就是游戏的玩家，不似传统那般固定的模式，而是让AI来扮演玩家跟用户对话，这是不是很有趣呢？

　　在我看过作者将其思路分享出来后，感觉更是很受启发。

　　让我大受启发的主要是有以下两点：

　　一是利用了open AI的function call，可以自行编写一些功能，让AI根据实际情况来进行调用，比如成语接龙这个游戏里，编写一个自定义的function ，查询数据库的成语，成功返回候选的成语，错误则返回false。

　　open AI关于function call的介绍信息，如下图，


![image.png](https://images.hive.blog/DQmVVK86b1Hh8WbKu1vtUJ6YfJhrVFwXgRBDTtVFVT9hbEU/image.png)

　　另一个启发，让我非受震撼。

　　如下是作者分享的游戏下prompt的内容，


![image.png](https://images.hive.blog/DQmeBZv7y3udFvWbSnJtfeyzSatwa2sEVirbxovdZSKkARu/image.png)


![image.png](https://images.hive.blog/DQmbX5Fs6YJ868BobUmZxBrtSKLJcZTCudCgugQfzaDTiSG/image.png)

　　这个prompt写的简直太准确和细致了！！！

　　通过这样很详细的描述，包括准确规则、提示用语、限制等，AI可以很准确的理解我们的意思，通过跟用户的对话，合理的去调用我们编写的function call。

　　简直不要太完美！

　　试想下，通过类似的思路，我们要再结合AI去完成一些其他的任务或游戏，会不会也很简单呢？

　　换句话讲，AI不仅大大降低了门槛，而且让我们的思路有了很大的转折和改变。

　　这个网站跟AI合作的思路，对我们的启发是不是很大呢？
