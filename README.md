

# wechat_info_collect  

致谢(这些师傅在脚本编写以及bug方面给予了宝贵的支持):  
  CHLnG, 山山而川  
  

公众号: 饿猫的小黑屋  
调查取证 | 针对微信客户端的信息收集工具, 一键提取本地PC所有的微信信息, 包括微信号, 手机号  
支持系统: Windows mac 
  
  
新增对于mac的支持  
没用过mac, 所以虽然写之前有构想支持mac, 但是开始写的时候还是忘了  
看到issues有人问多久支持mac, 受宠若惊, 感谢大家的喜欢 
于是当天下午就支持了mac, 但是因为开始写的时候忘记了这个事情, 所以导致加进去代码之后, 整个代码有些许混乱  
为了方便使用, 也没有分成多个文件, 都写在一个文件里, 使用会方便很多  
  
支持导出所有微信曾使用过的所有小程序名单:   
    如果需要查看曾使用过的小程序名单, 需要输入可用的微信公众号cookie和token  
    cookie以appmsglist开头  
    token在登陆后的url中直接可见, 参数名为token  
  
  
安装环境依赖  
Windows需要pypiwin32, mac只需安装requests即可  

>pip3 install pypiwin32  
>pip3 install requests  
  
演示截图:  

![image](https://user-images.githubusercontent.com/19652329/167572374-7b867c2b-23bf-40f8-883d-ca35d645bbf2.png)  
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
