新增对于mac的支持  
支持系统: Windows mac  
  
  

# wechat_info_collect
调查取证 | 针对微信客户端的信息收集工具, 一键提取本地PC所有的微信信息, 包括微信号, 手机号等  
暂且写个python版本的, 后续再写c或者其他语言的, 使用会更方便    
已经测试过部分系统, 但是在某些特殊情况下依然会有失败的可能, 这些情况下无法修复Bug, 如果实战遇到的话, 需要自己手动查看地址  

如果需要查看曾使用过的小程序名单, 需要输入可用的微信公众号cookie和token  
cookie可抓包查看  
token在登陆后的url中直接可见, 参数名即token  


安装环境依赖  

Windows需要pypiwin32, mac无需  

>pip3 install pypiwin32  
>pip3 install requests  


  
演示截图:  

![image](https://user-images.githubusercontent.com/19652329/167572374-7b867c2b-23bf-40f8-883d-ca35d645bbf2.png)

如果需要导出所有小程序名单, 需要可用的公众号cookie和token  
详情请见 

https://mp.weixin.qq.com/s?__biz=Mzg4NDU4OTQ1NA==&mid=2247484267&idx=1&sn=c9ce06274bc6fed834c635d29b35f883&chksm=cfb4958af8c31c9c03c536cfa081ca1bd471bfd66144a0b30241031318e02e236bece78853de&token=1855708768&lang=zh_CN#rd  


![image](https://user-images.githubusercontent.com/19652329/167623636-925c3302-7811-4031-a6d6-f055481f1110.png)  

=====================================  
2022年5月13日更新:  
增加对于mac的支持, 暂不支持导出小程序名单  


=====================================  

2022年5月10日更新:
支持查看所有微信曾使用过的所有小程序名单  
![image](https://user-images.githubusercontent.com/19652329/167609080-fe2bb5fe-9dd7-4556-a54b-e5087f1b0516.png)


=====================================  

2022年5月9日更新:  

增加自动化寻找地址失败后手动输入存储地址功能  

=====================================  
