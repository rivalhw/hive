# 如何让喂给AI大模型的数据更安全（脱敏）？

**Author:** @rivalhw  
**Permlink:** 5eg82z-ai  
**Created:** 2026-05-03T09:22:39  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "tags": [
    "ai",
    "llm",
    "cn-reader",
    "cn"
  ],
  "image": [
    "https://images.hive.blog/DQmV6tKzr14CLF4B26jmyQeVPhE6c1728T2eCbUkYgomEwA/image.png",
    "https://images.hive.blog/DQmRkYxmAb3R7ZXz7GnSMBWNqXFF7pLKogiRgqPhVef3eas/001.png",
    "https://images.hive.blog/DQmNbSV5F7FMtBREJeuomoqDj6s3ZfBNKLvEefLM8Hg213Z/002.png",
    "https://images.hive.blog/DQmWCVuMgbuUZK4i9ikrL7XyUQV3pAxuz3ofvBiq8kP5msM/003.png",
    "https://images.hive.blog/DQmeJTxnoFRNWfe88LscWg83ejYSDAoXPtpY5X2QUoMWu2H/5a620e8b6e63ab990ebb47d3a6dac246.png",
    "https://images.hive.blog/DQmaLhjScKQymM2XZiM3f8y424PVk5ahD1pZhVbRj1YJdCZ/image.png"
  ],
  "links": [
    "https://github.com/openai/privacy-filter.git"
  ],
  "format": "markdown"
}

---

在如今这个AI几乎无处不在的时代，使用AI既是趋势，也是当下的一种热门和常见。

但是，有一个问题不知道大家有没想过，每当我们输入自己想要的内容给AI时，一些敏感的数据同样也会暴漏给AI背后的大模型。如果一些不良的商家拿这些数据再去训练，必然会造成安全和个人隐私方面的一些问题。

哦，也许有人会说，这些AI大模型企业不是说了，这些数据不会被用来训练吗？

呵呵，这些话根本不足为信。

很简单的一个道理，之前大模型用来训练的很多数据，都是来源于一些主流平台，那些平台也做了不准爬取的限制，但是结果又如何呢？还不是照爬不误。

有些平台上的内容比如git上的一些私人仓库，都被拿去做训练了。可见，所谓的隐私和限制，在这些大模型跟前完全如同纸糊的浆糊，熟视无睹。


![image.png](https://images.hive.blog/DQmV6tKzr14CLF4B26jmyQeVPhE6c1728T2eCbUkYgomEwA/image.png)


![001.png](https://images.hive.blog/DQmRkYxmAb3R7ZXz7GnSMBWNqXFF7pLKogiRgqPhVef3eas/001.png)


![002.png](https://images.hive.blog/DQmNbSV5F7FMtBREJeuomoqDj6s3ZfBNKLvEefLM8Hg213Z/002.png)

![003.png](https://images.hive.blog/DQmWCVuMgbuUZK4i9ikrL7XyUQV3pAxuz3ofvBiq8kP5msM/003.png)

chatGPT、codex等下也有所谓的临时聊天，隐私保护模式，但根本不足为信

既然这样，我们在跟AI打交道的过程中，就要注意避免将隐私或重要数据发给它。

日常的沟通交流还好说，但碰到一些文件内容处理，就很难避免了。通常做法就是将文件一股脑丢给AI，至于里边有没有敏感或重要数据，有时候还真顾不上查看了。

好在有个privacy-filter （隐私过滤），专门用来脱敏敏感数据。

所谓脱敏，这是专业的一个叫法，通俗地讲，就是把你文件里涉及到的一些敏感数据，比如给客服记录、医疗档案、金融日志去隐私化，才能拿去分析或共享。

这样我们在发给AI大模型前，先用这个privacy-filter （隐私过滤）简单过滤下即可。

嗯，privacy-filter （隐私过滤） 是本地安装的，也就是说，本地处理完成，不涉及联网。

安装的方法很简单：

##### 1. 进入你想放项目的目录（比如 C:\git）
cd C:\git

##### 2. 克隆项目
git clone https://github.com/openai/privacy-filter.git

#####  3. 进入项目目录
cd privacy-filter

#####  4. 安装（这时当前目录下有 setup.py 或 pyproject.toml）
pip install -e .

##### 5. 验证安装
opf "Alice was born on 1990-01-02."

安装完成后，使用非常简单，就是调用 opf即可，如下，

>opf "Alice was born on 1990-01-02."


![5a620e8b6e63ab990ebb47d3a6dac246.png](https://images.hive.blog/DQmeJTxnoFRNWfe88LscWg83ejYSDAoXPtpY5X2QUoMWu2H/5a620e8b6e63ab990ebb47d3a6dac246.png)

第一次运行时，因为要下载大模型，因此慢些。

我尝试了下，

>PS C:\git\privacy-filter> opf --device cpu 'username: rivalhw password: 123456'

>username: <PRIVATE_PERSON> password: <SECRET>

用项目自带的文件再测试下直接过滤文件，

>opf --device cpu C:\git\privacy-filter\examples\data\sample_eval_five_examples.jsonl


![image.png](https://images.hive.blog/DQmaLhjScKQymM2XZiM3f8y424PVk5ahD1pZhVbRj1YJdCZ/image.png)

有了privacy-filter ，下次再有大文件丢给大模型前，用它来帮你过滤（脱敏）下就放心多了。:)

戏剧的是，这个 privacy-filter 竟然还是 OpenAI它自己推出的。。。囧
