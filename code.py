# -*- coding: utf-8 -*-
import win32api
import win32con
import getpass
import re
import os

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

# 获取文件存储位置
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
file_list = os.listdir(file_path)
file_list.remove("All Users")
file_list.remove("Applet")


# info 未处理的精确结果
user_file_name = "wxid_tn7r68mg8aws22"
def get_info(user_file_name):
    with open(file_path+user_file_name+"\\config\\AccInfo.dat", mode="r", encoding="ISO-8859-1") as f:
        # 处理raw数据
        raw_info = f.read()
        raw_info = raw_info[raw_info.find("wxid"):]
        info = ""
        for char in raw_info:
            if "\\" not in ascii(char):
                info = info + str(char)
            else:
                info = info + "`"
    info = set(info.split("`"))

    # 获取微信id
    for misc in info:
        if "wxid" in misc:
            wxid = misc
    print("The wxid : " + wxid)
    info.remove(wxid)

    # 获取城市
    province = ""
    city = ""
    for misc in info:
        if misc.lower() in provinces.lower() and len(misc) >= 2:
            province = misc
        if misc.lower() in cities.lower() and len(misc) >= 2:
            city = misc
    if province != "":
        info.remove(province)
    if city != "":
        info.remove(city)

    # 获取微信号
    # 微信号长度限制为6-20位, 且只能以字母开头
    for misc in info:
        if 6 < len(misc) < 20 and misc[0].isalpha() == True:
            wx = misc
    print("The wechat : " + wx)
    info.remove(wx)

    # 获取手机号
    for misc in info:
        p_numbers = r"0?(13|14|15|17|18|19)[0-9]{9}"
        p = re.compile(p_numbers)
        numbers = re.search(p, misc)
        if numbers != None:
            number = numbers.group(0)
            info.remove(number)
            break
    print("The number : " + number)

    # 获取疑似邮箱, 邮箱参考性极低
    for misc in info:
        if "@" in misc and len(misc) > 3:
            email = misc
            break
        else:
            email = "--"
    print("The email maybe is : " + email)
    if email != "--":
        info.remove(email)

    print("The city : " + province + "--" + city)

    # 获取历史头像网址
    head_url = []
    for misc in info:
        if "http" in misc:
            head_url.insert(-1, misc)
    if head_url != []:
        print("The history_head_img : " + str(head_url))
    else:
        print("The history_head_img : --")
    for url in head_url:
        info.remove(url)

    # 杂项数据
    other_info = []
    for misc in info:
        if len(misc) > 30 or (len(misc) >= 2 and (misc.isdigit() == True or misc.isalpha()) == True):
            other_info.insert(-1, misc)
    print("The other info : " + str(other_info))
    print("\n" + "--------------------------------------------")

# 运行
for user_file_name in file_list:
    #try:
    get_info(user_file_name)
    #except:
    #print("Something wrong")

print(" 1. The email is very unreliable, you can ignore it\n",
    "2. There are only cities of the mainland\n",
    "3. The informations in [The other info] are some ciphertext and abbreviation for region\n",
    "4. There is some interference information in [The other info]"
)