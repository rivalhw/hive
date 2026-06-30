# 用AI改进了打包下载Hive上的文章

**Author:** @rivalhw  
**Permlink:** ai-hive  
**Created:** 2026-04-04T07:54:48  
**Category:** hive-105017  
**Tags:** {
  "tags": [
    "hive-105017",
    "hive",
    "ai",
    "tools",
    "cn-reader",
    "cn"
  ],
  "image": [
    "https://images.hive.blog/DQmSTioSreiXh6PqDwYqr8f5A3nNWGqAHDv63GDL3N66S8i/image.png",
    "https://images.hive.blog/DQmW5dU3CUanHkDiY2aAJawxHmB3Vr7pEntMNK6PVgwy4Z4/001.png",
    "https://images.hive.blog/DQmNpnNFL7U2phmUu42PNfWbkWZTQakvRUiuwt7zdAA7BZ9/002.png",
    "https://images.hive.blog/DQmPKpDRvEucu5hCR9oDdRWQSK2PfkaGkTJPQZfD97vQSAJ/003.png",
    "https://images.hive.blog/DQmYSUqyHeEXFfD686uc4zqxV1FdFp1GFTdoi3HaMTaPS3B/004.png",
    "https://images.hive.blog/DQmf5DHSTqd5K3kKY1NRBRvTYByaTia36bsKhZApKzZNUsq/005.png",
    "https://images.hive.blog/DQmbujXNaA4X6ydM6ChRR9yoSAnx9KCgNK6rdSBAPTo6FQX/006.png",
    "https://images.hive.blog/DQmeeWVzcp2JKdVpxGfG82KHUhTWGJpq9xSvY2Qp4YuVyEp/007.png",
    "https://images.hive.blog/DQmS51YZYJCAoFGeNoJ1no9E4DNoYD7FTpv8PoCqRwfG4mr/008.png",
    "https://images.hive.blog/DQmbsuB69HbqHXj8kuwCtFduWii7zXToXCEV2afhVrLAq1H/009.png",
    "https://images.hive.blog/DQmTYbHuJWc92zneDEcyt84LiBVg7DNzur9rFxJpCmT6ZPM/010.png",
    "https://images.hive.blog/DQmRx2q6YL9DkA1djPt563S8ksNuuRGxMcD7qDuLLGcQjvk/011.png",
    "https://images.hive.blog/DQme4UoK93m8uL9ZgXTZ1HzHUwh7z5rHR3s4iTRMHSkezQQ/012.png",
    "https://images.hive.blog/DQmRF73gTAkBpeKP5RNpwYSFeQjm1uCxbSyvJ7XgKuyek7q/013.png",
    "https://images.hive.blog/DQmP4TehH4o8T5MmSH6PVDKQGjm9UydXwx9bTGwAMsPkzDX/014.png",
    "https://images.hive.blog/DQmYUTqky7tRGp9B2BVCv3Fu9QrZefoP1GTJNP3GtCu4jBH/015.png",
    "https://images.hive.blog/DQmaobokY2cRbmGeggunEE4kNwpgG8aapnL9hqX3YpFm1vW/016.png",
    "https://images.hive.blog/DQmdVuxAGBz5EE28bRdrvJHv64iyB99XDYcpShTxQNriCue/018.png",
    "https://images.hive.blog/DQmNQGB5QjmZsXKj35rreXr3PSRn5wXgGRNXmtUoR6YosjE/image.png"
  ],
  "links": [
    "https://hive.blog"
  ],
  "app": "hiveblog/0.1",
  "format": "markdown"
}

---

我之前不是用AI辅助写了个下载https://hive.blog 上文章的程序嘛，那个是用的网络抓取方式，就是模拟网络访问，逐个去下载，虽然能用，但速度实在太慢，效果也不好。

![image.png](https://images.hive.blog/DQmSTioSreiXh6PqDwYqr8f5A3nNWGqAHDv63GDL3N66S8i/image.png)

昨天忽然想到，可以用hive.io 的API方式直接下载。刚好前几天的时候，我开通了kimi的cli 会员，想到这里，便打开了kimi cli，尝试了下。

首先我将现有的API文档地址，以及自己的要求告诉给它，

>https://developers.hive.io/ 
这个是hive网站的完整API和文档，你根据这个写一个程序，实现通过输入API来下载某个指定账户下的全部或指定日期期间的文章。


![001.png](https://images.hive.blog/DQmW5dU3CUanHkDiY2aAJawxHmB3Vr7pEntMNK6PVgwy4Z4/001.png)


kimi很快帮我完成了初个版本。

不过我给它提了几个要求，让生成的效果更符合我的想法，

>下载为markdown格式，多线程下载，下载后按照账户名称/年/月/日保存，文件名按照原先不变。


![002.png](https://images.hive.blog/DQmNpnNFL7U2phmUu42PNfWbkWZTQakvRUiuwt7zdAA7BZ9/002.png)

![003.png](https://images.hive.blog/DQmPKpDRvEucu5hCR9oDdRWQSK2PfkaGkTJPQZfD97vQSAJ/003.png)

![004.png](https://images.hive.blog/DQmYSUqyHeEXFfD686uc4zqxV1FdFp1GFTdoi3HaMTaPS3B/004.png)

![005.png](https://images.hive.blog/DQmf5DHSTqd5K3kKY1NRBRvTYByaTia36bsKhZApKzZNUsq/005.png)

![006.png](https://images.hive.blog/DQmbujXNaA4X6ydM6ChRR9yoSAnx9KCgNK6rdSBAPTo6FQX/006.png)

![007.png](https://images.hive.blog/DQmeeWVzcp2JKdVpxGfG82KHUhTWGJpq9xSvY2Qp4YuVyEp/007.png)

搞好了，现在运行看下效果！🤣


![008.png](https://images.hive.blog/DQmS51YZYJCAoFGeNoJ1no9E4DNoYD7FTpv8PoCqRwfG4mr/008.png)

![009.png](https://images.hive.blog/DQmbsuB69HbqHXj8kuwCtFduWii7zXToXCEV2afhVrLAq1H/009.png)

因为采用了多线程，下载的速度还是蛮快的。我看了下，我从2016年开始的写的文章，大约几分钟就全部下载完成了。

这速度比通过网络访问抓取明显高效多了，而且还稳定可靠！


![010.png](https://images.hive.blog/DQmTYbHuJWc92zneDEcyt84LiBVg7DNzur9rFxJpCmT6ZPM/010.png)
下载下来的文章，自动按照年/月/日保存到文件夹下


![011.png](https://images.hive.blog/DQmRx2q6YL9DkA1djPt563S8ksNuuRGxMcD7qDuLLGcQjvk/011.png)

打开看下最新的文章，格式是Markdown，不错！

程序的源码截图，


![012.png](https://images.hive.blog/DQme4UoK93m8uL9ZgXTZ1HzHUwh7z5rHR3s4iTRMHSkezQQ/012.png)

![013.png](https://images.hive.blog/DQmRF73gTAkBpeKP5RNpwYSFeQjm1uCxbSyvJ7XgKuyek7q/013.png)

看了下，下载下来的文章名称，是按照地址栏里的英文来编号，这个不太好，要改成对应的中文文章名称。

让AI再修改下。


![014.png](https://images.hive.blog/DQmP4TehH4o8T5MmSH6PVDKQGjm9UydXwx9bTGwAMsPkzDX/014.png)

这次AI显然误解了我的意思。我本意是想让它帮我把程序改为按照文章中文名称保存，结果它理解成将刚才已下载的文章转换成中文名称，并帮我重新写了个新的程序专门用户转换。

好吧，念你一片好心，我就不追究你的过错了。

重新再来一次，这次我把意思表达清楚了。


![015.png](https://images.hive.blog/DQmYUTqky7tRGp9B2BVCv3Fu9QrZefoP1GTJNP3GtCu4jBH/015.png)
重新修改之后，我一时贪快，把多线程从默认的8个改成16个，结果发现因为请求过多导致被API节点拒绝，频繁出现一些错误。



![016.png](https://images.hive.blog/DQmaobokY2cRbmGeggunEE4kNwpgG8aapnL9hqX3YpFm1vW/016.png)


![018.png](https://images.hive.blog/DQmdVuxAGBz5EE28bRdrvJHv64iyB99XDYcpShTxQNriCue/018.png)
好吧，重新改回默认的8个线程就妥了。

修改好的程序，我放到了[github.com代码仓](https://github.com/rivalhw/hive) 了，如下图，


![image.png](https://images.hive.blog/DQmNQGB5QjmZsXKj35rreXr3PSRn5wXgGRNXmtUoR6YosjE/image.png)

有了这款工具，这下保存自己的文章就方便多了。有需要的朋友可以自己下载，如果不懂程序，但想要下载打包自己的文章，后续我再考虑做个在线版本，这样只要输入自己账号，就自动打包和下载好了。🤣🤣🤣
