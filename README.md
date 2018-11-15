# MCDaemon

[中文文档](https://github.com/kafuuchino-desu/MCDaemon/blob/master/README_cn.md)

----------
A software for automatically controlling minceraft server with support for plugins
tested on Centos7 with python2

## how to use

1.download the latest [release](https://github.com/kafuuchino-desu/MCDaemon/releases)  
2.unzip it and create a shell script named as `start.sh`   
3.type your server start commands in the script (i suggest you write like this `cd server && java -xxx` so you can put your server files in the server folder to organize the files easier)
4.install the requirments using `pip install -r requirments.txt`
5.you can start the server using `python server.py` now

------

## Plugin API

this program includes a Plugin API which you can get information from server output and execute a certain command

to start using the Plugin API and write your Plugin you should follow those steps:

1.create a  .py file in the plugins folder

2.define a function named as OnServerInfo(server, info)

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

-----

## About

this repo is currently maintained by chino_desu(minecraft id:chino_desu).

you can contact me by:

twitter: [@chino_desu_](https://twitter.com/chino_desu_)

discord: chino_desu#8564
