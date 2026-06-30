# AI最大的问题

**Author:** @rivalhw  
**Permlink:** 4dtogw-10  
**Created:** 2026-05-30T03:02:39  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "tags": [
    "llm",
    "ai",
    "life",
    "cn-reader",
    "cn"
  ],
  "image": [
    "https://images.hive.blog/DQmanS5wEmqMc5ikmkoK1aHMZhzHsJ8AbHGTkuZr6ixsX8g/image.png",
    "https://images.hive.blog/DQmZvBiPbzHw67Q3UowLy1A1nKiEQqwZv2cv9TKCco3wNZq/f1f9a91d-a00b-4000-b9f0-1fa4e8af9f4f.png",
    "https://images.hive.blog/DQmU6ujaV5WWwxYZ3bP68Zv6cwZdMGidgYGETrZgMcGm8wu/image.png"
  ],
  "format": "markdown"
}

---

这两天有个热闹的话题，就是OpenClaw（龙虾）的创始人 Peter Steinberger  在X上贴出了自己使用的token消耗量，如下图，


![image.png](https://images.hive.blog/DQmanS5wEmqMc5ikmkoK1aHMZhzHsJ8AbHGTkuZr6ixsX8g/image.png)
图片来源于[Peter Steinberger ](https://x.com/steipete/status/2055346265869721905) X.com 上帖子

从截图上来看，他一个月消耗的 Token 数量为6030亿。

有人计算了下，相当于

>平均每天要花费4万多美元

这显然是个非常疯狂的数字，不过实际上虽说用了这么多，但他是 OpenAI 公司的员工，可以无限量免费使用公司的token，自然也不用每天花那么多钱了。

但是说到token消耗，这玩意说真的，真是很费钱啊。

有人跟我抬杠，说他用了几个小时，也不过花了几块钱。嗯，我这里说的都是强模型，那种模型聊天吹牛可以，但没办法用来工作的模型，不在我的讨论范围。


![f1f9a91d-a00b-4000-b9f0-1fa4e8af9f4f.png](https://images.hive.blog/DQmZvBiPbzHw67Q3UowLy1A1nKiEQqwZv2cv9TKCco3wNZq/f1f9a91d-a00b-4000-b9f0-1fa4e8af9f4f.png)


我看了下我自己的使用，比如昨天用了刚推出的最新Opus4.8，最贵的一条命令，消耗了715万 token，用了我5.71美刀，折合人民币38.64元，如下图，


![image.png](https://images.hive.blog/DQmU6ujaV5WWwxYZ3bP68Zv6cwZdMGidgYGETrZgMcGm8wu/image.png)


这只是一个命令任务花费的，要知道，一天工作可不止提交这一个指令。我算是很谨慎了，但每天用去几十刀也很正常。

不是我想这样，实在是其它的大模型太拉跨，“货比货就想扔”,我自己同时在用的大模型有3、4个，有时候你不得不用其中一个你认为最好的。

codex其实也不错，包月便宜实惠。但是，我发现它有个很大的问题，就是总喜欢“做好事”。

比如你要做某个功能，它会帮你完成后，然后“好心”再“顺手”增加或调整下另外某处功能，看起来是好意，但这玩意就是个双刃剑，甚至可以说就是坑。。。

为啥？

原因也很简单，AI 永久了，人就会变得懒惰，很多工作都会交给AI，审查时也只是大概看下，修改的内容多了，自然会漏掉一些。这样时间久了，就会出现你修改后边的内容，忽然发现前边之前确认过的内容或模块发生问题，反复检查之后，才发现是被之前不知道何时早已改坏，而这坑直到问题出现时才发现。。。

我之前提到过，去年年底到今年年初以来，AI编码这里提升很大，最重要的是，解决了大部分幻觉问题。但是，鉴于目前AI都是基于上下文理解，彻底已解决幻觉我认为这话还为时过早，或许可以说之前已经解决了90%的幻觉问题，剩下的10%似乎离彻底解决不远了。。。

实际上呢，我现在的感受是，剩下的10%如果看作一个问题整体，下次再解决30%、50%。。。这就是个无解的方程，只要基于目前这种上下文方式，而不是像人类那样通过彻底理解，估计幻觉问题永远都会存在剩下10%的问题存在了。

AI看起来非常聪明，似乎无所不能，但它当下最大的问题，就是不知道对与错，只能永远给出一个它认为最大概率正确的“答案”。
