# 人人都能用的起的免费大模型：尝试本地安装和使用Ollama大模型（llama3.3 ，llama3.2）

**Author:** @rivalhw  
**Permlink:** ollama-llama3-3-llama3-2  
**Created:** 2024-12-09T07:20:03  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "format": "markdown",
  "image": [
    "https://images.hive.blog/DQmP71tpuxjQK1gps2NqNdb1WrTjDL3PDae68HqqU6Bf3gr/014.png",
    "https://images.hive.blog/DQmQEYYFYupFiARx77e3mEzn91hgfddexcm12K61A7VBwXb/image.png",
    "https://images.hive.blog/DQmbVUudi8jTdgjQXUJSkZ4YmvEU15MnJTTTfLVEerS2Kxp/001.png",
    "https://images.hive.blog/DQmVi9p547VXwbg2YWiFhAKcadzsgpaNq8TANGmUftpN7pj/002.png",
    "https://images.hive.blog/DQmXvEuq6qz9AXgPizEp3v9XfG51DQunbPE2hUZaSzBGUQz/003.png",
    "https://images.hive.blog/DQmPZhYSnVyUejEfda2xFb2AGHMwDFUpqvivoevJQMJgtyK/005.png",
    "https://images.hive.blog/DQmYKMKY3KnhPCuZBNPe8CQCUXaeot1zGqPvXh2x52cH1LP/006.png",
    "https://images.hive.blog/DQmeb5txJ6TgXNS91ShrMR8Xi3hcRs9ogX9k3QzNu9QSws5/007.png",
    "https://images.hive.blog/DQmdJsgZujLYMEySVCfNjNF83Moa6vGh7a5W4WEuMv88fnf/008.png",
    "https://images.hive.blog/DQmXYjwmnYty45sR9QYvEv1nnjkevKJNo3zu1ovjgpBKmYJ/009.png",
    "https://images.hive.blog/DQmNnTTHGdGKt3LRw3VzCE1mjGT4oUa5F6Wh2QHXi6mdKjg/010.png",
    "https://images.hive.blog/DQmYWMApotMQCXF28gP1UHAWJgWssTGLr7zGAaiHMa75LYG/012%20-%20%E5%89%AF%E6%9C%AC.png",
    "https://images.hive.blog/DQmYWMApotMQCXF28gP1UHAWJgWssTGLr7zGAaiHMa75LYG/012.png",
    "https://images.hive.blog/DQmd7otFth3yHtS4ShGgsu3vrfedeVmCtgc81XzVbvhHhrb/013.png",
    "https://images.hive.blog/DQmWMBXZeXiF4sXJ4ni1AvEzzW6DSTc4hQgAoNsp3g1rS88/011.png",
    "https://images.hive.blog/DQmUcMKGXja4WFMnWzTAUgg6FBCWD4EnRXgn2UbxyTU1k1e/015.png"
  ],
  "tags": [
    "ai",
    "llama",
    "ollama",
    "vscode",
    "cn-reader",
    "cn"
  ]
}

---

周六收到邮件，看到AI大模型Ollama开源了新版本 Llama 3.3 ，不仅有70B，还支持中文版，不禁心里有些痒痒，打算尝试下载使用下。

![image.png](https://images.hive.blog/DQmQEYYFYupFiARx77e3mEzn91hgfddexcm12K61A7VBwXb/image.png)

我之前安装过Llama 3.2，不过是1B而已，而且貌似当时不支持中文，你让它用中文回答，它却用拼音糊弄你。。。实在尴尬的很，囧囧囧。。。


![001.png](https://images.hive.blog/DQmbVUudi8jTdgjQXUJSkZ4YmvEU15MnJTTTfLVEerS2Kxp/001.png)

老样子，上github上，下载大模型先。

我之前下载Ollama，发现有个问题，就是它默认是安装在C盘符下，而我的C盘可用空间很小，导致下载到中途因为空间不够而问题而中断，




![002.png](https://images.hive.blog/DQmVi9p547VXwbg2YWiFhAKcadzsgpaNq8TANGmUftpN7pj/002.png)

![003.png](https://images.hive.blog/DQmXvEuq6qz9AXgPizEp3v9XfG51DQunbPE2hUZaSzBGUQz/003.png)

于是这次我找了下文档，将默认的路径改到其它盘符下，这样就不担心空间不够了。

如果你也碰到这类问题，就按照我这个方法，设置好变量先，将默认下载路径改为其它盘符，就可以完美解决该问题。

![005.png](https://images.hive.blog/DQmPZhYSnVyUejEfda2xFb2AGHMwDFUpqvivoevJQMJgtyK/005.png)

![006.png](https://images.hive.blog/DQmYKMKY3KnhPCuZBNPe8CQCUXaeot1zGqPvXh2x52cH1LP/006.png)

![007.png](https://images.hive.blog/DQmeb5txJ6TgXNS91ShrMR8Xi3hcRs9ogX9k3QzNu9QSws5/007.png)
开始下载 llama3.3 了，好激动，好期待。。。

![008.png](https://images.hive.blog/DQmdJsgZujLYMEySVCfNjNF83Moa6vGh7a5W4WEuMv88fnf/008.png)

![009.png](https://images.hive.blog/DQmXYjwmnYty45sR9QYvEv1nnjkevKJNo3zu1ovjgpBKmYJ/009.png)

结果呢，乐极生悲，提示在验证成功后，出现错误如下：
PS D:\ollama> ollama run llama3.3
pulling manifest
pulling 4824460d29f2... 100% ▕████████████████████████████████████████████████████████▏  42 GB
pulling 948af2743fc7... 100% ▕████████████████████████████████████████████████████████▏ 1.5 KB
pulling bc371a43ce90... 100% ▕████████████████████████████████████████████████████████▏ 7.6 KB
pulling 53a87df39647... 100% ▕████████████████████████████████████████████████████████▏ 5.6 KB
pulling 56bb8bd477a5... 100% ▕████████████████████████████████████████████████████████▏   96 B
pulling c7091aa45e9b... 100% ▕████████████████████████████████████████████████████████▏  562 B
verifying sha256 digest
writing manifest
success
Error: model requires more system memory (40.4 GiB) than is available (18.2 GiB)

大意就是说，我的系统内存空间不够，需要40。.G system memory，而我只剩下18.2G，实际上我电脑上是32G。

![010.png](https://images.hive.blog/DQmNnTTHGdGKt3LRw3VzCE1mjGT4oUa5F6Wh2QHXi6mdKjg/010.png)

![012 - 副本.png](https://images.hive.blog/DQmYWMApotMQCXF28gP1UHAWJgWssTGLr7zGAaiHMa75LYG/012%20-%20%E5%89%AF%E6%9C%AC.png)
本地暂时体验不了，就通过API接口在vscode下体验下也行
我用的是OpenRouter API


![012.png](https://images.hive.blog/DQmYWMApotMQCXF28gP1UHAWJgWssTGLr7zGAaiHMa75LYG/012.png)

![013.png](https://images.hive.blog/DQmd7otFth3yHtS4ShGgsu3vrfedeVmCtgc81XzVbvhHhrb/013.png)
在vscode下安装插件，实现AI访问

![011.png](https://images.hive.blog/DQmWMBXZeXiF4sXJ4ni1AvEzzW6DSTc4hQgAoNsp3g1rS88/011.png)
还是想用本地llama，毕竟openrouter是要花钱的，本地免费的才香嘛。
没办法，只能退而求次，下载3.2版本试下了。


![014.png](https://images.hive.blog/DQmP71tpuxjQK1gps2NqNdb1WrTjDL3PDae68HqqU6Bf3gr/014.png)
本地安装的是Llama 3.2 Vision，也就是7B这个版本。

![015.png](https://images.hive.blog/DQmUcMKGXja4WFMnWzTAUgg6FBCWD4EnRXgn2UbxyTU1k1e/015.png)
试了下，现在也支持中文了

改天把这个本地安装的llama，也集成到vscode下，这样以后在本地使用AI编程，就不用再另外购买付费版本了。:):):)
