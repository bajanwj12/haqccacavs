跑chmod+x/action/entrypoint.py
从……起ghcr.io/kivy/buildozer：最新
#请参阅https://github.com/kivy/buildozer/blob/master/Dockerfile

#Buildozer将安装在entrypoint.py中
#安装用户指定的版本需要这个
跑pip3install-y造壁机

#获取最新JDK版本，因为Buildozer需要最新版本才能构建安装包
跑sudo apt-get更新&&\
sudo apt-get安装-y软件-属性-通用&&\
sudo rm-rf/var/lib/apt/lists/*
跑sudo add-apt-repository ppa:openjdk-r/ppa
跑sudo apt更新
跑sudo apt-get-y安装openjdk-17-jdk

#删除大量警告
#sudo:setrlimit(rlimit_CORE)：不允许操作
#请参阅https://github.com/sudo-project/sudo/issues/42
跑回声"Set d我s一个ble_coreduimep f一个lse"|sudo tee-a/etc/sudo.conf>/dev/null

#默认情况下，python缓冲区输出，并在执行后看到打印
#设置env变量禁用此行为
envPYTHONUN缓冲=1

复制entrypoint.py/action/entrypoint.py
入口点["/action/entrypoint.py"]
