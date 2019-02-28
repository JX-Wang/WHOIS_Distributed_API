# WHOIS API Service

🕷 一个基于Flask的分布式Whois获取Api

### USE
不添加whois服务器```curl http://ip:port/WHOIS/<domain>```

添加whois服务器```curl http://ip:port/WHOIS/<domain:whois_srv>```



### Mode
  mode示意图重做中...
![](https://github.com/WUD-51/WHOIS-API/blob/master/Demo.jpg)

## API_Server（主节点）

*This Server is used for sending domain's whois query to Client*

### 说明：基于flask和gevent的whois任务分发的并发API

### 功能：根据用户发来的域名在数据库中找到对应的whois服务器，将域名和对应的whois服务器发送给API从节点，可以选择性的加上对应的代理信息一并发送个给子节点

#### Feature：
  1. 心跳感知：
      ##### 1.1 主从节点采用心跳的的方式进行感知，主节点定时向所有的从节点发送数据，若从节点出现崩溃（即没有按照规则返回正常的数据，或者不返回数据）的情况，主节点则将其从effective节点（活跃节点）中去除，等待下一次心跳感知，在此期间，主节点只向活跃的从节点发送需要探测的数据。
      ##### 1.2 若从出现节点崩溃的情况，主节点则会向管理员发送邮件，邮件内容包括崩溃的节点的IP地址和出错节点的数量，管理员可以通过邮件内容找到出错的节点并进行维护
  2. 并发：
      ##### 2.1 基于协程```gevent monkey_patch()```和 ```gevent WSGIServer```的高性能并发模型，单节点单核日处理300w+的域名数据探测，数据正确率为约为80%
  3. 多线程:  
      通过开启多线程来分别进行分发，主从节点间的心跳感知的操作(基于schedule模块儿的定时心跳感知)
      ```python
      API_process = multiprocessing.Process(target=start, name="API SERVICE")
      API_process.start()
      monitor_process = multiprocessing.Process(target=S.monitor, name="Monitor service")
      monitor_process.start()
      ```
      基于```gevent WSGIServer```的Web服务器
      ```python
      def start():
        """API start"""
        http_server = WSGIServer(('', _port), app)
        http_server.serve_forever()
  4. proxy：
      proxy在发送时是可选的，不加proxy，API从节点也可进行whois探测，不过为了保证稳定，添加代理是一种可持续探测的必要方法  
      
      
## API_Client (从节点)  
  *The Client will get whois data from whois server*  

### 说明：从节点也是基于flask和gevent的高性能并发探测系统

### 功能：主节点发送来的domain和对应whois服务器以及代理等信息进行whois信息的探测

#### Feature：
  1. 
#### 处理过程
  用户只需向API_Server发送域名即可，如
  ```http://localhost:port/WHOIS/baidu.com```
  API_Server会对baidu.com进行处理，并将其加上对应的whois服务器（可选择加上代理），发送给API从节点，从节点返回whois数据给API_Server，API_Server再将其返回给用户
  
#### 效率
   目前测试过10w域名的whois请求，采用4个API从节点进行探测，探测速度约```0.06s/个```，whois信息正确率```95%+```
   
#### Contact
wjx.wud@gmail.com
Harbin Institute of Technology

[wjx的博客](http://www.wudly.cn)
