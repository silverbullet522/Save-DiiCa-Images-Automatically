### 准备工作

开始扒图之前，首先你需要准备好mitmdump，PC为安卓端配置好代理，这些步骤请自行在网上查询。

大致步骤：PC安装mitmdump->安卓端配置代理->安卓端安装mitmdump证书->clash打开服务模式和tun模式（在境外的就不用这一步ww）->运行该项目

mitm默认端口是8080，配置安卓端口时使用mitm的端口就好，clash设置好tun模式就行，不用把clash的端口也改为8080

安卓端的操作建议直接在PC上使用安卓模拟器进行。

### 可能遇到的问题

**1**.有些安卓模拟器（比如雷电）在设置代理后，并不能生效（体现在访问mimt.it时提示没有透过代理）

**解决办法**：https://blog.csdn.net/kxltsuperr/article/details/133412233

这个地方看到设置完代理就行，安装证书的过程看下面。

**2**.安卓7以后安卓app就不再支持用户证书了，所以通过PC代理后，手机只有浏览器有网，而app都没有网。所以需要把证书安装为系统证书。

**解决办法**：https://cloud.tencent.com/developer/article/2186752

上传证书时碰到的其他问题可以百度相应的报错信息，应该很好解决。

### 扒图流程

1. 先运行step1.bat，或者直接在目录下打开 cmd 运行`mitmdump -s save_responses.py`。

2. 命令窗口出来后，先在终端输入1或2选择从DiiCa或是Liella\LiyuuCollection中保存响应。

3. 安卓端打开对应APP或网页，进入卡包的图鉴页面，手动滑动该页面一直到底。这时应该会自动生成`reponses`文件夹，在里面保存响应报文。这里可以连续点入多个卡包，一次性保存。

4. 保存完之后，可以选择关闭当前终端。

5. 再运行step2.bat，或者直接在目录下打开 cmd 运行`python save_pictures.py`，等待自动下载。结束后如果图片有缺漏可以再次执行依次step2，会跳过已保存的图片。

   没装python的话，第二步可以直接运行save_pictures.exe可执行文件。
