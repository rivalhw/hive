# 我是如何用AI完成一款儿童游戏？

**Author:** @rivalhw  
**Permlink:** 7yk6j6-ai  
**Created:** 2024-08-30T02:43:57  
**Category:** hive-105017  
**Tags:** {
  "app": "hiveblog/0.1",
  "format": "markdown",
  "image": [
    "https://images.hive.blog/DQmbYTgJ9Ywuvy2jeeTTCQGnoaNuX8dTN6fGxqBFzJ8BDy8/player_fighter.png",
    "https://images.hive.blog/DQmYdoo89enujmoS3NvBeA9F6yHj58Axj9yDKLygzc4riMn/enemy_fighter.png",
    "https://images.hive.blog/DQmSbneBu8VGTzrDoBjCtKGhqPTzEeDrMaNZzeAKKvC4BVV/Airplane-Shooting-Game01.jpg",
    "https://images.hive.blog/DQmbENkJDkkC5paEHHzPui544BBrT5tyDkkXzswYDmaG8HT/Airplane-Shooting-Game02.jpg",
    "https://images.hive.blog/DQmQLoJJ6zKjD3vkkSG7WeoLkE1BL29Lws6XF2vuowWnCBq/Airplane-Shooting-Game03.jpg",
    "https://img.youtube.com/vi/EKQQRD_cxCY/0.jpg",
    "https://img.youtube.com/vi/ToepFFwz7S8/0.jpg",
    "https://img.youtube.com/vi/69yyOQCmW18/0.jpg"
  ],
  "links": [
    "https://www.youtube.com/embed/EKQQRD_cxCY?si=GKY32lAaNHUZ2cnE"
  ],
  "tags": [
    "game",
    "life",
    "cn-reader",
    "cn"
  ]
}

---

话说前几日的时候，我用AI做了一款小游戏，本意是用来演示现在的AI编程发展速度之快，以及AI编辑器已经非常非常方便实用，即便是不懂编程的小白，都可以轻松上手。

有句话讲，有心栽花花不开，无心插柳柳成荫。我把那期做成了短视频，发布到视频号，视频没有引起太大反响，反而是晚上回家的时候，我把白天做的那款游戏，拿出来给孩子们玩了下，反倒吸引了他们。

玩了一会，两个小家伙就开始给我提了些意见，比如如果这个移动的方格能换成真正的战斗飞机那就更逼真了。

于是，我便在网上找下战斗机的图像。我开始的想法是，想让AI帮我画一个战斗机，类似卡通一些效果，这样更容易引起小朋友们的兴趣。

结果，尝试了好一会，生成的图像效果总是不尽人意。我要求的战斗机图像，是那种平面上，不需要背景那种。

折腾了一会后，我想着这战斗机图像也不是什么稀缺的，网上应该能找到类似的吧？

于是我又花了一些时间，终于在网上找到了我心目中的战斗机，如下图，


![player_fighter.png](https://images.hive.blog/DQmbYTgJ9Ywuvy2jeeTTCQGnoaNuX8dTN6fGxqBFzJ8BDy8/player_fighter.png)
这个是我方的战斗机


![enemy_fighter.png](https://images.hive.blog/DQmYdoo89enujmoS3NvBeA9F6yHj58Axj9yDKLygzc4riMn/enemy_fighter.png)
敌方的战斗机


于是，我让AI帮我修改了下代码，将原先的方块格子，更改成增加了战斗机图像，这样看起来逼真多了。

新增的战斗机很逼真，孩子们显然很开心，但很快他们又提出了新的要求，就是说发射的子弹过于小，显得不够威力，另外子弹有点漂移，希望打出去的子弹显得更快些。

我按照他们的要求，让AI重新修改了下。

这次他们又提出了新的需求，说只有自己发射子弹，敌机没有子弹，太简单，时间久了感觉有点无趣，如果敌机也能发射子弹，增加了游戏难度，玩起来就更刺激了。

我按照他们的要求，让AI给敌机也增加了发射子弹，为了更逼真，我还做了两个改动，一是敌机的子弹改为绿色，跟我方的子弹红色区分开；另外就是敌机发射子弹为随机，这样看起来就更逼真。

为了游戏更有趣味，我还增加了计分，每击落一架敌机，就累计增加10分，直到游戏结束。


![Airplane-Shooting-Game01.jpg](https://images.hive.blog/DQmSbneBu8VGTzrDoBjCtKGhqPTzEeDrMaNZzeAKKvC4BVV/Airplane-Shooting-Game01.jpg)


![Airplane-Shooting-Game02.jpg](https://images.hive.blog/DQmbENkJDkkC5paEHHzPui544BBrT5tyDkkXzswYDmaG8HT/Airplane-Shooting-Game02.jpg)


这次改动之后，孩子们玩的就非常带劲了。

最后，为了防止他们过度沉溺游戏，我增加了倒计时，倒计时结束时，游戏就自动结束。

对了，我还将他们每次游戏的记录保存起来，每次游戏结束后，会出现个排行榜，由高往低将分数展现出来。


![Airplane-Shooting-Game03.jpg](https://images.hive.blog/DQmQLoJJ6zKjD3vkkSG7WeoLkE1BL29Lws6XF2vuowWnCBq/Airplane-Shooting-Game03.jpg)


<iframe width="560" height="315" src="https://www.youtube.com/embed/EKQQRD_cxCY?si=GKY32lAaNHUZ2cnE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
飞机大战 AirplaneShootingGame V 1.0

<iframe width="560" height="315" src="https://www.youtube.com/embed/ToepFFwz7S8?si=tlSskU4Q0SdTl4kZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
飞机大战 AirplaneShootingGame V 2.0

>A fun airplane shooting game designed for children, featuring both friendly and enemy fighter jets. The player controls the movement of their jet left and right using the cursor, and missiles are fired with the spacebar. The game ends if the player is hit by enemy fire or collides with an enemy jet.

>一款适合儿童娱乐的打飞机游戏，分为我方和敌方战机，控制光标左右移动战机，空格键发射导弹，被敌方击中或被撞则游戏结束。


后边有时间，我准备再给游戏增加上音效，比如子弹发出的声音，以及打中敌机后的声音效果。

哦，那个游戏背景，我一直还没找到合适的背景图片。


<iframe width="560" height="315" src="https://www.youtube.com/embed/69yyOQCmW18?si=DencLn6vmHJT70zC" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
飞机大战 AirplaneShootingGame V3.1
