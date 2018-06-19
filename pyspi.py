from bs4 import BeautifulSoup
import re
import json
import requests


def getPrice(brand="iphonex"):
    url="https://search.jd.com/Search?keyword="+brand+"&enc=utf-8&wq=iphonex&pvid=bcb1dd6c4a3d4fae8d15f7f412237340"
    wb=requests.get(url)
    soup=BeautifulSoup(wb.text,"lxml")

    prices=soup.select('strong > i')
    for price in prices:
    	print(price.text)
    return prices    


def getRepu():
    url="http://club.jd.com/productpage/p-5089253-s-0-t-3-p-0.html?callback=fetchJSON_comment98vv4712"
    resData=requests.get(url).text
    jsonStr = re.findall(r'fetchJSON_comment98vv4712\((.*?)\);', resData)[0]
    data = json.loads(jsonStr)
    summary = data["productCommentSummary"]
    print("全部评价", summary["commentCount"], "好评", summary["goodCount"], "中评", summary["generalCount"], "差评", summary["poorCount"]) 
    repu="全部评价 %s \n好评 %s \n中评 %s \n差评 %s " % (summary["commentCount"],summary["goodCount"] ,summary["generalCount"],summary["poorCount"])
    
    return repu

def getBrand():
    for i in range(0,2):
        b=i*2-1
        c=1+30*(i-1)
        url="https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page="+str(b)+"&s="+str(c)+"&click=0"

        data=requests.get(url)
        data.encoding='utf-8'
        soup=BeautifulSoup(data.text,"lxml")
        te=soup.select('div.p-name.p-name-type-2 > a > em')
        for t in te:
           print(t.text+"\n")
    return te
if __name__ == '__main__':
    getPrice()
    getBrand()
    getRepu()