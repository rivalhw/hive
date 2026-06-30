# 尝试在zed下使用DeepSeek

**Author:** @rivalhw  
**Permlink:** zed-deepseek  
**Created:** 2026-05-01T08:58:30  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "format": "markdown",
  "image": [
    "https://images.hive.blog/DQmXwBuaYeWpaEXVToG6g65PYZSGmF74iLJ1PESYPkDmxJr/image.png",
    "https://images.hive.blog/DQmVyF3ebo3CHDKKUUEoez9Ltnk8Jqzvq52PBU8Dp9Ru7NE/11d58c0486327eaab24985c742401323.png",
    "https://images.hive.blog/DQmbtNoZqAi9gcBaRisUEYAPd4jufo29iFhVbzvmRGWHbPL/d929e6531f43d9b704e56518963119f2.png",
    "https://images.hive.blog/DQmV1FHXm1RGskrkFcKBK9DrgMjZbxT8oAX6Nn52pNgcTE1/3a5986df9eda6167c57647959658d78c.png",
    "https://images.hive.blog/DQmYiK2euDhRQ3sF34NqRchUC94v2tiXeyiGXDo7KPaACKb/f797e52cc23d3aa29f7e20debaea62ff.png",
    "https://images.hive.blog/DQmQSPUDfeTPi5xHGdeEFGT9QNzKGpw7BoFFdga1u2am3pE/image.png"
  ],
  "tags": [
    "zed",
    "ai",
    "deepseek",
    "cn-reader",
    "cn"
  ],
  "users": [
    "lemooljiang"
  ]
}

---

昨天提到说我用DeepSeek V4的时候，发现速度奇慢无比，后来@lemooljiang  留言说，

>不要走openrouter，直接用官网的API就行，能快不少！

我昨晚试了下，用国内API 直连，发现果然是。

这真是“听人劝 能吃饱饭”。

今早在家，试了下DeepSeek V4的效果。

我在本地电脑安装了个 zed 软件，


![image.png](https://images.hive.blog/DQmXwBuaYeWpaEXVToG6g65PYZSGmF74iLJ1PESYPkDmxJr/image.png)

这玩意比较冷僻，估计很多人都不一定听过。我之前有篇帖子介绍过这个软件，当初是把它当记事本来用，效果比一般的记事本文件要多很多，其中最大的优点，就是适合打开超大文件比如几百M甚至上G的文件，同时打开后浏览内容时，非常丝毫，不会有其它软件那种明显卡顿的感觉。

偶然间，发现这家伙竟然也有AI的功能，而且看起来，AI是它今后主攻的重点方向。

zed下接入大模型很简单，打开界面后，直接输入API key即可，


![11d58c0486327eaab24985c742401323.png](https://images.hive.blog/DQmVyF3ebo3CHDKKUUEoez9Ltnk8Jqzvq52PBU8Dp9Ru7NE/11d58c0486327eaab24985c742401323.png)

至于使用，也很简单，Ctrl+Enter 键，弹出个输入框，直接在里边输入即可，


![d929e6531f43d9b704e56518963119f2.png](https://images.hive.blog/DQmbtNoZqAi9gcBaRisUEYAPd4jufo29iFhVbzvmRGWHbPL/d929e6531f43d9b704e56518963119f2.png)


我用Deep Seek V4 测试写了个简易计算器，发现通过直连速度果然快很多，而且生成后的界面还挺好看，


![3a5986df9eda6167c57647959658d78c.png](https://images.hive.blog/DQmV1FHXm1RGskrkFcKBK9DrgMjZbxT8oAX6Nn52pNgcTE1/3a5986df9eda6167c57647959658d78c.png)

孩子在边上，说让我帮他生成个变形金刚。

我试了下，生成后如下图，


![f797e52cc23d3aa29f7e20debaea62ff.png](https://images.hive.blog/DQmYiK2euDhRQ3sF34NqRchUC94v2tiXeyiGXDo7KPaACKb/f797e52cc23d3aa29f7e20debaea62ff.png)

发现生成的效果不好，很丑，而且还有乱码。

孩子一看这效果，顿时没了兴趣，转身就走开了。

哦，可能是我描述的不够清晰吧。囧


![image.png](https://images.hive.blog/DQmQSPUDfeTPi5xHGdeEFGT9QNzKGpw7BoFFdga1u2am3pE/image.png)

不过话说回来，zed的界面，做的真是极简到极致，比如最常见的按钮，一般的软件都会把按钮平铺到软件界面上，但zed显然不这样，除非你想要，否则尽可能不出现，这点刚开始用时很不习惯，但用多了就觉得挺好的。

看起来zed在这方面的追求，很有种追求极客精神的味道。
