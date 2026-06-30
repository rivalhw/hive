# [EOS学习笔记]Hello World

**Author:** @rivalhw  
**Permlink:** eos-hello-world  
**Created:** 2019-08-09T13:59:30  
**Category:** eos  
**Tags:** {
  "tags": [
    "eos",
    "cn-reader",
    "partiko",
    "sct",
    "zzan"
  ],
  "image": [
    "https://cdn.steemitimages.com/DQmS9sHNyPYC1ARNheWRDbfR5NsoQooKCUEDbSy18kiMhHe/01%20hellocpp.png",
    "https://cdn.steemitimages.com/DQmRqNVUHZYqxB9Bbp4zCCMs7Lxzt1zbVUBYd3s9GnKTjzH/02%20cpp.png",
    "https://cdn.steemitimages.com/DQmasvZvtfdGyfhwiuoxKpaf4kvACyRBPkAGzJUKg1VzxnF/04%20cleoswalletkeys.png",
    "https://cdn.steemitimages.com/DQmShXqadkQpxfbRDbsuf1SFco3XY84gXh8xLebhW4BTKpW/05%20cleos%20create%20account%20hello.png",
    "https://cdn.steemitimages.com/DQmeyg6NDDTevwMgk8ye3H9KM7tZeuYgYKhQXx4xMnNmuBZ/06%20setcontract.png",
    "https://cdn.steemitimages.com/DQmeCPr2TWhzbptWtvs6eNPoTvkib7KyeFYeBhWfVPh1zRr/07%20hellorivalhw.png",
    "https://cdn.steemitimages.com/DQmZKYHA6vVWySL5xjMUovAEmoaQbHHsFaF4xrRHMQSXLpb/07-2%20hellorivalhw.png",
    "https://cdn.steemitimages.com/DQmY7Zc1v7GfoiBZAnBg6eWyuBnRoKSTP3KAsTJE4iE9dBE/08%20newhello.png",
    "https://cdn.steemitimages.com/DQmdfmZNVhcq65QLniCynx2ZnvZB7c77hKeEsehZkcu1Yz8/09%20recompile.png",
    "https://cdn.steemitimages.com/DQmc67TaWCF2prmDDnYVXUpykpaWJfRNhgjDRgEEpWMr31n/10%20setcontract2.png",
    "https://cdn.steemitimages.com/DQmVrHMLnZioGehbBegYvfa2vhvA8SyDzYZ8y579Ns5KVsV/11.png",
    "https://cdn.steemitimages.com/DQmTbqELQKweAQo91wJnE3Mxva1GwcEwBQ2MudEwCm8G8fB/12.png",
    "https://cdn.steemitimages.com/DQmYJ9M2Fbu5WfDEL3AcUR3H2FcSF8iSks3TSmaA2BkfiSg/03%20nodeosuccessexit.png"
  ],
  "app": "steemit/0.1",
  "format": "markdown"
}

---

创建一个新合约文件hello
touch hello.cpp

![01 hellocpp.png](https://cdn.steemitimages.com/DQmS9sHNyPYC1ARNheWRDbfR5NsoQooKCUEDbSy18kiMhHe/01%20hellocpp.png)

编译合约文件
eosio-cpp hello.cpp -o hello.wasm

![02 cpp.png](https://cdn.steemitimages.com/DQmRqNVUHZYqxB9Bbp4zCCMs7Lxzt1zbVUBYd3s9GnKTjzH/02%20cpp.png)

cleos wallet keys
![04 cleoswalletkeys.png](https://cdn.steemitimages.com/DQmasvZvtfdGyfhwiuoxKpaf4kvACyRBPkAGzJUKg1VzxnF/04%20cleoswalletkeys.png)

注意，执行这里需要确保钱包(wallet)的状态为unlock状态

创建hello账户
cleos create account eosio hello YOUR_PUBLIC_KEY  -p eosio@active

![05 cleos create account hello.png](https://cdn.steemitimages.com/DQmShXqadkQpxfbRDbsuf1SFco3XY84gXh8xLebhW4BTKpW/05%20cleos%20create%20account%20hello.png)

cleos set contract hello contracts/hello -p hello@active
![06 setcontract.png](https://cdn.steemitimages.com/DQmeyg6NDDTevwMgk8ye3H9KM7tZeuYgYKhQXx4xMnNmuBZ/06%20setcontract.png)


cleos push action hello hi '["rivalhw"]' -p bob@active
![07 hellorivalhw.png](https://cdn.steemitimages.com/DQmeCPr2TWhzbptWtvs6eNPoTvkib7KyeFYeBhWfVPh1zRr/07%20hellorivalhw.png)

cleos push action hello hi '["rivalhw"]' -p alice@active
![07-2 hellorivalhw.png](https://cdn.steemitimages.com/DQmZKYHA6vVWySL5xjMUovAEmoaQbHHsFaF4xrRHMQSXLpb/07-2%20hellorivalhw.png)

稍微修改下hello合约内容
![08 newhello.png](https://cdn.steemitimages.com/DQmY7Zc1v7GfoiBZAnBg6eWyuBnRoKSTP3KAsTJE4iE9dBE/08%20newhello.png)


重新编译合约文件
![09 recompile.png](https://cdn.steemitimages.com/DQmdfmZNVhcq65QLniCynx2ZnvZB7c77hKeEsehZkcu1Yz8/09%20recompile.png)

cleos set contract hello contracts/hello -p hello@active
![10 setcontract2.png](https://cdn.steemitimages.com/DQmc67TaWCF2prmDDnYVXUpykpaWJfRNhgjDRgEEpWMr31n/10%20setcontract2.png)

cleos push action hello hi '["bob"]' -p alice@active
![11.png](https://cdn.steemitimages.com/DQmVrHMLnZioGehbBegYvfa2vhvA8SyDzYZ8y579Ns5KVsV/11.png)

用正确的方式重新打开
cleos push action hello hi '["alice"]' -p alice@active
![12.png](https://cdn.steemitimages.com/DQmTbqELQKweAQo91wJnE3Mxva1GwcEwBQ2MudEwCm8G8fB/12.png)
果然，如你所愿 :)



我在测试的时候，总出现一些莫名其妙的问题，后来才发现是因为没有正常退出nodeos引起的，有时候replay后就可以，有时候甚至连 hard replay 也不可以，无奈之下只好delete  all blocks

pkill nodeos
![03 nodeosuccessexit.png](https://cdn.steemitimages.com/DQmYJ9M2Fbu5WfDEL3AcUR3H2FcSF8iSks3TSmaA2BkfiSg/03%20nodeosuccessexit.png)
