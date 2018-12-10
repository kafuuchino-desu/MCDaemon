# MCDaemon

[English document](https://github.com/kafuuchino-desu/MCDaemon/blob/master/README.md)

------

一个用于实现插件功能的原版服务端控制脚本  
在centos7和python2环境下测试通过

## 开始使用

1.下载最新的 [release](https://github.com/kafuuchino-desu/MCDaemon/releases)  
2.解压之后在解压出的文件夹里面创建一个启动脚本： `start.sh`   
3.在启动脚本里面输入你的服务端启动参数 (建议使用 `cd server && [服务端启动命令]`之后把服务端放在server文件夹内方便管理文件)  
4.使用 `pip install -r requirements.txt`安装依赖  
5.用 `python server.py` 启动服务端  

------

## 插件API

### OnServerInfo() API  

在你的插件文件中定义一个onServerInfo(srever, info)函数(例如 `plugin.py`)  

### onServerStartup() API

在你的插件文件中定义一个onServerStartup(srever, info)函数(例如 `plugin.py`)  

### onPlayerJoin() 和 onPlayerLeave() API

在你的插件中定义一个onPlayerJoin(server, playername) 或者 onPlayerLeave(server, playername) 函数，playername变量是一个str，包含那个正在退出或加入服务器的玩家名

----------

## API 对象说明

##### server对象具有以下几种方法：

server.stop():停止服务器

server.start():启动服务器

server.send(string):发送一个字符串到服务端的STDIN，记得在字符串最后面加上`\n`让服务端执行命令，如果没有特殊情况请使用execute()

server.execute(command):执行一条命令

server.say(data):调用服务端的`/tellraw @a`命令并帮你自动填写data到json格式

server.tell(player, text):调用服务端的`/tellraw`命令并帮你转换player和text到json格式

##### info对象具有以下属性:

info.hour/info.min/info.sec:服务端输出这条log的时间

info.sourceProcess:这条信息从哪个进程发送，例如 'Server Thread/INFO'

info.isPlayer:信息是否是一个玩家的聊天内容

info.player:哪个玩家发送了这条信息

info.content:如果这条信息不是玩家发送的，里面包含的内容就是在sourceProcess后面的整段信息，如果这段信息是玩家发送的，里面包含的内容就是玩家的聊天内容，请注意里面是不包含玩家名的，例如内容是 `hi`而不是`<chino_desu> hi`

##### 插件热重载:  

使用`!!MCDReload`重新载入插件

------

## 关于

这个脚本目前由chino_desu(minecraft id:chino_desu)维护

下面是联系方式

twitter: [@chino_desu_](https://twitter.com/chino_desu_)

discord: chino_desu#8564
