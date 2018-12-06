# MCDaemon

[中文文档](https://github.com/kafuuchino-desu/MCDaemon/blob/master/README_cn.md)

----------
A software for automatically controlling minceraft server with support for plugins  
tested on Centos7 with python2

## how to use

1.download the latest [release](https://github.com/kafuuchino-desu/MCDaemon/releases)  
2.unzip it and create a shell script named as `start.sh`   
3.type your server start commands in the script (i suggest you write like this `cd server && java -xxx` so you can put your server files in the server folder to organize the files easier)
4.install the requirments using `pip install -r requirements.txt`
5.you can start the server using `python server.py` now

------

## Plugin API

### OnServerInfo() API  

(non blocking)define a function named as onServerInfo(server, info) in your plugin file(for example `plugin.py`)  

### onServerStartup() API

(non blocking)define a define a function named as onServerStartup(server) in your plugin file(for example `plugin.py`)  

### onPlayerJoin() and onPlayerLeave() API

(non blocking)define a function named as onPlayerJoin(server, playername) or onPlayerLeave(server, playername),the playername variable is a string containing the name of which player is joining/leaving server

----------

## API objects

##### the server object contains those attributes:

server.stop():stops the server

server.start():starts the server

server.send(string):send a string to server's STDIN,remember to add a '\n' to execute the command,use execute() if not necessary

server.execute(command):execute a command

server.say(data):a simple wrapper for the `/tellraw @a` command

server.tell(player, text):a simple wrapper for the `/tellraw` command

##### the info object contains those attributes:

info.hour/info.min/info.sec:time of this line of log

info.sourceProcess:which process sent this message ,such as 'Server Thread/INFO'

info.isPlayer:if the message is sent by a player

info.player:which player sent this message

info.content:if the message is not sent by a player it will contain the message printed after the sourceProcess, if the message is sent by a player it will ONLY conain the message player sent such as `hi`

but not `<chino_desu> hi`

##### reloading plugins:

use`!!MCDReload` to reload the plugins

-----

## About

this repo is currently maintained by chino_desu(minecraft id:chino_desu).

you can contact me by:

twitter: [@chino_desu_](https://twitter.com/chino_desu_)

discord: chino_desu#8564
