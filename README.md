

# 电子取证 | wechat_info_collect  

  

微信更新了, 在3.7.0.30之后的版本都不能通过这种方式读取信息了  
有需要的话可以自行通过Hook去抓取信息, 写成脚本也许  
本项目暂时不更新  


以下是原项目:  

调查取证 | 针对微信客户端的信息收集工具, 一键提取本地PC所有的微信信息, 包括微信号, 手机号等  
公众号: 饿猫的小黑屋 | 薛定的饿猫  
欢迎师傅们提issues或者加我微信提出bug和改进建议     
暂不会更新导出聊天记录的功能, 随着微信版本迭代, 这个功能需要频繁更新, 不过已经有团队内部开发在使用, 这个项目较长时间内不会支持这个功能  

__新增EXE版本__:  
直接运行即可, 需要导出的话可使用 wechat_info_collect_win.exe > result.txt的方式  
还有一部分bug没有修, 建议遇到了就用python版本, 短时间内不会修复这些bug  
后面可能会考虑出聊天记录相关  
去掉了大部分信息, 仅保留关键部分:  
&emsp;&emsp;1. wxid(新老形式id均支持)  
&emsp;&emsp;2. 微信号  
&emsp;&emsp;3. 手机号(国内外手机号均支持)  
&emsp;&emsp;4. 绑定邮箱(参考性存疑, 有不真实的情况)   
解决Windows环境下无python或者py文件打包为exe过大的问题  
采用golang编写, 暂不放源码, 后面会跟着另外一个大项目一起开源  
这个功能会作为上述项目的杂项子模块功能  
  
------------- __以下是原python项目__ -------------  
__支持系统__: Windows mac  
__支持提取信息__:  
&emsp;&emsp;1. wxid(新老形式id均支持)  
&emsp;&emsp;2. 微信号  
&emsp;&emsp;3. 手机号(国内外手机号均支持)  
&emsp;&emsp;4. 绑定邮箱(参考性存疑, 有不真实的情况)  
&emsp;&emsp;5. 所在城市(微信所设置城市)  
&emsp;&emsp;6. 历史头像(好像也不完全是, 有时候会有些好友的头像出现, 暂时不知道为什么)  
&emsp;&emsp;7. 历史使用过的小程序(需要联网)  
&emsp;&emsp;8. 一些其它信息(比如个性签名和一些不知道是什么的md5)  
  
__使用流程__:  
&emsp;&emsp;1. 直接运行脚本  
&emsp;&emsp;2. Windows系统下会询问是否导出历史使用小程序名单(mac暂不支持该功能)  
&emsp;&emsp;3. 如果要导出小程序使用名单, 需要输入可用的微信公众号cookie和token, token在登陆后的url中可见, cookie可f12查看, 以appmsglist开头  
&emsp;&emsp;4. Windows下如果脚本自动搜寻微信文件存储地址失败, 会提示手动输入地址, 以[WeChat files]结尾  
  
__结果导出__:  
  &emsp;&emsp;本来也没多少数据, 就不加导出功能了, 有需要的话可以使用重定向来写入文本  
  >python .\WeChat_info_collect_v3.3.py > result.txt  
  >no # 这里是选择是否需要导出小程序使用名单, 但是用上面的命令来重定向写的话, 不会有提示  
  >如果需要导出的话, 按照yes - cookie - token 的顺序填写即可  
  ![image](https://user-images.githubusercontent.com/19652329/168786080-319e88aa-b240-4f86-9de9-42a8d67a4e78.png)  


__下个版本预增加程序__:  
&emsp;&emsp;1. 一键打包机器所有用户信息文件以供下载  
&emsp;&emsp;2. 增加参数-r, 对文件夹中所有信息文件进行信息提取  
&emsp;&emsp;* .以上在于针对不便在取证机器上运行脚本时使用, 可一键打包所有信息文件, 然后在本地使用-r提取所有信息  
&emsp;&emsp;* .计划使用c编写, 以免目标机器无python环境  

* 因为我没有mac, 所以在写的时候遗忘了mac的计划, 导致在看到issues有mac需求而更新了对于mac的支持后, 整个脚本看上去有些混乱  
* 欢迎师傅们在issues提出更多需求, bug, 改进建议等  

__安装环境依赖__  
Windows需要pypiwin32, mac只需安装requests即可  

>pip3 install pypiwin32  
>pip3 install requests  
  
__演示截图__:  

![image](https://user-images.githubusercontent.com/19652329/167609080-fe2bb5fe-9dd7-4556-a54b-e5087f1b0516.png)  
  
*导出小程序名单使用样例*
![image](https://user-images.githubusercontent.com/19652329/167623636-925c3302-7811-4031-a6d6-f055481f1110.png)  
  
详情可见  
https://mp.weixin.qq.com/s?__biz=Mzg4NDU4OTQ1NA==&mid=2247484267&idx=1&sn=c9ce06274bc6fed834c635d29b35f883&chksm=cfb4958af8c31c9c03c536cfa081ca1bd471bfd66144a0b30241031318e02e236bece78853de&token=1855708768&lang=zh_CN#rd 
