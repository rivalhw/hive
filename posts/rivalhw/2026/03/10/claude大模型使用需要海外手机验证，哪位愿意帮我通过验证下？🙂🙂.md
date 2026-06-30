# claude大模型使用需要海外手机验证，哪位愿意帮我通过验证下？🙂🙂

**Author:** @rivalhw  
**Permlink:** 4hcd7s  
**Created:** 2026-03-10T08:42:24  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "format": "markdown",
  "image": [
    "https://images.hive.blog/DQmTb71gARCq1DQAMcFadDP7ARECq1EjqSrgbVKj1dTX8jw/image.png",
    "https://images.hive.blog/DQmULyJ63MJdsSp1otxX8XHYhCLGqijMzq3WEK1f3vYr7RK/image.png",
    "https://images.hive.blog/DQmb9hHX44ze7NLPJvG6CR2PhoxMoVBqLQi3bxaX2ds1uTU/image.png"
  ],
  "links": [
    "http://127.0.0.1:7890"
  ],
  "tags": [
    "ai",
    "gpt",
    "cn-reader",
    "cn"
  ]
}

---

openAI最新的大模型gpt-5.4出来了，我这两天用了下，感觉挺不错，说说自己的感受。

在gpt-5.4出来之前的前几天，不知道是怎么回事，我在用chatGPT网页版本的时候，明显能觉得性能比之前差许多，给出的回答质量显然无法跟先前相比，只是我最近用网页版较少，就没太在意。

嗯，跑题了，说说gpt-5.4吧，我这里主要谈其code和推理能力，个人感受比先前的5.3要好一点，但要说好很多，显然这话我说不出口，事实就摆在那里嘛，我甚至怀疑这gpt-5.4是openAI放出的专门针对claude的“无奈之举”吧。囧

当然，gpt-5.4在合规方面似乎放松了些，至少我在用的时候，发现不像5.2和5.3时动不动就收到不合规的信息，我用的是cursor客户端，不知道是不是跟在cursor提示词做了优化有关，这个只是我的一些猜测。

我用的cursor客户端，使用claude 的optus 4.6 和 gpt5.4消耗的token太大了，随便一个问题提过去，几美刀就不见了，弄得我现在感觉一天小心谨慎，完全没了之前使用大模型那种“洒脱”，隔一阵子就刷新看下usage，看下有没哪次请求过大导致消耗token太多？尽管我如此“省吃俭用”，这个月才过去了1/3不到，我看了下账单已经有67刀了，

![image.png](https://images.hive.blog/DQmULyJ63MJdsSp1otxX8XHYhCLGqijMzq3WEK1f3vYr7RK/image.png)

有朋友推荐说有OpenCode,我尝试安装了下，用的是openrouter的api，



初开始，虽然能用默认大模型，但像optus等用不了，后来发现问题是OpenCode默认走的是本地网络，需要强制其使用VPN端口流量，如，

>set http_proxy=http://127.0.0.1:7890
set https_proxy=http://127.0.0.1:7890


![image.png](https://images.hive.blog/DQmb9hHX44ze7NLPJvG6CR2PhoxMoVBqLQi3bxaX2ds1uTU/image.png)


尝试用了下，发现如果只是做一般的工作，还可以。但是如果较为频繁的使用，就会发现稳定性很不友好，时不时会出现中断，这既影响效率，又影响心情。

显然，OpenCode目前还有不少的问题，等到日后稳定了再考虑吧。

claude 在国内是被禁止使用，是这家企业不给我们用。网上有一些折中的方法，但是我觉得不是很好，如果能直接使用其官方订阅，是非常不错的。


![image.png](https://images.hive.blog/DQmTb71gARCq1DQAMcFadDP7ARECq1EjqSrgbVKj1dTX8jw/image.png)
卡在海外手机验证这里

可惜，官方订阅需要个国外手机号码验证，我没国外的手机号码，没法做这个验证，只能眼睁睁看看。

就是需要验证下手机通过下身份，支付都是绑定我自己的卡。哪位朋友如果知道这个操作是安全的，并且愿意给些这方面帮助，提供手机号码帮验证下？这里深表感谢了！！！

嗯，香港的手机号码不行，也被限制的。

大（强）模型好用，就是太贵。何况像optus这种，你想付费给对方钱，人家还不收。。。

看有些商家吹嘘自己的大模型多么牛逼。。。有时也是挺无语的。。。东西好不好用，得顾客说了算吧？如果真做到想gpt和claude这样效果，客户觉得好，追着要付费购买，那才真的说明你的产品好，而不是在那里自卖自吹。。。
