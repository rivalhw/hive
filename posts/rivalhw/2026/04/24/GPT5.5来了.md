# GPT5.5来了

**Author:** @rivalhw  
**Permlink:** gpt5-5  
**Created:** 2026-04-24T02:14:18  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "format": "markdown",
  "image": [
    "https://images.hive.blog/DQmYrbzer5fmnvvoWeFPuHqyiYqejNvjpVUJZkHPWtJJczT/image.png",
    "https://images.hive.blog/DQmX35SKRxJG37gYqGxKNaoYT7EyZi6CTZaCUPS62pxpGJA/image.png",
    "https://images.hive.blog/DQmaWR6P5h7vDVRKzNfTbxHe1z53i1skPrQ92kVPS9o3BDF/image.png",
    "https://images.hive.blog/DQmdd7PJTz7aA1WkDMa6itWKJhznM8yDvWeUfwQL5Q42kYF/76218fc6d028b3aca6d86bc6fd097805.png",
    "https://images.hive.blog/DQmNQpqfCQHoGMLXfJycvQ2AUjuurxthmevpNuaEkKa8sfv/image.png"
  ],
  "tags": [
    "ai",
    "gpt",
    "codex",
    "opus",
    "kimi",
    "cn-reader",
    "cn"
  ]
}

---

早晨一打开电脑，发现GPT似乎有些变化，仔细看了下，果不其然，从昨天的GPT5.4升级到了最新的5.5,如下图，


![image.png](https://images.hive.blog/DQmYrbzer5fmnvvoWeFPuHqyiYqejNvjpVUJZkHPWtJJczT/image.png)

看下5.5比之前的5.4做了哪些方面的改善，我们让它自己回答，



![image.png](https://images.hive.blog/DQmX35SKRxJG37gYqGxKNaoYT7EyZi6CTZaCUPS62pxpGJA/image.png)



![image.png](https://images.hive.blog/DQmaWR6P5h7vDVRKzNfTbxHe1z53i1skPrQ92kVPS9o3BDF/image.png)




从它自己给出的回答，可以看出，这次5.5的升级，主要体现在：

>GPT-5.5 的优势主要体现在“长链路技术分析 + 代码落地 + 多步骤排查”

这种升级，对于大多数普通使用用户来说，应该是很难觉察到。但对于我这类经常要进行长链路(较长任务)技术分析的用户来说，那可真是及时雨啊。

我之前用gpt5.4和opus4.6，但是上个月的时候，发现opus4.6忽然不给用了。没办法，只好切换到国产的kimi2.5,勉强可以用，但效果嘛，只能说一分价钱一分货，比上不足，比下有余。

后来为了方便，我干脆现在弄了台新加坡的远程服务器，这样opus就可以继续用了。之前我是在不同终端使用多个大模型，后来我一想这样太麻烦，有时候为了一个任务还需要文件多次来回拷贝，非常琐碎，干脆就在这同一台服务器上部署好多个大模型调用，包括kimi-cli、codex。

现在我的做法是，最复杂的任务交给opus(最新的4.7)，其次codex，日常的工作由kimi完成，毕竟kimi最便宜，一个任务跑十几甚至几十分钟，也不会心疼。


![76218fc6d028b3aca6d86bc6fd097805.png](https://images.hive.blog/DQmdd7PJTz7aA1WkDMa6itWKJhznM8yDvWeUfwQL5Q42kYF/76218fc6d028b3aca6d86bc6fd097805.png)

人常说，“偏听则暗，兼听则明。” 同样，碰到一时难以判断的问题，我会分别交给opus4.7和codex5.4,让他们先给出各自的分析结果，然后我再把两者给出的分析综合再交由其中一个分析，这样得出来的分析结果就会较为全面，也尽可能避免了一些极端情况下的误判。


![image.png](https://images.hive.blog/DQmNQpqfCQHoGMLXfJycvQ2AUjuurxthmevpNuaEkKa8sfv/image.png)

AI真是个好工具，用的好，真的对人工作的帮助和提升很大啊。
