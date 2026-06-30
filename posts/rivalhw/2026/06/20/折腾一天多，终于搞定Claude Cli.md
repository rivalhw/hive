# 折腾一天多，终于搞定Claude Cli

**Author:** @rivalhw  
**Permlink:** claude-cli  
**Created:** 2026-06-20T02:51:39  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "tags": [
    "claude",
    "ai",
    "life",
    "cn-reader",
    "cn"
  ],
  "image": [
    "https://images.hive.blog/DQmTNgZyGizegUMpYc47oBFYrvYotyPgFWDKGYdMELRxpdX/000.png",
    "https://images.hive.blog/DQmYuFadfKwGqN6mAHgXhLbYEo6reEDb2HF1QRHg8gH9dC8/001.png",
    "https://images.hive.blog/DQmc5yHFsrZR7C5FYJ8S18CDPHwcQzzxoJuFJs8jym4yAvi/002.png",
    "https://images.hive.blog/DQmXJgCnxEuoS639bJFFA6pEpooqWcmFjVRMdFwDr6iFqcz/003.png",
    "https://images.hive.blog/DQmdSvqckwRAchPTadXUSYVWP2DZodYwLGHJWz4eAuMnDsr/005.png",
    "https://images.hive.blog/DQmWL1sgt5D3Tozwi85qRmUvH6PvHLWf96egQZH2LeqyKwd/006.png",
    "https://images.hive.blog/DQmWV8x6rvJZkoqiWhu9QtASpzZtu6GgR7dz7ZuwwngrS97/007.png",
    "https://images.hive.blog/DQmZ2JrVHQjsEiiuhwyrfzFU4a26F41r2fVhdiohM3mkBg2/008.png",
    "https://images.hive.blog/DQmX7vxZ4fK1vUrkdYM7dtSCBvrFsLCES3UwaHxWxR3c5rf/009.png",
    "https://images.hive.blog/DQmeB4P2KrKKB2ppy8C5HUo8HFzRTWzWwrTiXbiJe4RDnMK/010.png",
    "https://images.hive.blog/DQmVSgksynaDSV3veAeNHNkNQYEo7mHaPHuwfTRDDV47Mp7/011.png",
    "https://images.hive.blog/DQmbUViH4xotnEoteFLD4bVJHHhrMJxXuPxpYpva19W8Gax/012.png",
    "https://images.hive.blog/DQmUy1UgE1XojCWyQqGJy3YKLUSTyu8SSNGD395GVDLmvpZ/013.png"
  ],
  "format": "markdown"
}

---

我之前用的是Cursor下的Claude大模型，比如Sonnet，Opus等。想用下Claude的code Cli，但是不给用国内呀。

直接通过Claude官网支付这一关肯定通不过，信用卡能直接识别。我想着用Google Pay试下，结果试了下，也能被识别，直接被拒，如下图，


![000.png](https://images.hive.blog/DQmTNgZyGizegUMpYc47oBFYrvYotyPgFWDKGYdMELRxpdX/000.png)

原因也简单，就是用Google Pay的时候，Claude也能识别到卡号，进而判断所在区，被拒绝也是可想而知了。

后来想了个办法，终于搞定了。


![001.png](https://images.hive.blog/DQmYuFadfKwGqN6mAHgXhLbYEo6reEDb2HF1QRHg8gH9dC8/001.png)


![002.png](https://images.hive.blog/DQmc5yHFsrZR7C5FYJ8S18CDPHwcQzzxoJuFJs8jym4yAvi/002.png)

我之前用Claude的时候，总是被弹出要求电话识别，当时一直以为没有电话验证是无法使用的。但其实不然，关键原因就出在这个Ip身上。

没错，你猜的很对，非美区地方，需要电话验证。

但反过来呢，如果是美区，要求就没那么严格了。

于是，我便自己做了个美区的服务器，Ip是真实的美区住宅那种，为了防止IP乱挑引起的风控麻烦，我特意选了个静态固定住宅ip,这样从身份上就完全没问题了。

刚开通pro账户，一通操作猛如虎，忽然发现弹出如下图这个信息，

![003.png](https://images.hive.blog/DQmXJgCnxEuoS639bJFFA6pEpooqWcmFjVRMdFwDr6iFqcz/003.png)

怎么？看这样子是说我快达到限额了？

不理他，继续用。

结果呢，很快就达到满额了。

![005.png](https://images.hive.blog/DQmdSvqckwRAchPTadXUSYVWP2DZodYwLGHJWz4eAuMnDsr/005.png)

看了下，显示是晚上10点会恢复额度。

在输入栏里输入 /usage 就会显示即时额度如下，

![006.png](https://images.hive.blog/DQmWL1sgt5D3Tozwi85qRmUvH6PvHLWf96egQZH2LeqyKwd/006.png)


好吧，那就休息下，等10点后再继续用吧。

10：10刚果，我打开电脑，发现额度恢复了！


![007.png](https://images.hive.blog/DQmWV8x6rvJZkoqiWhu9QtASpzZtu6GgR7dz7ZuwwngrS97/007.png)

都说Claude的大模型很烧token，你看这一个任务跑个十多分钟，能不烧大量Token嘛！

难怪比起Open AI 的codex，感觉Claude的明显消耗的很快了。。。


![008.png](https://images.hive.blog/DQmZ2JrVHQjsEiiuhwyrfzFU4a26F41r2fVhdiohM3mkBg2/008.png)

![009.png](https://images.hive.blog/DQmX7vxZ4fK1vUrkdYM7dtSCBvrFsLCES3UwaHxWxR3c5rf/009.png)

![010.png](https://images.hive.blog/DQmeB4P2KrKKB2ppy8C5HUo8HFzRTWzWwrTiXbiJe4RDnMK/010.png)

![011.png](https://images.hive.blog/DQmVSgksynaDSV3veAeNHNkNQYEo7mHaPHuwfTRDDV47Mp7/011.png)

![012.png](https://images.hive.blog/DQmbUViH4xotnEoteFLD4bVJHHhrMJxXuPxpYpva19W8Gax/012.png)


![013.png](https://images.hive.blog/DQmUy1UgE1XojCWyQqGJy3YKLUSTyu8SSNGD395GVDLmvpZ/013.png)

必须得有一个纯净、稳定的美区环境，后续可以避免被识别到导致账户被封等麻烦事。

据说新开的用户，尽量不要直接购买最贵套餐，以避免容易被识别，我不清楚是不是这回事，但为了稳妥起见，我先用pro一个月，等稳定没问题了再考虑升级吧。

折腾了两天时间，好在最后终于搞定了，真是不容易啊。囧😳
