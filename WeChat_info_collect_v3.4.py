# -*- coding: utf-8 -*-
import getpass
import re
import os
import requests
import sys

provinces = '''
北京(BeiJing)

上海(ShangHai)

天津(TianJin)

重庆(ChongQing)

香港(XiangGang)

澳门(Aomen)

安徽(AnHui)

福建(FuJian)

广东(GuangDong)

广西(GuangXi)

贵州(GuiZhou)

甘肃(GanSu)

海南(HaiNan)

河北(HeBei)

河南(HeNan)

黑龙江(HeiLongJiang)

湖北(HuBei)

湖南(HuNan)

吉林(JiLin)

江苏(JiangSu)

江西(JiangXi)

辽宁(LiaoNing)

内蒙古(NeiMengGu)

宁夏(NingXia)

青海(QingHai)

陕西(ShanXi)

山西(ShanXi)

山东(ShanDong)

四川(SiChuan)

台湾(TaiWan)

西藏(XiZang)

新疆(XinJiang)

云南(YunNan)

浙江(ZheJiang)

'''
cities = '''
香港(XiangGang)
东城区(dongcheng)
西城区(xicheng)
朝阳区(chaoyang)(zhaoyang)
丰台区(fengtai)
石景山区(shijingshan)
海淀区(haidian)
门头沟区(mentougou)
房山区(fangshan)
通州区(tongzhou)
顺义区(shunyi)
昌平区(changping)
大兴区(daxing)
澳门(AoMen)
安庆(AnQing)，亳州(BoZhou)，蚌埠(BangBu)，池州(ChiZhou)，巢湖(ChaoHu)，滁州(ChuZhou)，阜阳(FuYang)，合肥(HeFei)，淮南(HuaiNan)，淮北(HuaiBei)，黄山(HuangShan)，六安(LiuAn)，马鞍山(MaAnShan)，宿州(SuZhou)，铜陵(TongLing)，芜湖(WuHu)，宣城(XuanCheng)

福州(FuZhou)，龙岩(LongYan)，南平(NanPing)，宁德(NingDe)，莆田(PuTian)，泉州(QuanZhou)，三明(SanXing)，厦门(XiaMen)，漳州(ZhangZhou)

潮州(ChaoZhou)，东莞(DongGuan)，佛山(FoShan)，广州(GuangZhou)，河源(HeYuan)，惠州(HuiZhou)，江门(JiangMen)，揭阳(JieYang)，梅州(MeiZhou)，茂名(MaoMing)，清远(QingYuan)，深圳(ShenZhen)，汕头(ShanTou)，韶关(ShaoGuan)，汕尾(ShanWei)，云浮(YunFu)，阳江(YangJiang)，珠海(ZhuHai)，中山(ZhongShan)，肇庆(ZhaoQing)，湛江(ZhanXiang)

北海(BeiHai)，百色(BaiSe)，崇左(ChongZuo)，防城港(FangChengGang)，桂林(GuiLi)，贵港(GuiGang)，贺州(HeZhou)，河池(HeChi)，柳州(LiuZhou)，来宾(LaiBin)，南宁(NanNing)，钦州(QinZhou)，梧州(WuZhou)，玉林(YuLin)

安顺(AnShun)，贵阳(GuiYang)，六盘水(LiuPanShui)，遵义(ZunYi)

白银(BaiYin)，金昌(JinChang)，嘉峪关(JiaYuGuan)，酒泉(JiuQuan)，兰州(LanZhou)，庆阳(QingYang)，天水(TianShui)，武威(WuWei)，张掖(ZhangYe)

海口(HaiKou)，三亚(SanYa)

保定(BaoDing)，承德(ChengDe)，沧州(CangZhou)，邯郸(HanDan)，衡水(HengShui)，廊坊(LangFang)，秦皇岛(QinHuangDao)，石家庄(ShiJiaZhuang)，唐山(TangShan)，邢台(XingTai)，张家口(ZhangJiaKou)

安阳(AnYang)，焦作(JiaoZuo)，开封(KaiFeng)，洛阳(LuoYang)，鹤壁(HeBi)，漯河(LuoHe)，南阳(NanYang)，平顶山(PingDingShan)，濮阳(PuYang)，三门峡(SanMenXia)，商丘(SHangQiu)，新乡(XinXiang)，许昌(XuChang)，信阳(XinYang)，郑州(ZhengZhou)，周口(ZhouKou)，驻马店(ZhuMaDian)

大庆(DaQing)，哈尔滨(HaErBin)，鹤岗(HeGang)，黑河(HeiHe)，鸡西(JiXi)，佳木斯(JiaMuSi)，牡丹江(MuDanJiang)，齐齐哈尔(QiQiHaEr)，七台河(QiTaiHe)，绥化(SuiHua)，双鸭山(ShuangYaShan)，伊春(YiChun)

鄂州(E'Zhou)，黄石(HuangShi)，黄冈(HuangGang)，荆州(JingZhou)，荆门(JingMen)，十堰(ShiYan)，武汉(WuHan)，襄阳(XiangYang)，孝感(XiaoGan)，咸宁(XianNing)，宜昌(YiChang)

长沙(ChangSha)，常德(ChangDe)，郴州(ChenZhou)，衡阳(HengYang)，怀化(HuaiHua)，娄底(LouDi)，邵阳(ShaoYang)，湘潭(xiangTan)，岳阳(YueYang)，益阳(YiYang)，永州(YongZhou)，株洲(ZhuZhou)，张家界(ZhangJiaJie)

白山(BaiShan)，白城(BaiCheng)，长春(ChangChun)，吉林(JiLin)，辽源(LiaoYuan)，四平(SiPing)，松原(SongYuan)，通化(TongHua)

常州(ChangZhou)，淮安(HuaiAn)，连云港(LianYunGang)，南京(NanJing)，南通(NanTong)，苏州(SuZhou)，宿迁(SuQian)，泰州(TaiZhou)，无锡(WuXi)，徐州(XuZhou)，盐城(YanCheng)，扬州(YangZhou)，镇江(ZhenJiang)

抚州(FuZhou)，赣州(GanZhou)，景德镇(JingDeZhen)，九江(JiuJiang)，吉安(JiAn)，南昌(NanChang)，萍乡(PingXiang)，上饶(ShangRao)，新余(XinYu)，鹰潭(YingTan)，宜春(YiChun)

鞍山(AnShan)，本溪(BenXi)，朝阳(ChaoYang)，大连(DaLian)，丹东(DanDong)，抚顺(FuShun)，阜新(FuXin)，葫芦岛(HuLuDao)，锦州(JinZhou)，辽阳(LiaoYang)，盘锦(PanJin)，沈阳(ShenYang)，铁岭(TieLing)，营口(YingKou)

包头(BaoTou)，赤峰(ChiFeng)，鄂尔多斯(E'ErDuoSi)，呼和浩特(HuHeHaoTe)，通辽(TongLiao)，乌海(WuHai)

固原(GuYuan)，吴忠(WuZhong)，银川(YingChuan)

西宁(XiNing)

安康(AnKang)，宝鸡(BaoJi)，汉中(HanZhong)，商洛(ShangLuo)，铜川(TongChuan)，渭南(WeiNan)，西安(Xi'An)，延安(YaNan)，咸阳(XianYang)，榆林(YuLin)

长治(ChangZhi)，大同(DaTong)，晋城(JinCheng)，临汾(LinFen)，朔州(ShuoZhou)，太原(TaiYuan)，忻州(XinZhou)，阳泉(YangQuan)，运城(YunCheng)

滨州(BinZhou)，东营(DongYing)，德州(DeZhou)，菏泽(HeZe)，济南(JiNan)，济宁(JiNing)，莱芜(LaiWu)，临沂(LinYi)，聊城(LiaoCheng)，青岛(QingDao)，日照(RiZhao)，泰安(TaiAn)，潍坊(WeiFang)，威海(WeiHai)，烟台(YanTai)，淄博(ZiBo)，枣庄(ZaoZhuang)

巴中(BaZhong)，成都(ChengDu)，德阳(DeYang)，达州(DaZhou)，广元(GuangYuan)，广安(GuangAn)，泸州(LuZhou)，乐山(LeShan)，绵阳(MianYang)，眉山(MeiShan)，内江(NeiJiang)，南充(NanChong)，攀枝花(PanZhiHua)，遂宁(SuiNing)，雅安(YaAn)，宜宾(YiBin)，自贡(ZiGong)，资阳(Ziyang)

高雄(GaoXiong)，基隆(JiLong)，嘉义(JiaYi)，台北(TaiBei)，台中(TaiZhong)，新竹(XinZhu)

拉萨(LaSa)

克拉玛依(KeLaMaYi)，乌鲁木齐(WuLuMuQi)

保山(BaoShan)，昆明(KunMing)，玉溪(YuXi)，昭通(ZhaoTong)

杭州(HangZhou)，湖州(HuZhou)，嘉兴(JiaXing)，金华(JinHua)，丽水(LiShui)，宁波(NingBo)，衢州(QuZhou)，绍兴(ShaoXing)，台州(TaiZhou)，温州(WenZhou)，舟山(ZhouShan)
'''

# 判断操作系统
os_name = os.name
if os_name == "nt":
    os_name = "windows"
    flag = input("Do you want to collect all applets (yes/no): ")
    if flag == "yes":
        cookie = input("Please enter your cookie: ")
        token = input("Please enter your token: ")
    else:
        pass
    print("============================================")
if os_name == "posix":
    # linux/unix
    os_name = "linux"

# 获取文件存储位置
if os_name == "windows":
    import win32api
    import win32con

    reg_root = win32con.HKEY_USERS
    reg_path = ""

    key = win32api.RegOpenKey(reg_root, reg_path, 0)
    for item in win32api.RegEnumKeyEx(key):
        if len(item[0]) > 20 and "Classes" not in item[0]:
            sub_reg_path = item[0] + "\\SOFTWARE\\Tencent\\WeChat"
            try:
                key = win32api.RegOpenKeyEx(reg_root, sub_reg_path, 0)
            except Exception as e:
                continue
    try:
        value, key_type = win32api.RegQueryValueEx(key, 'FileSavePath')
    except Exception as e:
        value, key_type = win32api.RegQueryValueEx(key, 'InstallPath')
        value = value + "\\locales\\WeChat Files\\"
    # print(value)
    # 文件保存路径
    if value == "MyDocument:":
        # print("The default location of the file has not been changed")
        username = getpass.getuser()
        file_path = "C:\\Users\\" + username + "\\Documents\\WeChat Files\\"
        # print(file_path)
    else:
        file_path = value

    # 获取用户文件
    try:
        # print(file_path)
        file_list = os.listdir(file_path)
        file_list.remove("All Users")
        file_list.remove("Applet")
    except:
        print("\nfailed to find the path by the script")
        print("Please enter the path of your [WeChat Files]")
        print("You can find the path in your WeChat's setting")
        print("It looks like [x:\\\\xxx\\xxx\\WeChat Files]")
        file_path = input("The path : ") + "\\"
        file_list = os.listdir(file_path)
        file_list.remove("All Users")
        file_list.remove("Applet")

# mac地址
if os_name == "linux":
    file_list = []
    user_name = os.getlogin()
    file_path = "/Users/" + user_name + "/library/containers/com.tencent.xinWECHAT/data/library/application " \
                                        "support/com.tencent.xinWeChat/2.0b4.0.9/"
    files_list = os.listdir(file_path)
    for file_name in files_list:
        if len(file_name) == 32:
            file_list.append(file_name)


def check_wxid_version(raw_info):
    global wxid_version
    if "wxid_" in raw_info:
        wxid_version = "new_wxid"
    else:
        wxid_version = "old_wxid"


# info 未处理的精确结果
# 传入文件地址
def get_info(user_file_name):
    if os_name == "windows":
        file = file_path + user_file_name + "\\config\\AccInfo.dat"
        file_size = os.path.getsize(file)
    if os_name == "linux":
        file = file_path + user_file_name + r"/account/userinfo.data"
        file_size = os.path.getsize(file)

    if file_size == 0:
        return

    with open(file, mode="r", encoding="ISO-8859-1") as f:
        # 处理raw数据
        raw_info = f.read()
        # 获取原始wxid的版本
        check_wxid_version(raw_info)
        if os_name == "windows":
            if wxid_version == "new_wxid":
                raw_info = raw_info[raw_info.find("wxid"):]
            if wxid_version == "old_wxid":
                raw_info = raw_info
        if os_name == "linux":
            c_p_c = raw_info[:raw_info.find(":")]
            raw_info = raw_info[raw_info.find("wxid"):]
        info = ""
        for char in raw_info:
            if "\\" not in ascii(char):
                info = info + str(char)
            else:
                info = info + "`"
        info_2 = list(set(info.split("`")))
        info_2.sort(key=info.index)
        info = info_2
        info_list = []
        for x in info:
            if len(x) > 1:
                info_list.append(x)
        info = info_list
        if wxid_version == "old_wxid":
            for x in info:
                an = re.search("[a-zA-Z0-9_]+", x)
                if len(x) >= 6 and len(an.group(0)) >= 6:
                    d_list = r"!@#$%^&*()+={}|:\"<>?[]\;',./`~'"
                    flag_id = 0
                    for i in x:
                        if i in d_list:
                            wxid = x.replace(i, "")
                            flag_id = 1
                    if flag_id == 0:
                        wxid = an.group(0)
                    break
            info = info[info.index(x):]
            info[0] = wxid

    if info != []:
        # 获取微信id
        try:
            wxid = info[0]
            print("The wxid : " + wxid)
        except:
            pass

        # 获取城市
        if os_name == "windows":
            province = ""
            city = ""
            for misc in info:
                if misc.lower() in provinces.lower() and len(misc) >= 2:
                    province = misc
                    continue
                if misc.lower() in cities.lower() and len(misc) >= 2:
                    city = misc
                    continue
            try:
                if province != "":
                    info.remove(province)
                if city != "":
                    info.remove(city)
            except:
                pass

        if os_name == "linux":
            if "CN" in c_p_c:
                c_p_c = c_p_c.replace("CN", "")
                c_p = c_p_c.split("\"")
                c_p_flag = 1

        # 获取微信号
        # 微信号长度限制为6-20位, 且只能以字母开头
        try:
            for misc in info:
                if 6 <= len(misc) <= 20 and misc[0].isalpha() is True:
                    wx = misc
            print("The wechat : " + wx)
            info.remove(wx)
        except:
            print("The wechat : " + wxid)

        # 获取手机号
        for misc in info:
            p_numbers = r"[\+0-9]+"
            p = re.compile(p_numbers)
            numbers = re.search(p, misc)
            try:
                if "+" in numbers.group(0) and len(numbers.group(0) >= 6):
                    number = numbers.group(0)
                else:
                    p_numbers = r"0?(13|14|15|17|18|19)[0-9]{9}"
                    p = re.compile(p_numbers)
                    numbers = re.search(p, misc)
                    number = numbers.group(0)
            except:
                continue
            if "*" in number:
                number = number.replace("*", "")
            print("The phone : " + number)
            try:
                info.remove(number)
            except:
                info.remove(number + "*")
            break

        # 获取疑似邮箱, 邮箱参考性极低
        for misc in info:
            if "@" in misc and len(misc) > 3 and "." in misc:
                email = misc
                break
            else:
                email = "--"
        if "*" in email:
            email_ = email.replace("*", "")
        else:
            email_ = email
        print("The email maybe is : " + email_)
        if email != "--":
            info.remove(email)

        if os_name == "windows":
            print("The city : " + province + " - " + city)
        if os_name == "linux" and "CN" in c_p_c and c_p_flag == 1:
            print("The city : " + c_p[0] + " - " + c_p[1])

        # 获取使用过的小程序
        if os_name == "windows":
            if flag == "yes":
                applet_list = []
                applet_path = file_path + user_file_name
                sub_applet_list = os.listdir(applet_path)
                if "Applet" in sub_applet_list:
                    applet_path = file_path + user_file_name + "\\Applet"
                    sub_applet_list = os.listdir(applet_path)
                    for applet_name in sub_applet_list:
                        if "wx" in applet_name:
                            applet_list.append(applet_name)

                applet_search_url = r"https://mp.weixin.qq.com/cgi-bin/operate_appmsg?sub=search_weapp"
                headers = {
                    "Host": "mp.weixin.qq.com",
                    "Connection": "close",
                    "Content-Length": "39",
                    "sec-ch-ua": "Not A;Brand",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "charset": "UTF-8",
                    "X-Requested-With": "XMLHttpRequest",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch ua-platform": "Windows",
                    "Accept": "* / *",
                    "Origin": "https://mp.weixin.qq.com",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=77&token=" + token + "&lang=zh_CN",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh - CN, zh",
                    "Cookie": cookie
                }

                applets = []
                for key in applet_list:
                    data = {
                        "key": key,
                        "token": token
                    }

                    req_json = requests.post(applet_search_url, headers=headers, data=data).json()
                    applets.append(req_json["items"][0]["weapp"]["nickname"])
                    # print(req["items"][0]["weapp"]["nickname"])
                print("The applets : " + str(applets))

        # 获取历史头像网址
        head_url = []
        rm_url = []
        for misc in info:
            if "http://" in misc:
                index_http = misc.find("http")
                misc_http = misc[index_http:]
                if "*" in misc_http:
                    misc_2 = misc_http.replace("*", "")
                    head_url.append(misc_2)
                    rm_url.append(misc)
                else:
                    head_url.insert(-1, misc_http)
                    rm_url.append(misc)
        if head_url != []:
            print("The history_head_img : " + str(head_url))
        else:
            print("The history_head_img : --")
        for url in rm_url:
            try:
                info.remove(url)
            except:
                info.remove(url + "*")

        # 杂项数据
        other_info = []
        for misc in info:
            if len(misc) > 30:
                if "*" in misc:
                    misc = misc.replace("*", "")
            if len(misc) > 30 or (len(misc) >= 2 and misc.isdigit() is True):
                other_info.insert(-1, misc)
        print("The other info : " + str(other_info))
        print("\n" + "--------------------------------------------")


# 理论来说2.0b4.0.9应该不会变
# 这个命名从18年到现在似乎没变过, 所以就不麻烦写代码来获取了
# 以后要是变了改了就是
for user_file_name in file_list:
    # try:
    if os_name == "linux":
        is_null = os.listdir(file_path + user_file_name)
        if "Account" in is_null:
            get_info(user_file_name)
        else:
            break
    if os_name == "windows":
        get_info(user_file_name)

print(" 1. The email is very unreliable, you can ignore it\n",
      "2. There are only cities of the mainland\n",
      "3. The information in [The other info] is some ciphertext and abbreviation for region\n",
      "4. There is some interference information in [The other info]"
      )
