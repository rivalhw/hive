# 适合的才是最好的：几款不同AI向量数据库对比感受

**Author:** @rivalhw  
**Permlink:** 2fdqij-ai  
**Created:** 2023-07-12T05:02:00  
**Category:** hive-105017  
**Tags:** {
  "tags": [
    "ai",
    "opensource",
    "embedding",
    "database",
    "cn"
  ],
  "image": [
    "https://images.hive.blog/DQmNmQ1kevjZYFbka4vWt57c2Z2oZDQSm5gv9bH1Cgr7fTF/binary-gb4b764622_1280.jpg",
    "https://images.hive.blog/DQmXwnYo3mQydJwdrFrCfmoQ5uiNsqJuHYSR6etfPCTRaS4/image.png",
    "https://images.hive.blog/DQmYQyn1tjTfnrFbTXP3mssKZzqfiQo27BAYcz2ekJBhAY5/Qdrant.png",
    "https://images.hive.blog/DQmba1gn22Wx7nLvJ4aZ6epSZXHgvZpXwN5XMYtn6Nh3bwk/Chroma.png",
    "https://images.hive.blog/DQmSfrdSaD2U78iJS4c5aYGrSYZF2pxz5DHp2Raqp11AdF7/Milvus.png",
    "https://images.hive.blog/DQmcaqVYaz78QDn3TsqpX3wJLnxKKAt54pdFvLRknHMbNyJ/image.png",
    "https://images.hive.blog/DQmXYYScLMaccG12VrtwJYTUxak7pgHZtbsyi5u818Je1VC/image.png",
    "https://images.hive.blog/DQmXscn4wit5AGS1SbDfFZaCTe5Cn9Qs7LHWZAcu2B5VBVN/image.png",
    "https://images.hive.blog/DQmQDAZ3op7mMounpTmTwBELiDoR2EieEriuDpjBTjiVS4F/image.png",
    "https://images.hive.blog/DQmTSNQrXmiRnn84a4R9Rrs44njLKCmiNeUmR38jqob4Bky/image.png",
    "https://images.hive.blog/DQmPtqqYNKMkVwahshXQb1g5XX9WRwtRe4weH7QxKpKKwZu/image.png",
    "https://images.hive.blog/DQmfSyaQW7q5LExfPjeuZDE3KbCzh62VmHf77KmapQN9VkN/image.png",
    "https://images.hive.blog/DQmUFJ9fUpFvSeKsAjqivLPqK9abhwhkEj2eob4dtZGgZJm/image.png",
    "https://images.hive.blog/DQmStVdeYyaZZuXRfr7RJ8KRC72SWar6hcr5NfwLjDYHiy1/image.png",
    "https://images.hive.blog/DQmPTzTA2AhhnuYcPTTYUyscVJfFdmyFyT3eaXBoU6fgbC5/image.png",
    "https://images.hive.blog/DQmW4TMwLonp3nDZn76gq4t6XkTwQQrnzC6NzZwjxqNQvsd/image.png"
  ],
  "links": [
    "https://pixabay.com/users/geralt-9301/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2728117"
  ],
  "app": "hiveblog/0.1",
  "format": "markdown"
}

---

最近在学习跟AI相关，说到AI，自然避免不了要使用到向量数据库，今天我就拿市面上几款向量数据库做下对比，也来谈下自己粗浅的感受吧。

　　Google上对向量数据库的解释如下，

>向量数据库是一种专门用于存储和查询向量数据的数据库系统，与传统数据库相比，向量数据库使用向量化计算，能够高速地处理大规模的复杂数据；并可以处理高维数据，例如图像、音频和视频等，解决传统关系型数据库中的痛点；同时，向量数据库支持复杂的查询操作，也可以轻松地扩展到多个节点，以处理更大规模的数据。

　　其实我们普通人简单理解：向量数据库是专为AI量身打造，比传统数据库更擅长图像、音频、视频数据处理。

　　四款向量数据库，分别为：**Pinecone**、**Qdrant**、**Chroma**、和**Milvus**。其中除了**Pinecone**，其它三款均为开源。其中前三款是国外的，最后一款**Milvus**是国产的，我查询了下，是上海一家企业开发的。赞！

　　![image.png](https://images.hive.blog/DQmXwnYo3mQydJwdrFrCfmoQ5uiNsqJuHYSR6etfPCTRaS4/image.png)

　　Pinecone官方网页

　　今天我们主要对比这三款开源的。

　　首先从社区活跃度和人气度来看，

　　![Qdrant.png](https://images.hive.blog/DQmYQyn1tjTfnrFbTXP3mssKZzqfiQo27BAYcz2ekJBhAY5/Qdrant.png)

　　Qdrant在github上目前有11.6K star，最近一次更新是3星期前。

　　![Chroma.png](https://images.hive.blog/DQmba1gn22Wx7nLvJ4aZ6epSZXHgvZpXwN5XMYtn6Nh3bwk/Chroma.png)

　　Chroma在github上目前有7K star，最近一次更新是一星期前。

　　![Milvus.png](https://images.hive.blog/DQmSfrdSaD2U78iJS4c5aYGrSYZF2pxz5DHp2Raqp11AdF7/Milvus.png)

　　Milvus在github上目前有21.1K star，最近一次更新是一星期前。

　　从人气和社区活跃度上看，这款国产的**Milvus**向量数据库，毫无疑问地绝对的第一。

　　我们再来从用户使用体验上看下。

　　![image.png](https://images.hive.blog/DQmcaqVYaz78QDn3TsqpX3wJLnxKKAt54pdFvLRknHMbNyJ/image.png)

　　**Qdrant**官网

　　![image.png](https://images.hive.blog/DQmXYYScLMaccG12VrtwJYTUxak7pgHZtbsyi5u818Je1VC/image.png)

　　Qdrant提供了四种安装方法，分别是：Docker、From source、Python client和Kubernetes，最后这个Kubernetes其实我不也不清楚是什么。

　　使用也很简单，

　　![image.png](https://images.hive.blog/DQmXscn4wit5AGS1SbDfFZaCTe5Cn9Qs7LHWZAcu2B5VBVN/image.png)

　　Chroma支持两种安装方式，分别是python和javascript，

　　我采用的是python安装。

　　![image.png](https://images.hive.blog/DQmQDAZ3op7mMounpTmTwBELiDoR2EieEriuDpjBTjiVS4F/image.png)

　　不知道怎么回事，我开始先在windows下安装，总是出现兼容包问题。而更换到Ubuntu下安装，很容易就安装成功。

　　![image.png](https://images.hive.blog/DQmTSNQrXmiRnn84a4R9Rrs44njLKCmiNeUmR38jqob4Bky/image.png)

　　Chroma的使用也很简单，如上图，几句简单的调用直接便可以使用。

　　Chroma部署在AWS上也很简单，按照其最低要求至少2G内存，AWS上大概是15刀每月。

　　![image.png](https://images.hive.blog/DQmPtqqYNKMkVwahshXQb1g5XX9WRwtRe4weH7QxKpKKwZu/image.png)

　　看下**Milvus**

　　![image.png](https://images.hive.blog/DQmfSyaQW7q5LExfPjeuZDE3KbCzh62VmHf77KmapQN9VkN/image.png)

　　**Milvus**支持Docker安装，方法也很简单，如下图操作，

　　![image.png](https://images.hive.blog/DQmUFJ9fUpFvSeKsAjqivLPqK9abhwhkEj2eob4dtZGgZJm/image.png)

　　**Milvus**提供AWS Cloud和Google Cloud接入，类似阿里云数据库那种，只需要修改uri和token key即可。

　　提供三种版本供用户选择，分别为免费版、标准版和企业版。

　　![image.png](https://images.hive.blog/DQmStVdeYyaZZuXRfr7RJ8KRC72SWar6hcr5NfwLjDYHiy1/image.png)

　　其中免费版貌似只支持一个Cluster，标准版65刀每月，企业版99刀每月，新用户提供100刀一个月的免费券。

　　![image.png](https://images.hive.blog/DQmPTzTA2AhhnuYcPTTYUyscVJfFdmyFyT3eaXBoU6fgbC5/image.png)

　　支持REST ful API、Python、NodeJS、JAVA。

　　除此之外，**Milvus**还提供类似web UI Query界面，可以很方便地直接在上边操作查询，有点像我们使用传统数据库查询工具那种。

　　我尝试用java在本地测试了下，感受不错。

　　![image.png](https://images.hive.blog/DQmW4TMwLonp3nDZn76gq4t6XkTwQQrnzC6NzZwjxqNQvsd/image.png)

　　总体讲，**Milvus**提供的支持和服务更为全面，**Chroma**和**Qdrant**的文档和技术支持差不多，**Chroma**更为轻量级，便于很快部署，对配置要求也不是很高，有点想sql lite那种，很容易上手，非常适合新手或创业者。

　　**Milvus**唯一的缺点，就是价格方面不太亲民，即便是标准版也需要65刀美金，而这个价格，已经可以够**Chroma**在AWS上购买四个多月的服务支持了。

　　![binary-gb4b764622_1280.jpg](https://images.hive.blog/DQmNmQ1kevjZYFbka4vWt57c2Z2oZDQSm5gv9bH1Cgr7fTF/binary-gb4b764622_1280.jpg)
Image by <a href="https://pixabay.com/users/geralt-9301/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2728117">Gerd Altmann</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2728117">Pixabay</a>
