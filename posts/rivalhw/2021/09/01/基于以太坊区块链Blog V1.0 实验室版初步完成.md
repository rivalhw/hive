# 基于以太坊区块链Blog V1.0 实验室版初步完成

**Author:** @rivalhw  
**Permlink:** blog-v1-0  
**Created:** 2021-09-01T13:28:57  
**Category:** hive-105017  
**Tags:** {
  "tags": [
    "web3",
    "smartcontract",
    "eth",
    "cn-reader",
    "cn"
  ],
  "image": [
    "https://images.hive.blog/DQmev9HZbYXiV7wsRdoEqKfnjNYj5tev2xQ1ysETgvBqCuo/001.png",
    "https://images.hive.blog/DQmYC2Qz33B12sMqVpn4TPTwG6pf2nRvm8jHxu8uPuv6nBB/002.png",
    "https://images.hive.blog/DQmfYcMm53qRxEPKzWZsSafPLkS7iNPzjsKtH156KDivUYT/003.png",
    "https://images.hive.blog/DQmY3q7mQKyRUP1n8gKnJhiXnnQwEprqVvZHrzmvvq1KT5f/005.png",
    "https://images.hive.blog/DQmQ9vzA2NzwYmQMjyap1zqBZfoK6QtquZjcKtAZC8z6DGZ/004.png",
    "https://images.hive.blog/DQmbkb1qTCQpzcdgaiXs7YVmdgUKHjBSQ8FUzyx8VVxSe6K/006.png"
  ],
  "app": "hiveblog/0.1",
  "format": "markdown",
  "author": "rivalhw"
}

---

这几天研究了下Web3.js，算是有了一些理解。

Web3.js是一个javascript库，可以让你执行很多与区块链进行交互的任务，比如部署和操作智能合约、以太币转账等。

针对我之前编写的博客智能合约，我使用Web3编写了对应的前端js，如新增博客文章，如下图，

![001.png](https://images.hive.blog/DQmev9HZbYXiV7wsRdoEqKfnjNYj5tev2xQ1ysETgvBqCuo/001.png)

博客修改的程序跟新增差不多，

![002.png](https://images.hive.blog/DQmYC2Qz33B12sMqVpn4TPTwG6pf2nRvm8jHxu8uPuv6nBB/002.png)

获取博文的操作，

![003.png](https://images.hive.blog/DQmfYcMm53qRxEPKzWZsSafPLkS7iNPzjsKtH156KDivUYT/003.png)

![005.png](https://images.hive.blog/DQmY3q7mQKyRUP1n8gKnJhiXnnQwEprqVvZHrzmvvq1KT5f/005.png)

构造函数初始化

![004.png](https://images.hive.blog/DQmQ9vzA2NzwYmQMjyap1zqBZfoK6QtquZjcKtAZC8z6DGZ/004.png)

开始测试下调用智能合约更新博客操作

![006.png](https://images.hive.blog/DQmbkb1qTCQpzcdgaiXs7YVmdgUKHjBSQ8FUzyx8VVxSe6K/006.png)

根据返回的hash地址，在以太坊测试网络上查看，success

结合之前编写的智能合约、中心化程序以及现在的前端js调用，基本完成了博客系统V1.0。

当然，这个Blog V1.0只是我个人用来熟悉相关技术的一个实验品，目前还有许多地方待完善，我后边会继续接着完善下。
