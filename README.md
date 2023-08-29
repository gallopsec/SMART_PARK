#  大华智慧园区综合管理平台文件上传漏洞 POC
大华智慧园区设备开放了文件上传功能，但未在上传的文件类型、大小、格式、路径等方面进行严格的限制和过滤，导致攻击者可以通过构造恶意文件并上传到设备上，然后利用该漏洞获取权限并执行任意命令。
```
Usage:
  python3  SMART-PARK.py -h
```
![示例](https://github.com/gallopsec/SMART_PARK/blob/main/poc.png)
![示例](https://github.com/gallopsec/SMART_PARK/blob/main/test1.png)
