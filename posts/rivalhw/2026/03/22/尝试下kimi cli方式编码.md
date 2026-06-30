# 尝试下kimi cli方式编码

**Author:** @rivalhw  
**Permlink:** kimi-cli  
**Created:** 2026-03-22T04:28:03  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "format": "markdown",
  "image": [
    "https://images.hive.blog/DQmZFSeZ6Shid97QAtmwBwYv83QhiJtgELwvsQMMRFEJiPB/001.png",
    "https://images.hive.blog/DQmTaW12zHJVBS2iZn5n2THmNv5e1AHZGYGBpSBE3Er2hL4/002.png",
    "https://images.hive.blog/DQmWtkVjRBpqsrNvmoG3iaRhUANdmjjaHDNyR2ANr4SjfPV/003.png",
    "https://images.hive.blog/DQmR1JdpbZSPbHguJEM9gdX3rBvAsGSjPMaC86rWZqZsozu/004.png",
    "https://images.hive.blog/DQmWC9BbhHXaH2PMehFcPWHm3pQ7TRsX5xkpVfsiTb7y2he/image.png",
    "https://images.hive.blog/DQmbE2PKHAT1poRGj4izaJriS12ucofJd2NmbNoYhKZNsDs/IMG20260319092853.jpg",
    "https://images.hive.blog/DQmPmFDDPHMRb3TSdFyQTVFCZ18sYfZGCda5ABSyKDYmq8Z/IMG20260322111004.jpg"
  ],
  "tags": [
    "ai",
    "cli",
    "kimi",
    "tools",
    "cn-reader",
    "cn"
  ]
}

---

我一直用IDE软件进行编码，已经习惯了，但AI大模型的发展之快，让我现在感觉到传统的IDE编码方式已经快要失去了其原有的意义，比如传统IDE的回滚(退回)功能，在AI编程下几乎没有了意义，至于其它的语法检测、代码补全等都是同样的道理，当然，最主要的就是AI编程，已经彻底改变了原先的人工编程方式。

这两天看到Cursor新推出了最新的Composer 2大模型。Composer 1.5我一直就有在用，怎么说呢，速度方面绝对是没问题，很快。在一些推理方面也不错。但是呢，总感觉发挥不稳定，偶尔也会出现一些推理莫名其妙的，需要人工进行纠正。

至于Composer 1.5跟gtp5.3 或者claude optus4.6 ，那根本没法比，不在一个重量级上。

但是，实话实说，用 Composer  1.5进行一般的逻辑推理，性能和质量是足够了，更关键的是，费用比optus等要便宜不知道多少倍。

嗯，这次看到 新推出 Composer 2.0,我昨天就马上尝试了下，速度依旧很快，但是嘛，发现依旧是在合规方面做了很多增加，导致用起来比之前明显不爽了许多。

据说 Composer 2.0里边用了kimi2.5大模型，我心想，与其那样，那我还不如直接用kimi不更好？

说干就干，去kimi网站上，直接下载了cli ,安装后直接在终端下使用，我以前很少用终端进行编码，这次用了下，发现比IDE方便和爽多了。

开始安装时，终端总是出现闪退，我用AI查了下，说是问题出在：

>PowerShell requires an execution policy in [Unrestricted, RemoteSigned, Bypass]

说白了就是，当前 PowerShell 执行策略禁止运行安装脚本（uv 安装器被拦截）

解决的方法也很简单，直接运行如下命令：

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

我尝试用cli方式完善下我之前写的那个工具，


![001.png](https://images.hive.blog/DQmZFSeZ6Shid97QAtmwBwYv83QhiJtgELwvsQMMRFEJiPB/001.png)


![002.png](https://images.hive.blog/DQmTaW12zHJVBS2iZn5n2THmNv5e1AHZGYGBpSBE3Er2hL4/002.png)


![003.png](https://images.hive.blog/DQmWtkVjRBpqsrNvmoG3iaRhUANdmjjaHDNyR2ANr4SjfPV/003.png)


![004.png](https://images.hive.blog/DQmR1JdpbZSPbHguJEM9gdX3rBvAsGSjPMaC86rWZqZsozu/004.png)


![image.png](https://images.hive.blog/DQmWC9BbhHXaH2PMehFcPWHm3pQ7TRsX5xkpVfsiTb7y2he/image.png)

看下修改后的程序，让其运行后，处理图片后的效果，如下图，



![IMG20260319092853.jpg](https://images.hive.blog/DQmbE2PKHAT1poRGj4izaJriS12ucofJd2NmbNoYhKZNsDs/IMG20260319092853.jpg)

![IMG20260322111004.jpg](https://images.hive.blog/DQmPmFDDPHMRb3TSdFyQTVFCZ18sYfZGCda5ABSyKDYmq8Z/IMG20260322111004.jpg)
嗯，这两张照片，是我在路边抓的蝴蝶，随手拍的图片。

哇，效果还不错嘛！

看来，传统的IDE编程方式要没落了，以后我也要改用这种cli方式编程了。:)
