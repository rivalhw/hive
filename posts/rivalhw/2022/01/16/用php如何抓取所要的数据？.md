# 用php如何抓取所要的数据？

**Author:** @rivalhw  
**Permlink:** php  
**Created:** 2022-01-16T02:47:45  
**Category:** hive-105017  
**Tags:** {
  "tags": [
    "php",
    "program",
    "code",
    "life",
    "cn"
  ],
  "image": [
    "https://images.hive.blog/DQmZhZkfVHVss2WosRE58kUZUBQoD6A51Zjt24yAk7PqEm7/image.png",
    "https://images.hive.blog/DQmUpgscg2WfjWDadxjBW9EBBtoGxkFpkGzsVsrTWifdEPx/image.png",
    "https://images.hive.blog/DQmYT1bPkD7b6GTyhcuzz3ZDqvpntC6VnbUxaKQLx48YHUZ/image.png",
    "https://images.hive.blog/DQmW2jw7GUXTiZrLWcbzLMTwFMvKr5Th9xF63zB5XnVwLCt/image.png",
    "https://images.hive.blog/DQme9zbBm3RBM8tDUrHLXDehVLB9P7Y8vjwDjNRz1WDhr1V/image.png",
    "https://images.hive.blog/DQmaTTGHdTq7dLfQq4y3tuiJJmjxSnkx459BcshjHtTBTVz/image.png",
    "https://images.hive.blog/DQmWaDwSfXsYCWj7f2fVZ7UxTn1gN8hbhkR3MHhSzD5mM8H/image.png",
    "https://images.hive.blog/DQmXuUxfS5ju83ucvph4W3AMAmWwa6zn4kXU7e7uYQYMRXF/image.png",
    "https://images.hive.blog/DQmaZSAF1p2wZLqS5Gt5DCimFuWXnYL5v5QL1Pehw7VB8Hr/image.png",
    "https://images.hive.blog/DQmW3NR1hn5L8dtzjka6hYLgZrHjVNyZtV1indVuKbCcRhc/image.png"
  ],
  "app": "hiveblog/0.1",
  "format": "markdown",
  "author": "rivalhw"
}

---

跟几个朋友一起吃饭的时候，其中有一位朋友问我，能不能拿到那个数据？

　　朋友口中所说的那个，就是香港六合彩。

　　虽说六合彩在大陆不合法，但在香港可是公开合法的，拿到其历年来的历史数据，应该还是有把握的。

　　我在网上搜索了一阵子，找到这样一个网站，

　　![image.png](https://images.hive.blog/DQmZhZkfVHVss2WosRE58kUZUBQoD6A51Zjt24yAk7PqEm7/image.png)

　　上边有六合彩历年来的数据，但怎样才能把这些数据整理出来呢？如果靠手工整理，一是工作任务太繁琐，二也容易出错，想到这里，我决定写个程序把这些数据抓取下来。

　　我原想着用python来抓取数据，都说python爬数据那是一流的，但仔细一想，python语法我不熟啊，现在现学似乎也来不及。

　　用java吗？杀鸡哪里用的着牛刀。还是用php吧，虽说好多年没用了，但照着语法手册，依葫芦画瓢，应该可以试下。

　　没有php的环境，就下载了个安装神器包xampp，这玩意帮你把php、mysql、apache甚至tomcat等都一起打包安装好了，安装好的控制台见如下图，

　　![image.png](https://images.hive.blog/DQmUpgscg2WfjWDadxjBW9EBBtoGxkFpkGzsVsrTWifdEPx/image.png)

　　测试下是否安装好环境，如下图，

　　![image.png](https://images.hive.blog/DQmYT1bPkD7b6GTyhcuzz3ZDqvpntC6VnbUxaKQLx48YHUZ/image.png)

　　嗯，环境安装正常。

　　接下来就是写个程序，把相关的数据抓过来。

　　本着不重复造轮子的原则，我在网上找到了一个插件:PHP Simple HTML DOM Parser，一款php下专门用于html解析的插件，

　　![image.png](https://images.hive.blog/DQmW2jw7GUXTiZrLWcbzLMTwFMvKr5Th9xF63zB5XnVwLCt/image.png)

　　看了下调用语法，似乎也挺简单。

　　打开网站的数据页面，查看网页源代码，发现数据都在这个table里，

　　![image.png](https://images.hive.blog/DQme9zbBm3RBM8tDUrHLXDehVLB9P7Y8vjwDjNRz1WDhr1V/image.png)

　　先写一段抓取程序，如下图，

　　![image.png](https://images.hive.blog/DQmaTTGHdTq7dLfQq4y3tuiJJmjxSnkx459BcshjHtTBTVz/image.png)

　　注意抓取的时候，除了定义table之外，也要定义table的属性：table[class="table table-bordered  table-striped"]"]'。

　　抓取完成后，就是打印抓取的数据了，打印程序很简单，用foreach把抓取的数据打印即可，

　　![image.png](https://images.hive.blog/DQmWaDwSfXsYCWj7f2fVZ7UxTn1gN8hbhkR3MHhSzD5mM8H/image.png)

　　![image.png](https://images.hive.blog/DQmXuUxfS5ju83ucvph4W3AMAmWwa6zn4kXU7e7uYQYMRXF/image.png)

　　![image.png](https://images.hive.blog/DQmaZSAF1p2wZLqS5Gt5DCimFuWXnYL5v5QL1Pehw7VB8Hr/image.png)

　　基本程序就写好了，调试无误后，测试下，如下图，

　　![image.png](https://images.hive.blog/DQmW3NR1hn5L8dtzjka6hYLgZrHjVNyZtV1indVuKbCcRhc/image.png)

　　嗯，没有问题，是想要的数据。:)
