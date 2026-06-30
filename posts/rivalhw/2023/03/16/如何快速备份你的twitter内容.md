# 如何快速备份你的twitter内容

**Author:** @rivalhw  
**Permlink:** 6hppuz-twitter  
**Created:** 2023-03-16T02:07:54  
**Category:** hive-105017  
**Tags:** {
  "tags": [
    "twitter",
    "backup",
    "github",
    "cn-reader",
    "cn",
    "tips"
  ],
  "image": [
    "https://images.hive.blog/DQmbumBV5eurvTJuCbCaXHm9VgbXXNDKi9toSFEkg1NVTS6/001.png",
    "https://images.hive.blog/DQmZQNeB6BJXwoW17Vujged9vjFknWZqqf1wYwmpv2ACiRY/002.png",
    "https://images.hive.blog/DQmWAXUTXareeee9vAiGB1dpT68epA3dAQVYhPB1oM8Ei76/003.png",
    "https://images.hive.blog/DQmNzZrXMGADAVxd28jh7Gs9Hy2i9hWLFQpJjqUZi7ffNvu/image.png",
    "https://images.hive.blog/DQmU2CUd6zGpHcN8Pos8NGUGAXAu84EvunzsH7VdxTdJctz/image.png",
    "https://images.hive.blog/DQmW5vhYpdUzbp13CpsCGqdXWHcTNoyHySW4iVYxpkkro9p/image.png",
    "https://images.hive.blog/DQmP2kKdQL2Ygn8CU2KUwmG3mf85dnRFGNcs15mmpB8F2Vd/image.png",
    "https://images.hive.blog/DQmXjyp9uo61KpGmiak2M8mJn9pFkqDvFzXSRjN2KHwyeBg/image.png"
  ],
  "links": [
    "https://github.com/yihong0618/GitHubPoster"
  ],
  "app": "hiveblog/0.1",
  "format": "markdown"
}

---

我用twitter，其实时间挺早的。早到什么时间已经记得不太清晰，但肯定是比国内的新浪微博还要早些。事实上，在新浪微博(大概是2010年左右吧)之前，国内还出过一个类似微博的软件，名字我已经记不清楚了(貌似记得叫：嘀咕 digu)，我大约用了1、2年吧，而且那个软件非常方便，从一开始，它就提供手机版，嗯，我用诺基亚的手机就可以在上边发文，发图片。。。

　　可惜新浪微博崛起后没两年，那个微博软件估计用的人少了，后来慢慢就彻底消失。

　　我后来使用twitter，刚开始twitter国内还是可以访问的，不仅twitter，其它的比如google等，也是后来在2010年才退出大陆，紧跟着无法访问了。

　　twitter最吸引我的，就是在上边可以看到许多各种各样的信息，当然，这其中不乏一些我不喜欢，甚至有些讨厌的内容，但这没关系，也不影响我对它的喜欢，毕竟，我使用它，除了想多了解不同地方的风土人情之外，另外一个很重要的原因，就是也想多了解不同地方人的不同观点。

　　我的座右铭之一，就是不一定同意你的观点，但我还是想多了解下你的想法，这样做我认为最大的好处，就是极大避免自以为是，让自己的思想陷入僵局。

　　twitter在国内被墙后，我用的就很少了，前两年的时候，有次好久没登陆，便想上去看看，结果发现，自己的twitter账户下，不知道何时被“发布”了许多垃圾内容，绝大多数都是类似那种色情的图片等，我很快意识到，我的账户被黑了。

　　后来查看了下，果不其然，账户的确是被黑了，也因为垃圾内容，账户被twitter临时冻结，我为此还专门发邮件去twitter申诉，最后的结果自然是好的，账户被追回。

　　为了避免以后类似事件再发生，我当即除了改密码之外，另外设置了安全策略，其实就是手机二次验证，自此，我认为可以高枕无忧。

　　前几天的时候，我登录twitter，发现被提示，

>只有 Twitter Blue 用户可以使用短信双因素认证方法。只用几分钟就能将它删除。

我记得Twitter Blue 用户貌似是要收费的，这就让人觉得很奇怪了，用个双重验证，还要额外收费？

![001.png](https://images.hive.blog/DQmbumBV5eurvTJuCbCaXHm9VgbXXNDKi9toSFEkg1NVTS6/001.png)

看到下边这句，就更郁闷，
>为了避免失去对 Twitter 的访问权限，请通过 2023年3月19日 删除短信双重身份验证。

那就取消呗，反正我用的也很少了。


![002.png](https://images.hive.blog/DQmZQNeB6BJXwoW17Vujged9vjFknWZqqf1wYwmpv2ACiRY/002.png)

![003.png](https://images.hive.blog/DQmWAXUTXareeee9vAiGB1dpT68epA3dAQVYhPB1oM8Ei76/003.png)


想了想，怎么把twitter上的一些信息保存下来，即便这些信息似乎已经无关紧要。

恰好在网上看到这样一个软件，可以快速将你的twitter内容备份下来。

就是操作稍微麻烦了些，我试了下，最简单的步骤方法图下，

1、fork  [GitHubPoster](https://github.com/yihong0618/GitHubPoster)
![image.png](https://images.hive.blog/DQmNzZrXMGADAVxd28jh7Gs9Hy2i9hWLFQpJjqUZi7ffNvu/image.png)

2、设置github权限(Configuring the default GITHUB_TOKEN permissions ) 如下操作图示，

![image.png](https://images.hive.blog/DQmU2CUd6zGpHcN8Pos8NGUGAXAu84EvunzsH7VdxTdJctz/image.png)
这一步详细操作也可以[猛击这里查看](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#configuring-the-default-github_token-permissions)

3、按照如下图，找到 Twitter Back Up按钮

![image.png](https://images.hive.blog/DQmW5vhYpdUzbp13CpsCGqdXWHcTNoyHySW4iVYxpkkro9p/image.png)

4、按图示输入你要备份的twitter账户名称(不需要登录)，然后点击 Run workflow

![image.png](https://images.hive.blog/DQmP2kKdQL2Ygn8CU2KUwmG3mf85dnRFGNcs15mmpB8F2Vd/image.png)

5、等待显示完成后，即可查看，推特备份记录在 OUT_FOLDER/${twitter_user_name}.txt 中。

我看了下，这个软件不仅支持twitter备份，还支持许多知名平台，如下图，


![image.png](https://images.hive.blog/DQmXjyp9uo61KpGmiak2M8mJn9pFkqDvFzXSRjN2KHwyeBg/image.png)

...

这真是不错啊，有空了继续去研究下。
