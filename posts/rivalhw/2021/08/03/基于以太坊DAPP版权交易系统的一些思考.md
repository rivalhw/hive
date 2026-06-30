# 基于以太坊DAPP版权交易系统的一些思考

**Author:** @rivalhw  
**Permlink:** dapp  
**Created:** 2021-08-03T00:06:18  
**Category:** hive-105017  
**Tags:** {
  "tags": [
    "eth",
    "cn-reader",
    "cn"
  ],
  "image": [
    "https://images.hive.blog/DQmUHUzavwChegNoeKLQjji28DetU9oAS1m5yGQehvK2DZp/ethereum-3818347_1920.jpg"
  ],
  "links": [
    "https://pixabay.com/users/vjkombajn-764634/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=3818347"
  ],
  "app": "hiveblog/0.1",
  "format": "markdown",
  "author": "rivalhw",
  "users": [
    "lemooljiang"
  ]
}

---

昨天看了下基于以太坊DAPP的版权交易系统，有所启发。

整体的设计框架由三大部分构成，分别为前端(front end)、后端(back end)和以太坊智能合约(eth)三部分。

前端部分主要由用户注册、登陆登陆和交易部分，前端其实主要用户展示。

后台用户前端数据的交互和提交，数据库可是使用市面上任意流行数据库，比如mysql等，当用户提交注册账户时，首先提交到以太坊，生成账户和密码信息后，再将账户信息存储在本地数据库中，用户下次用户的登陆交互。当然，这里用户注册设置的密码，同以太坊生成的密码要单独分开，简单可以理解为，如果用户只是登陆，只用访问本地数据库验证即可；如果用户需要交易，每次在交易之前需要输入以太坊密钥授权，当然，因为本地 不做以太坊的密钥保存，所以每次交易都需要提供密钥。

后端以太坊交互这里，设计了两种token，一种是基于ERC20的token，另一种是基于ERC721的token ，也就是双层token。

整个系统的角色分为5种，分别是拍照者(原创作者)、用户、购买者、社区治理者和投资人。

主要实现以下激励，包括，

>激励社区共同挑选出优质的照片；
>对于贡献优质照片的摄影师进行奖励；
>促进更加活跃的版权买卖；
>降低维权成本，促进维权；
>合理分配版权收益和维权收益；

但这个系统设计我认为目前存在以下几点问题，

1、发行token在国内不合法；

2、版权资产在国内法律下属于不可分割；

3、eth现有的交易成本太高；

这套系统整体绝大部分都是围绕token进行的激励机制，如果缺乏了这1条，整个系统的机制几乎就崩塌。而第1点发行token这条路，在国内属于完全走不通，所以这里基本是一条死路。

第2点，国内之前好像有个案例官司，最后的结果是，像版权这种虚拟资产，在国内是不允许分割的，所以如果要进行分割，只能走国外道路。

第3点，以太坊的交易成本过高，尤其是牛市的时候，不但成本过高，一般人普遍难以接受，另外就是交易的时间有时候也会影响。

对于这点，蒋兄(@lemooljiang)建议使用polygone，这个也是基于以太坊的layer2扩容解决方案，既可以解决以太坊上成本过高问题，又不用担心时间，最重要的是，polygone几乎跟以太坊相同，移植成本也非常低。


![ethereum-3818347_1920.jpg](https://images.hive.blog/DQmUHUzavwChegNoeKLQjji28DetU9oAS1m5yGQehvK2DZp/ethereum-3818347_1920.jpg)

Image by <a href="https://pixabay.com/users/vjkombajn-764634/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3818347">Miloslav Hamřík</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3818347">Pixabay</a>
