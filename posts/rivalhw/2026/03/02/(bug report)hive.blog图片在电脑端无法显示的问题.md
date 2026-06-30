# (bug report)hive.blog图片在电脑端无法显示的问题 

**Author:** @rivalhw  
**Permlink:** hiveblog  
**Created:** 2026-03-02T05:07:03  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "format": "markdown",
  "image": [
    "https://files.peakd.com/file/peakd-hive/rivalhw/23t8D1dSfgrKdDn9jV1cQkYLCX2pc9XA4QpoeHPF1jehAC8cGiLip1gvpqa4N7fXLrCsy.png",
    "https://files.peakd.com/file/peakd-hive/rivalhw/23t8DBnQF5o9BCRPVJhEwMgjfuhuUyjHpsVwZwsTfjooCKjJm5kvk48viE4yQqTvg6znf.png",
    "https://files.peakd.com/file/peakd-hive/rivalhw/23tmf5G3S1LBsgoTA5ebYcqSvRtsm8ofuQQPFKznwKXa8aChuHfK4vRXc9zDrpqZd13nh.png",
    "https://files.peakd.com/file/peakd-hive/rivalhw/23y9Cim61y29V9GERwkM4m3dJsDny2uWp3Nqkf6e63xMzTmJGGrCcjWWAVVWgVm3zjU6Q.jpg",
    "https://files.peakd.com/file/peakd-hive/rivalhw/23w38LabbVhBq6jXZ4Bey76EUTb3YZJgw2xkqfQNSdLuQAh8XpU4RD6n4VYNj7GSyYBqq.png",
    "https://files.peakd.com/file/peakd-hive/rivalhw/Eo8ZYbEvfXRPepCZ2HNbjURh2QKj2q82A7ha6KPjdijxXSoBdNy2CtnhVhxD5xMcYDB.png",
    "https://files.peakd.com/file/peakd-hive/rivalhw/23tSzWXZGXFVRxyfthyAtpUsZ7uBPtyUvFtma8suMvrnMbQFnyaoa9CqvUsrkKM4MdTu1.png",
    "https://files.peakd.com/file/peakd-hive/rivalhw/23twAVeHooqKHfeWe7dZdX1DQ2bVDJNUC83ez2MSTzECSBUBV1Banzu1K9GcvqLEkXKtH.png"
  ],
  "links": [
    "https://images.hive.blog/768x0/"
  ],
  "tags": [
    "hiveblog",
    "bug",
    "report",
    "cn-reader",
    "cn"
  ],
  "users": []
}

---

这几天在用hive.blog的图片上传时，总是会提示出错:

>UPLOAD FAILED!


![000.png](https://files.peakd.com/file/peakd-hive/rivalhw/23t8DBnQF5o9BCRPVJhEwMgjfuhuUyjHpsVwZwsTfjooCKjJm5kvk48viE4yQqTvg6znf.png)

我开始以为是短暂性故障，结果发现连续几天一直都不可以。

无奈只好改用其它图片上传插件，比如peakd.com，这样才可以。

我一直习惯了在hive.blog下编辑，还是会把上传后的内容，包括图片等复制到hive.blog下，一切似乎都没什么问题。

但是，文章发布出去后，发现列表时预览，图片看不到，如下图，


![001.png](https://files.peakd.com/file/peakd-hive/rivalhw/23tmf5G3S1LBsgoTA5ebYcqSvRtsm8ofuQQPFKznwKXa8aChuHfK4vRXc9zDrpqZd13nh.png)

这很奇怪，难道是图片没上传好？

我重新打开文章，再次编辑，发现没什么问题啊。

重新回到列表查看时，发现问题依旧，图片仍然无法查看。

但是，手机端浏览时，反而很正常，图片能显示，


![02.jpg](https://files.peakd.com/file/peakd-hive/rivalhw/23y9Cim61y29V9GERwkM4m3dJsDny2uWp3Nqkf6e63xMzTmJGGrCcjWWAVVWgVm3zjU6Q.jpg)


这是怎么回事呢？

还是看下html源码吧。

用chrome dev 打开网页，


![03.png](https://files.peakd.com/file/peakd-hive/rivalhw/23w38LabbVhBq6jXZ4Bey76EUTb3YZJgw2xkqfQNSdLuQAh8XpU4RD6n4VYNj7GSyYBqq.png)

定位到图片位置，发现一个问题，原先图片的地址前，多了个：
>https://images.hive.blog/768x0/ 

比如图片通过peakd.com上传后为：

>https://files.peakd.com/file/peakd-hive/rivalhw/244KLkSUiptLUCSD3jCntkxawqSjpz2XXL1anohziCKCLjvbpoftPWPkgN7WETYweKNMP.jpg

但保存后自动变成了，

>https://images.hive.blog/1536x0/https://files.peakd.com/file/peakd-hive/rivalhw/244KLkSUiptLUCSD3jCntkxawqSjpz2XXL1anohziCKCLjvbpoftPWPkgN7WETYweKNMP.jpg

这应该就是导致图片无法展示的原因了。

想起O哥之前提醒，万事不决问AI呀。

问了下AI，给出的如下：


![1-1.png](https://files.peakd.com/file/peakd-hive/rivalhw/Eo8ZYbEvfXRPepCZ2HNbjURh2QKj2q82A7ha6KPjdijxXSoBdNy2CtnhVhxD5xMcYDB.png)


![1-2.png](https://files.peakd.com/file/peakd-hive/rivalhw/23tSzWXZGXFVRxyfthyAtpUsZ7uBPtyUvFtma8suMvrnMbQFnyaoa9CqvUsrkKM4MdTu1.png)


![1-4.png](https://files.peakd.com/file/peakd-hive/rivalhw/23twAVeHooqKHfeWe7dZdX1DQ2bVDJNUC83ez2MSTzECSBUBV1Banzu1K9GcvqLEkXKtH.png)


大意是说，这是平台的一种图片优化方式，目的是为了，

>统一缓存
统一压缩
统一尺寸

我们只要使用hive.blog就没法避开这个，毕竟这个是hive.blog系统自动添加的。

但是，这个功能在电脑端是有问题的，而移动端正常，结果就出现了前边开头一幕，电脑列表端无法显示图片，如下图，


![005.png](https://files.peakd.com/file/peakd-hive/rivalhw/23t8D1dSfgrKdDn9jV1cQkYLCX2pc9XA4QpoeHPF1jehAC8cGiLip1gvpqa4N7fXLrCsy.png)

我在hive.blog下看了下，都是类似的问题。

希望hive.blog能早些解决这个bug问题。
