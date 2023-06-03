import requests
from lxml import etree
import xlwings
import redis


# 函数-获取列表页面总页数,链接,标题
def page_home(url_home):
    try:  # 获取首页(url_home)
        responses = requests.get(url_home, headers=headers, timeout=(100, 100))
        responses.raise_for_status()  # 如果发送失败请求(非200响应)，我们可以通过Response.raise_for_status()抛出异常。
        responses.encoding = responses.apparent_encoding  # 其中response.apparent_encoding为获取响应对象的编码格式,response.encoding为设置对象的编码格式
    except:
        print('网址错误' + url_home)
        print("列表内容获取失败!")

    # 实例化首页
    tree = etree.HTML(responses.text)
    # 获取总页数
    pages = tree.xpath('//*[@id="main"]/div[10]/span[2]/div/span/span/text()')
    pages_num = pages[0].split("/")[-1]
    # 获取网址列表
    url_list = tree.xpath('//td[@class="tal"]/a/@href')
    # 获取标题列表
    name_list = tree.xpath('//td[@class="tal"]/a//text()')
    # 函数返回 总页数,标题列表,url列表
    return pages_num, name_list, url_list



# 函数-获取网页文字性内容
def get_html_text(url):
    try:
        # 获取url网页
        response = requests.get(url=url, headers=headers, timeout=(120, 120))
        response.raise_for_status()
        response.encoding = response.apparent_encoding
    except:
        print("连接异常")
    # 实例化网页对象
    tree = etree.HTML(response.text)
    # 获取页面内容
    cont_text = tree.xpath('//*[@id="read_tpc"]//text()')

    # 函数返回页面内容
    return cont_text



"""
# 建立redis连接池
pool = redis.ConnectionPool(host="192.168.188.100", port=6379,
                            decode_responses=True)  # decode_responses=True,将redis二进制转换为字符串
r = redis.Redis(connection_pool=pool)
"""

"""
# 直接保存到本地excel中,缺点是不能更新去重
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/587.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4632.99 Safari/531.36'}
url_home = "https://jajibot.com/2048/thread.php?fid-4-page-1.html"
url_head = "https://jajibot.com/2048/"

# 运行函数page_home(),获取url-home网址的总页数,当前页面的url列表,标题列表
page_num, name_list, url_list = page_home(url_home)

# 打开本地xlsx文件
wb1 = xlwings.Book("2048content.xlsx")
sht1 = wb1.sheets[1]  # 打开第二个表格
hang = 1  # 表格中的第一行
# 根据列表总页数来获取每一个列表页面
for ls in range(int(page_num)):
    rg = 0  # 对url列表及标题列表进行切片
    # 逐个取出标题列表中的标题
    for tit in name_list:
        sht1.range("a{}".format(hang)).value = tit  # 将标题存入excel中
        sht1.range("b{}".format(hang)).value = url_head + url_list[rg]  # 将url存入excel中
        # 将内容存入excel中
        # sht1.range("c{}".format(hang)).value=str(get_html_text(url_head+url_list[rg])).replace("\\xa0",
        # '').replace("\\u3000", "") #将空白字符替换掉
        hang += 1
        rg += 1
    # 利用函数解析下一主页,获取对应列表,并进行下一循环
    page_num, name_list, url_list = page_home("https://jajibot.com/2048/thread.php?fid-4-page-{}.html".format(ls + 2))
wb1.save()
wb1.close()
"""

"""
#保存到redis中hash格式
#建立redis连接池
pool = redis.ConnectionPool(host="192.168.188.100", port=6379,decode_responses=True)
r = redis.Redis(connection_pool=pool)
#用url作为name存入hash表中,mapping={}可存入多个值
r.hset(url, mapping={"url":url,"标题": "2048的标题内容", "内容": str(get_html_text(url))})
print(r.hget(url, "标题"))
print("页面内容是这些:", r.hget(url, "内容"))
print(r.hgetall(url))
print(r.hkeys(url))
print(r.hvals(url))
print(r.keys())
"""



# 保存为redis列表
# 建立redis连接池
pool = redis.ConnectionPool(host="192.168.188.100", port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/587.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4632.99 Safari/531.36'}
url_home = "https://jajibot.com/2048/thread.php?fid-4-page-1.html"
url_head = "https://jajibot.com/2048/"
# 从主页获取总列表页数,主页url列表,标题列表
page_num, name_list, url_list = page_home(url_home)

for num in range(0,int(page_num)):  # 解析每一个列表页
    n = 0  # 切片数
    for i in url_list:  # 解析每一个url
        i = url_head + i  # 使url完整
        # print(i)
        # print(name_list[n])
        # 利用redis中的集合更新并去重
        if r.sadd('set1', i) and r.sadd("set2", name_list[n]):
            # 将内容添加到列表中
            r.rpush(i, i, name_list[n])  # , (str(get_html_text(i)).replace("\\xa0", '')).replace("\\u3000", "")
            print(r.lrange(i, 0, -1))
            print("添加成功")

        else:
            print("已存在,不更新")
        n = n + 1
    # 解析下一页
    # 若有解析页错误,则跳过
    try:
        if num >= int(page_num)-1: # 设置需要更新的页数 if num >= 49 :
            print("任务完成")
            break
        else:
            url_home = "https://jajibot.com/2048/thread.php?fid-4-page-{}.html".format(num + 2)
            page_num, name_list, url_list = page_home(url_home)
    except:
        print('此页错误,跳过此页')
"""



# 将redis中的数据写入excel
# 打开已有的excel表
wb = xlwings.Book("2048content.xlsx")
sht_rd = wb.sheets[1]
# 获取redis中所有的键
redis_list = r.keys()
num_re = 1  # excel表中行的值
for rd in redis_list:  # 从数据库中取出每一个值
    try:
        if len(rd) >= 5:  # 排除数据库中set1和set2
            sht_rd.range("a{}".format(num_re)).value = r.lrange(rd, 0, 0)  # 列表中的第一个值为url
            sht_rd.range("b{}".format(num_re)).value = r.lrange(rd, 1, 1)  # 列表中的第二个值为标题
            # sht_rd.range("c{}".format(num_re)).value = r.lrange(rd, 2, 2)  # 列表中的第三个值是内容页面
            num_re += 1
        else:
            pass
    except:
        print("数据错误,下一个")
wb.save()
wb.close()

