## WHOIS信息获取API从节点
---  
## API_Client (从节点)  
  *The Client will get whois data from whois server*  

### 说明：从节点也是基于flask和gevent的高性能并发探测系统

### 功能：主节点发送来的domain和对应whois服务器以及代理等信息进行whois信息的探测

#### Features：
  - 通过TCP协议，直接与whois服务器交互，获取whois信息
  - 采用动态解析，对不同whois服务器返回的数据采用不同的提取函数解析数据
  - 采用协程，高并发模型获取whois数据
  - 对于不同质量的whois数据，使用不同的flag进行标记，便于分析处理
#### 处理过程
  用户只需向API_Server发送域名即可，如
  ```http://localhost:port/WHOIS/baidu.com```
  API_Server会对baidu.com进行处理，并将其加上对应的whois服务器（可选择加上代理），发送给API从节点，从节点返回whois数据给API_Server，API_Server再将其返回给用户
  
#### 效率
   目前测试过10w域名的whois请求，采用4个API从节点进行探测，探测速度约```0.06s/个```，whois信息正确率```95%+```
### WHOIS获取核心代码见 [这里](https://github.com/JX-Wang/WHOISpy)

 
