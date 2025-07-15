从……起ghcr.io/kivy/buildozer：最新
#请参阅https://github.com/kivy/buildozer/blob/master/Dockerfile

#使入口点可执行
RUNchmod+x/action/entrypoint.py

#安装Buildozer(如果需要特定版本，请根据需要进行调整)
RUNpip3安装-y造土铲

#安装Buildozer最新JDK
RUNsudo apt-get更新&&\
sudo apt-get安装-y软件-属性-通用&&\
sudo rm-rf/var/lib/apt/lists/*
RUNsudo add-apt-repository ppa:openjdk-r/ppa
RUNsudo apt更新
RUNsudo apt-get-y安装openjdk-17-jdk

#修复sudo警告
RUN回声"Set d我的一个ble_coreduimp f一个else"|sudo tee-a/etc/sudo.conf>/dev/null

#禁用python输出缓冲
envPYTHONUN缓冲=1

#复制入口点脚本
复制entrypoint.py/action/entrypoint.py

入口点["/action/entrypoint.py"]
