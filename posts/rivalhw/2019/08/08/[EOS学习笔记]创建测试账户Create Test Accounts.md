# [EOS学习笔记]创建测试账户Create Test Accounts

**Author:** @rivalhw  
**Permlink:** eoscreate-test-accounts-1565231323  
**Created:** 2019-08-08T14:28:51  
**Category:** eos  
**Tags:** {
  "tags": [
    "eos",
    "cn-reader",
    "partiko",
    "sct",
    "zzan"
  ],
  "links": [
    "http://127.0.0.1:8888/;"
  ],
  "app": "steemit/0.1",
  "format": "markdown",
  "image": [
    "https://cdn.steemitimages.com/DQmeDyQ1nDBxxfLzj3X85sLW8S82uC3VfuvLk3DtqbrcPBS/0%20notrunning.png",
    "https://cdn.steemitimages.com/DQmVChVzZC6tS5bN6FQhZ75fDKENEQJrHtwhYv47pGS8qeX/5.png",
    "https://cdn.steemitimages.com/DQmaCxAkW7ZiCPKorgPYbiniKqxUuCGF9LsqPbb5UScYS5z/1%20cleos%20create%20account%20eosio%20bob.png",
    "https://cdn.steemitimages.com/DQmWY6LpTRUDJjw1qpZy7LwtvobF6YJQyS7KLxRjFxCENqG/2%20cleos%20create%20account%20eosio%20alice.png",
    "https://cdn.steemitimages.com/DQmYDLqDJcTyNsWDWpB15bEpkqSePE9vWnAdapj6NG7MUTE/4.png"
  ]
}

---

Step 1: Create Test Accounts 创建测试账户
cleos create account eosio bob yourpublic_key

出现如下提示错误：
Failed to connect to nodeos at http://127.0.0.1:8888/; is nodeos running?

![0 notrunning.png](https://cdn.steemitimages.com/DQmeDyQ1nDBxxfLzj3X85sLW8S82uC3VfuvLk3DtqbrcPBS/0%20notrunning.png)

原来是没有启动节点，

![5.png](https://cdn.steemitimages.com/DQmVChVzZC6tS5bN6FQhZ75fDKENEQJrHtwhYv47pGS8qeX/5.png)
重新启动后再次尝试，


![1 cleos create account eosio bob.png](https://cdn.steemitimages.com/DQmaCxAkW7ZiCPKorgPYbiniKqxUuCGF9LsqPbb5UScYS5z/1%20cleos%20create%20account%20eosio%20bob.png)

成功创建bob账户

再次试下创建另一账户 alice
![2 cleos create account eosio alice.png](https://cdn.steemitimages.com/DQmWY6LpTRUDJjw1qpZy7LwtvobF6YJQyS7KLxRjFxCENqG/2%20cleos%20create%20account%20eosio%20alice.png)

尝试创建个mytestaccound 账户，结果出现如下提示，
Error 3010001: Invalid name
Name should be less than 13 characters and only contains the following symbol .12345abcdefghijklmnopqrstuvwxyz
Error Details:

![4.png](https://cdn.steemitimages.com/DQmYDLqDJcTyNsWDWpB15bEpkqSePE9vWnAdapj6NG7MUTE/4.png)
原来账户名称不能超过13个字符，且比如为：.12345abcdefghijklmnopqrstuvwxyz 其中范围。

Step 2: Public Key 

cleos get account alice
