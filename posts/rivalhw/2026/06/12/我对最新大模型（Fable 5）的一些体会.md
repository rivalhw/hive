# 我对最新大模型（Fable 5）的一些体会

**Author:** @rivalhw  
**Permlink:** fable-5  
**Created:** 2026-06-12T02:00:12  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "tags": [
    "fable5",
    "ai",
    "llm",
    "cn-reader",
    "cn"
  ],
  "image": [
    "https://images.hive.blog/DQmYdXpcn97ZQNYfNdzDiA1JS5RFq2WK6Q3VLpc8BNGpaxg/marvinbla-bird-10323076.png"
  ],
  "links": [
    "https://pixabay.com/users/marvinbla-19861252/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=10323076"
  ],
  "format": "markdown"
}

---

两天前的时候，收到邮件，说最新的 Claude Fable 5 现在可以用了，邮件里还提了下，

>Anthropic's most powerful generally-available model.

意思是说，这个最新的模型（Fable 5）是 Anthropic 当前公开可用的最强大模型。

Anthropic 旗下之前有两个公开的大模型Sonnet 4.6 和 Opus4.7 ，属于目前市场上的主流模型，效果的确是很不错的。

而这次推出的Fable 5 ，以我这两天的实际使用体验来看，比 Sonnet 4.6 效果更好。

那么问题来了，具体好在哪里？

我认为其一就是新的Fable 5 的逻辑能力比Sonnet 4.6更强。从我使用来看，Fable 5可以做到之前Sonnet 4.6没解决的问题，至少是Sonnet 4.6没有主动帮我提出并解决，这点是主要优点。

其次，Fable 5  相比Sonnet 4.6，在一些问题的判断和看法上，更能给出准确的意见，更不会像其他一些模型那样只会捧杀和吹水，实则非但于解决问题无用，有时候反而容易误导用户。

Fable 5 相比Anthropic 的其他大模型，在安全策略上做了限制，比如在使用过程中，可能会收到类似如下信息，

>Fable 5 hit a safety filter, and the conversation was automatically switched to Claude Opus 4.8. Start a new conversation to continue with Fable 5, or continue this conversation with Claude Opus 4.8.

大意是说，Fable 5 触发了安全过滤机制，因此当前对话已自动切换至 Claude Opus 4.8。

我使用大模型，不会去看所谓的“跑分榜”，因为跑分榜以一来对我无用，二来那玩意很容易造假。就像前些年移动互联网兴起时，国内一些手机厂商总喜欢公布自己最新手机的跑分指数，并以此为耀。但明眼人一眼就能看出，跑分榜那玩意，太容易造假，只能当参考，绝对不能做依据。

我使用大模型，最关注的就是其实际解决问题的能力。你说某个大模型好，但我实际使用后，发现其只是夸夸其谈东拉西扯，说了一大堆废话，但最后问题越解决越麻烦，索性放弃。

而真正好的大模型，并不会将关注力放在如何取悦用户，而是将重心放在聚焦用户的关注点和实际解决问题点上，一个问题抛给大模型后，它不但分析问题本身，也会分析用户的要求，实事求是，而不是一味的取悦用户。说到这点，我认为国内大模型在这点上做的实在是太过分了，有时候为了讨好用户简直就是在一本正经地胡说八道嘛。

当然，大模型的缺点也是很多。我认为大模型最大的问题，还是那个老生常谈的，就是幻觉。

我开始用大模型的时候，被它的思路构架、写代码能力等深深震撼，但时间久了，发现问题来了了，尤其是你要完成一个复杂的，需要不断迭代的项目时，大模型的幻觉劣势非常明显。

网上有流传一个笑话，说你在.md里硬性要求大模型每次输出内容时，先叫声爸爸。

这看起来似乎是个笑话，但懂的人自然明白，这不是笑话，而是针对“幻觉”的一个很接地气的解决方法。试想，一旦发现某次大模型开始不叫爸爸了，那就可以断定这家伙出现了幻觉，思路紊乱。这个时候就要重新将你最核心的问题和要求重新梳理，避免大模型在“幻觉”的路上越走越偏。


![marvinbla-bird-10323076.png](https://images.hive.blog/DQmYdXpcn97ZQNYfNdzDiA1JS5RFq2WK6Q3VLpc8BNGpaxg/marvinbla-bird-10323076.png)
Image by <a href="https://pixabay.com/users/marvinbla-19861252/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=10323076">marvinbla</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=10323076">Pixabay</a>

有人曾举过一个很切合实际的例子,

>大模型好比炒菜，如果你放任它自发完成任务，它会为了给你炒一盘鸡蛋西红柿而把整个厨房炸掉，然后问你「你就说鸡蛋西红柿好不好吃吧。」大部分人上手用 AI 做项目，一开始都失败在这里：它创造出了一个可用的东西，但混乱的成长速度压过了功能的成长速度，然后在某一个崩溃成一团无法修复的乱麻，治丝益棼

说到底，现在跟大模型打交道，做的最多的，就是在纠正大模型，不断给它擦屁股，防止它跑偏，防止它搞错，更要防止它“自作聪明”搞乱搞砸你的项目。

最后说一点，昨天看到一篇新闻，大意是说 Anthropic  公司为了防止有人利用其最新大模型Fable 5训练AI，一旦发现就自动降智。。。

再设想下，这些企业利用自己研发的大模型在背后作更大的恶，一直没被发现呢？？

我想说的是，比起人工智能带给我们的焦虑，大模型这种运作背后的企业黑箱操作，才是最应该令我们警惕的。
