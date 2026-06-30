# 我的一点经验心得：如何让AI最大效率化

**Author:** @rivalhw  
**Permlink:** 5bbppt-ai  
**Created:** 2026-04-03T03:50:15  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "format": "markdown",
  "image": [
    "https://images.hive.blog/DQme2KQErykBfiReHaHJMM11MRRenhW82fLqEqKMxSg964q/yoshitaka2-ai-generated-8993116_1920.jpg"
  ],
  "links": [
    "https://pixabay.com/users/yoshitaka2-24545143/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=8993116"
  ],
  "tags": [
    "ai",
    "cn-reader",
    "cn"
  ]
}

---

我刚开始用AI的时候，非常热衷于输入一大段提示词，比如：

>你是一名web前端架构和分析工程师，有着非常非常的架构设计经验，擅长使用python和js语言，非常擅长XXX，有着大量丰富的XXX成功经验。。。

或者，

>你是一名三甲医院内科门诊医生，有着非常丰富的临床经验，善于。。。

其实早期AI开始的时候，这种提示词对于AI来说效果确实不错。那个时候的AI有两个问题：

一是过于通用性，如果你给其个专业方向，用起来效果确实比通用无方向效果更好；

二是频繁出现幻觉。所谓的幻觉，就是你在跟AI聊天途中，本来聊的好好的，但AI忽然冒出一些跟聊天内容无关的句子或想法，甚至完全不搭边，让人觉得很困惑。

但是，AI在高速发展了几年后，尤其是去年年底到今年开始，有了突破性的进展，如幻觉这种问题在强模型时基本已很少再犯，至于其它主流的模型，我自己试过几个发现也很少以前类似问题。

前几天的时候，网上曝出claude泄露了部分前端的代码(3月31日，美国大模型头部公司Anthropic 因构建配置失误，意外通过 npm 注册表中的源映射文件泄露了 Claude Code （编程工具）源代码)，发现现在的提示词发展已经到了可以非常粗暴但却效果很明显的地步了。

比如我看到有人贴出了部分的提示词内容，

>IMPORTANT: Go straight to the point. Try the simplest approach first without going in circles. Do not overdo it. Be extra concise.

>Keep your text output brief and direct. Lead with the answer or action, not the reasoning. Skip filler words, preamble, and unnecessary transitions. Do not restate what the user said — just do it. When explaining, include only what is necessary for the user to understand.

>Focus text output on:
>- Decisions that need the user's input
-> High-level status updates at natural milestones
>- Errors or blockers that change the plan

>If you can say it in one sentence, don't use three. Prefer short, direct sentences over long explanations. This does not apply to code or tool calls.

这段提示词的大意就是，

>直奔主题。先尝试最简单的方法，不要兜圈子。不要做得太过。务必简洁

看，高手往往都特别简单和纯粹，没有那么多情绪和琐事。


![yoshitaka2-ai-generated-8993116_1920.jpg](https://images.hive.blog/DQme2KQErykBfiReHaHJMM11MRRenhW82fLqEqKMxSg964q/yoshitaka2-ai-generated-8993116_1920.jpg)
Image by <a href="https://pixabay.com/users/yoshitaka2-24545143/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=8993116">yoshitaka2</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=8993116">Pixabay</a>

我在实践的过程中，也总结出了一些经验，这里顺便分享下：

**1、开发人员要学会从以前的亲历亲为工作，转变身份为指导、监督和审核；**

**2、跟AI沟通过程，尽量简洁、明了，但意思表达一定要准确，千万不要过多花里胡哨的内容；**

**3、做好日志和相应的记录如异常截图等，让AI接管你的工作环境，自行去运行、测试和分析，每次测试后将问题和异常等重新发给AI，让它根据这些内容自行去分析和修复；注意做好监督，如果发现有跟实际不符合，或者明显方向错误，及时纠正它。**

***
总之一句话，**跟AI沟通要简洁准确，尽量给他最大的发挥空间。**还是刚才那句话，**除非它犯错误或者跑偏了，否则不要限制它。**

我发现如果这样做，加上正确的思路，许多你想要做的事情几乎都可以完成。:)
