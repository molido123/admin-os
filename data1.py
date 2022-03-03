#!/usr/bin/python3.8
import pymysql

dict= [
    {'studentId': '08213101', 'name': '何通洋', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '甘肃省 平凉市 泾川县', 'phone': '15352070721', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '02210621', 'name': '华根达', 'departments': '计算机科学与技术学院', 'major': '神秘学', 'address': '幻想乡', 'phone': '18361457436', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213197', 'name': '黎娜', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '西藏自治区 阿里地区 措勤县', 'phone': '18175678478', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213710', 'name': '王平', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '香港特别行政区 九龙 黄大仙区', 'phone': '18635246270', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213420', 'name': '许娟', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '江苏省 扬州市 其它区', 'phone': '18125047983', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213516', 'name': '任敏', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '辽宁省 盘锦市 大洼县', 'phone': '18184767719', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213944', 'name': '常军', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '吉林省 通化市 梅河口市', 'phone': '18122835847', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213751', 'name': '龙洋', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '福建省 龙岩市 漳平市', 'phone': '18181583292', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213769', 'name': '白敏', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '云南省 玉溪市 江川县', 'phone': '18602783675', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213060', 'name': '周娟', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '广西壮族自治区 玉林市 陆川县', 'phone': '19835686292', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213663', 'name': '何秀英', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '湖南省 常德市 武陵区', 'phone': '18686644197', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213149', 'name': '易磊', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '内蒙古自治区 通辽市 其它区', 'phone': '18165538343', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213500', 'name': '彭明', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '云南省 文山壮族苗族自治州 西畴县', 'phone': '13262517287', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213475', 'name': '蒋娜', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '新疆维吾尔自治区 博尔塔拉蒙古自治州 精河县', 'phone': '19836544887', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213255', 'name': '刘刚', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '江西省 宜春市 丰城市', 'phone': '18111770120', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213002', 'name': '许伟', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '辽宁省 葫芦岛市 南票区', 'phone': '19827644335', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213420', 'name': '段丽', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '云南省 怒江傈僳族自治州 兰坪白族普米族自治县', 'phone': '13168656865', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213359', 'name': '郭强', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '山东省 潍坊市 昌邑市', 'phone': '13955790927', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213780', 'name': '宋明', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '安徽省 淮南市 田家庵区', 'phone': '19873358164', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213331', 'name': '曾杰', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '重庆 重庆市 大渡口区', 'phone': '18616332076', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213828', 'name': '赖桂英', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '河南省 周口市 西华县', 'phone': '19843226289', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213534', 'name': '龙娜', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '福建省 三明市 清流县', 'phone': '18626338338', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213884', 'name': '刘涛', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '西藏自治区 日喀则地区 萨迦县', 'phone': '19837305459', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213971', 'name': '阎磊', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '辽宁省 铁岭市 其它区', 'phone': '18141222102', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213168', 'name': '陆勇', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '河北省 张家口市 张北县', 'phone': '18636284453', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213389', 'name': '孟平', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '新疆维吾尔自治区 喀什地区 莎车县', 'phone': '18142224539', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213081', 'name': '赖芳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '贵州省 黔东南苗族侗族自治州 榕江县', 'phone': '18638076243', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213835', 'name': '赵磊', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '云南省 德宏傣族景颇族自治州 陇川县', 'phone': '18112468551', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213455', 'name': '夏平', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '湖北省 恩施土家族苗族自治州 利川市', 'phone': '18124771044', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213301', 'name': '宋平', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '香港特别行政区 新界 屯门区', 'phone': '18607814033', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213838', 'name': '锺超', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '黑龙江省 鹤岗市 萝北县', 'phone': '18147138719', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213324', 'name': '史芳', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '青海省 果洛藏族自治州 班玛县', 'phone': '18161553880', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213284', 'name': '阎刚', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '内蒙古自治区 赤峰市 巴林左旗', 'phone': '18121826684', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213083', 'name': '薛霞', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '福建省 南平市 浦城县', 'phone': '13475334779', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213357', 'name': '姜艳', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '吉林省 白城市 其它区', 'phone': '18134874140', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213732', 'name': '汪强', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '贵州省 安顺市 普定县', 'phone': '18179766148', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213373', 'name': '秦丽', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '陕西省 延安市 吴起县', 'phone': '19845176438', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213707', 'name': '黄强', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '贵州省 铜仁市 玉屏侗族自治县', 'phone': '18177313306', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213262', 'name': '康娜', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '山东省 聊城市 临清市', 'phone': '18114603238', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213814', 'name': '冯艳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '广东省 江门市 鹤山市', 'phone': '18167348821', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213197', 'name': '范平', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '重庆 重庆市 万州区', 'phone': '13561225628', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213469', 'name': '贺娜', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '香港特别行政区 香港岛 南区', 'phone': '13295421674', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213362', 'name': '黄娟', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '新疆维吾尔自治区 乌鲁木齐市 达坂城区', 'phone': '18624323516', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213911', 'name': '冯勇', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '河南省 郑州市 金水区', 'phone': '18143411269', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213645', 'name': '武丽', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '宁夏回族自治区 石嘴山市 惠农区', 'phone': '18102582445', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213169', 'name': '魏勇', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '青海省 黄南藏族自治州 河南蒙古族自治县', 'phone': '19802122419', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213381', 'name': '李勇', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '天津 天津市 武清区', 'phone': '18162185262', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213223', 'name': '萧静', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '西藏自治区 阿里地区 改则县', 'phone': '18151498624', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213601', 'name': '顾明', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '广东省 肇庆市 高要市', 'phone': '18143478896', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213333', 'name': '沈丽', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '浙江省 温州市 乐清市', 'phone': '18618223449', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213347', 'name': '黎刚', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '湖南省 娄底市 涟源市', 'phone': '18116367413', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213271', 'name': '周芳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '宁夏回族自治区 银川市 贺兰县', 'phone': '13670199182', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213554', 'name': '林杰', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '江苏省 无锡市 北塘区', 'phone': '18661241652', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213788', 'name': '许桂英', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '四川省 巴中市 通江县', 'phone': '18657369007', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213379', 'name': '郭娜', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '海南省 海口市 龙华区', 'phone': '18683612478', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213316', 'name': '汤洋', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '新疆维吾尔自治区 吐鲁番地区 其它区', 'phone': '18126563061', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213939', 'name': '谢洋', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '广西壮族自治区 来宾市 金秀瑶族自治县', 'phone': '18141176861', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213205', 'name': '江洋', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '香港特别行政区 新界 沙田区', 'phone': '18138770474', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213028', 'name': '姚明', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '湖北省 荆门市 沙洋县', 'phone': '18652315355', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213834', 'name': '任芳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '云南省 临沧市 双江拉祜族佤族布朗族傣族自治县', 'phone': '18132465213', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213155', 'name': '余强', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '天津 天津市 和平区', 'phone': '18643502520', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213947', 'name': '乔秀英', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '北京 北京市 通州区', 'phone': '13249319674', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213248', 'name': '尹勇', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '山西省 朔州市 朔城区', 'phone': '18644668721', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213261', 'name': '江敏', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '澳门特别行政区 离岛 -', 'phone': '18102134241', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213525', 'name': '韩军', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '香港特别行政区 九龙 黄大仙区', 'phone': '18137107341', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213527', 'name': '秦明', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '云南省 大理白族自治州 南涧彝族自治县', 'phone': '18133444714', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213040', 'name': '孙明', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '福建省 厦门市 翔安区', 'phone': '13911976348', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213731', 'name': '黎艳', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '新疆维吾尔自治区 和田地区 策勒县', 'phone': '18154034353', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213060', 'name': '谭强', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '海南省 三亚市 -', 'phone': '18152430487', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213135', 'name': '黎芳', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '山东省 威海市 环翠区', 'phone': '18184514316', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213984', 'name': '曾芳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '云南省 西双版纳傣族自治州 其它区', 'phone': '19812891587', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213769', 'name': '沈敏', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '江西省 上饶市 婺源县', 'phone': '18165151868', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213446', 'name': '刘芳', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '台湾 金门县 金宁乡', 'phone': '18619407572', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213536', 'name': '罗平', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '浙江省 温州市 鹿城区', 'phone': '18600920376', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213778', 'name': '白勇', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '山西省 晋中市 其它区', 'phone': '13265674526', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213953', 'name': '徐军', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '宁夏回族自治区 吴忠市 同心县', 'phone': '13268640901', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213765', 'name': '赵平', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '陕西省 安康市 石泉县', 'phone': '18694514081', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213951', 'name': '龙霞', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '山东省 泰安市 宁阳县', 'phone': '18627218339', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213934', 'name': '杨勇', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '山东省 济宁市 其它区', 'phone': '18145550707', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213056', 'name': '秦静', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '河南省 焦作市 中站区', 'phone': '18106463579', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213119', 'name': '韩秀英', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '宁夏回族自治区 石嘴山市 其它区', 'phone': '13486172725', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213568', 'name': '吕勇', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '海外 海外 -', 'phone': '18668685365', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213156', 'name': '邓洋', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '西藏自治区 昌都地区 其它区', 'phone': '18192827703', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213888', 'name': '杜芳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '黑龙江省 黑河市 五大连池市', 'phone': '18181414288', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213954', 'name': '孟丽', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '安徽省 蚌埠市 淮上区', 'phone': '18600057640', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213354', 'name': '石秀兰', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '西藏自治区 山南地区 浪卡子县', 'phone': '18155758566', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213545', 'name': '许秀英', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '澳门特别行政区 澳门半岛 -', 'phone': '19814632438', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213036', 'name': '尹平', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '北京 北京市 顺义区', 'phone': '18149786179', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213316', 'name': '余敏', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '内蒙古自治区 乌兰察布市 四子王旗', 'phone': '19886479466', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213174', 'name': '常平', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '江苏省 连云港市 灌南县', 'phone': '19844415472', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213012', 'name': '何明', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '澳门特别行政区 离岛 -', 'phone': '18168772246', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213500', 'name': '戴娜', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '湖南省 株洲市 株洲县', 'phone': '18131871315', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213278', 'name': '常芳', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '山东省 枣庄市 山亭区', 'phone': '18112181349', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213012', 'name': '戴静', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '台湾 云林县 二仑乡', 'phone': '19884373144', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213352', 'name': '韩秀兰', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '香港特别行政区 九龙 黄大仙区', 'phone': '18133039698', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213745', 'name': '郭秀英', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '贵州省 安顺市 镇宁布依族苗族自治县', 'phone': '18188232546', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213900', 'name': '邹秀英', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '黑龙江省 双鸭山市 岭东区', 'phone': '18635275565', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213072', 'name': '许超', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '湖北省 襄阳市 宜城市', 'phone': '18613094171', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213336', 'name': '朱杰', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '安徽省 淮北市 其它区', 'phone': '18155576977', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213526', 'name': '刘超', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '广西壮族自治区 桂林市 荔浦县', 'phone': '13201782798', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213933', 'name': '谢艳', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '辽宁省 铁岭市 其它区', 'phone': '18646887642', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213901', 'name': '廖刚', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '澳门特别行政区 离岛 -', 'phone': '18676362866', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213453', 'name': '梁芳', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '山西省 长治市 郊区', 'phone': '18659897680', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213017', 'name': '朱勇', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '四川省 攀枝花市 盐边县', 'phone': '18117845283', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213781', 'name': '郭勇', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '上海 上海市 徐汇区', 'phone': '18167784826', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213734', 'name': '丁刚', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '新疆维吾尔自治区 阿克苏地区 新和县', 'phone': '18670914157', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213339', 'name': '廖平', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '内蒙古自治区 巴彦淖尔市 乌拉特前旗', 'phone': '13478444130', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213792', 'name': '贺艳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '广西壮族自治区 桂林市 龙胜各族自治县', 'phone': '18188382075', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213877', 'name': '黄军', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '黑龙江省 伊春市 带岭区', 'phone': '19898636707', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213740', 'name': '杨洋', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '台湾 南投县 埔里镇', 'phone': '18675053551', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213045', 'name': '谢洋', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '山东省 泰安市 肥城市', 'phone': '18175124656', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213648', 'name': '董秀兰', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '甘肃省 平凉市 其它区', 'phone': '18175811634', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213924', 'name': '于洋', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '西藏自治区 日喀则地区 吉隆县', 'phone': '18153415381', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213707', 'name': '孟洋', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '江西省 赣州市 寻乌县', 'phone': '18658666882', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213638', 'name': '萧强', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '甘肃省 天水市 其它区', 'phone': '18140256861', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213722', 'name': '陆秀英', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '贵州省 六盘水市 盘县', 'phone': '18103036387', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213229', 'name': '吕敏', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '北京 北京市 东城区', 'phone': '18643655719', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213894', 'name': '万霞', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '吉林省 白城市 镇赉县', 'phone': '18662925146', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213227', 'name': '田娜', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '黑龙江省 双鸭山市 岭东区', 'phone': '19885035726', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213218', 'name': '朱芳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '辽宁省 阜新市 彰武县', 'phone': '18151613578', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213172', 'name': '宋娟', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '陕西省 渭南市 合阳县', 'phone': '18645312813', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213764', 'name': '贾超', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '西藏自治区 林芝地区 墨脱县', 'phone': '13300448243', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213006', 'name': '乔桂英', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '甘肃省 天水市 清水县', 'phone': '18140833202', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213161', 'name': '吕敏', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '福建省 宁德市 福安市', 'phone': '19866748897', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213267', 'name': '林洋', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '甘肃省 天水市 秦州区', 'phone': '18616042481', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213232', 'name': '宋洋', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '香港特别行政区 香港岛 湾仔', 'phone': '18664557822', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213828', 'name': '郭超', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '河北省 承德市 其它区', 'phone': '18117801646', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213392', 'name': '顾秀兰', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '四川省 成都市 郫县', 'phone': '18112416951', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213091', 'name': '武强', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '宁夏回族自治区 石嘴山市 惠农区', 'phone': '18687934751', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213562', 'name': '金秀兰', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '河北省 张家口市 阳原县', 'phone': '18137025977', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213437', 'name': '崔霞', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '河南省 周口市 扶沟县', 'phone': '18170366330', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213594', 'name': '高洋', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '香港特别行政区 新界 荃湾区', 'phone': '18669551764', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213892', 'name': '林明', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '青海省 海南藏族自治州 其它区', 'phone': '13833295412', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213816', 'name': '程芳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '澳门特别行政区 澳门半岛 -', 'phone': '18163553965', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213931', 'name': '任刚', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '广西壮族自治区 河池市 东兰县', 'phone': '18628860036', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213498', 'name': '秦强', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '辽宁省 锦州市 凌海市', 'phone': '19817873120', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213670', 'name': '李娟', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '浙江省 嘉兴市 海盐县', 'phone': '18648331732', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213475', 'name': '蔡磊', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '西藏自治区 日喀则地区 仲巴县', 'phone': '18151337636', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213182', 'name': '魏艳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '澳门特别行政区 澳门半岛 -', 'phone': '19839456055', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213418', 'name': '杨明', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '天津 天津市 和平区', 'phone': '18616805265', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213130', 'name': '谭秀英', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '四川省 眉山市 其它区', 'phone': '13147885025', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213862', 'name': '韩勇', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '辽宁省 锦州市 太和区', 'phone': '18645568032', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213619', 'name': '马静', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '天津 天津市 河西区', 'phone': '13661232123', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213663', 'name': '刘刚', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '江西省 景德镇市 珠山区', 'phone': '18151877383', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213593', 'name': '孔丽', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '上海 上海市 金山区', 'phone': '18171234283', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213660', 'name': '钱芳', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '四川省 资阳市 乐至县', 'phone': '18164646562', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213750', 'name': '徐涛', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '山西省 忻州市 保德县', 'phone': '18652894658', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213534', 'name': '邓明', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '海外 海外 -', 'phone': '13440583748', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213989', 'name': '谢洋', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '陕西省 咸阳市 彬县', 'phone': '13160067508', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213398', 'name': '汪明', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '辽宁省 朝阳市 龙城区', 'phone': '18667525121', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213794', 'name': '郝超', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '内蒙古自治区 阿拉善盟 额济纳旗', 'phone': '18611525132', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213552', 'name': '陈明', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '浙江省 绍兴市 嵊州市', 'phone': '18162462636', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213269', 'name': '顾勇', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '上海 上海市 嘉定区', 'phone': '18663278361', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213393', 'name': '汪刚', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '西藏自治区 那曲地区 嘉黎县', 'phone': '13128360755', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213539', 'name': '孙杰', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '甘肃省 天水市 清水县', 'phone': '19824506057', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213997', 'name': '蒋敏', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '新疆维吾尔自治区 克孜勒苏柯尔克孜自治州 乌恰县', 'phone': '19831271789', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213625', 'name': '尹丽', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '辽宁省 抚顺市 新抚区', 'phone': '18153884606', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213756', 'name': '叶强', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '江苏省 盐城市 射阳县', 'phone': '18616124267', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213054', 'name': '许静', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '浙江省 宁波市 宁海县', 'phone': '18624403053', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213182', 'name': '王涛', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '湖北省 黄冈市 红安县', 'phone': '18669674135', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213163', 'name': '常艳', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '宁夏回族自治区 石嘴山市 惠农区', 'phone': '18637829499', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213114', 'name': '毛明', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '湖北省 十堰市 茅箭区', 'phone': '18145126431', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213628', 'name': '雷明', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '广西壮族自治区 河池市 环江毛南族自治县', 'phone': '19820516346', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213876', 'name': '傅勇', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '西藏自治区 山南地区 加查县', 'phone': '18645168922', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213062', 'name': '林伟', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '四川省 宜宾市 高县', 'phone': '18113723648', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213258', 'name': '许勇', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '福建省 南平市 光泽县', 'phone': '18141514568', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213207', 'name': '姜霞', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '江西省 九江市 都昌县', 'phone': '18173822492', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213110', 'name': '白娟', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '湖南省 郴州市 资兴市', 'phone': '13725387838', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213622', 'name': '锺芳', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '青海省 黄南藏族自治州 河南蒙古族自治县', 'phone': '18168786113', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213534', 'name': '乔杰', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '宁夏回族自治区 固原市 泾源县', 'phone': '18177840895', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213084', 'name': '程霞', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '福建省 泉州市 鲤城区', 'phone': '19803296544', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213779', 'name': '孙霞', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '上海 上海市 青浦区', 'phone': '18621647755', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213110', 'name': '杨刚', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '四川省 泸州市 泸县', 'phone': '18628457961', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213565', 'name': '潘军', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '海外 海外 -', 'phone': '18144047112', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213144', 'name': '邱明', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '福建省 南平市 武夷山市', 'phone': '18189226987', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213409', 'name': '黄杰', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '新疆维吾尔自治区 阿克苏地区 其它区', 'phone': '18193708633', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213074', 'name': '蔡刚', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '吉林省 长春市 双阳区', 'phone': '18606462765', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213622', 'name': '赵霞', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '新疆维吾尔自治区 和田地区 洛浦县', 'phone': '18169106139', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213774', 'name': '林强', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '上海 上海市 闸北区', 'phone': '13682737989', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213071', 'name': '常艳', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '上海 上海市 虹口区', 'phone': '18132402567', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213191', 'name': '郭军', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '浙江省 金华市 浦江县', 'phone': '18161879707', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213955', 'name': '黄秀兰', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '河北省 秦皇岛市 青龙满族自治县', 'phone': '18181374754', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213919', 'name': '夏丽', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '安徽省 蚌埠市 五河县', 'phone': '18621364932', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213826', 'name': '沈静', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '湖北省 鄂州市 其它区', 'phone': '18142102441', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213122', 'name': '顾艳', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '台湾 新北市 三重区', 'phone': '18186321582', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213013', 'name': '雷娟', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '四川省 自贡市 其它区', 'phone': '13780157448', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213112', 'name': '谭静', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '吉林省 延边朝鲜族自治州 和龙市', 'phone': '13801026716', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213121', 'name': '魏芳', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '澳门特别行政区 澳门半岛 -', 'phone': '18111817113', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213794', 'name': '常刚', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '新疆维吾尔自治区 阿克苏地区 库车县', 'phone': '18176055112', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213192', 'name': '贺强', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '澳门特别行政区 澳门半岛 -', 'phone': '18133928473', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213483', 'name': '周秀英', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '湖北省 咸宁市 赤壁市', 'phone': '18678538873', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213110', 'name': '郭霞', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '四川省 资阳市 安岳县', 'phone': '18688352803', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213547', 'name': '邓勇', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '甘肃省 庆阳市 华池县', 'phone': '18116656987', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213767', 'name': '方洋', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '四川省 广安市 邻水县', 'phone': '18167245419', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213902', 'name': '余娟', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '甘肃省 陇南市 两当县', 'phone': '18668858891', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213465', 'name': '傅磊', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '香港特别行政区 九龙 九龙城区', 'phone': '18132484417', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213174', 'name': '胡军', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '宁夏回族自治区 银川市 贺兰县', 'phone': '18616616465', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213947', 'name': '常杰', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '山西省 阳泉市 城区', 'phone': '18146946188', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213787', 'name': '袁勇', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '山东省 莱芜市 钢城区', 'phone': '18132155651', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213786', 'name': '蔡伟', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '安徽省 淮南市 凤台县', 'phone': '18604967133', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213328', 'name': '尹娟', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '重庆 重庆市 沙坪坝区', 'phone': '18124964513', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213312', 'name': '锺磊', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '湖南省 怀化市 溆浦县', 'phone': '18156952514', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213479', 'name': '尹洋', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '香港特别行政区 九龙 油尖旺区', 'phone': '18137711119', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213859', 'name': '陈洋', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '内蒙古自治区 包头市 昆都仑区', 'phone': '18167381534', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213066', 'name': '孟平', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '台湾 基隆市 暖暖区', 'phone': '18656746646', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213725', 'name': '汪洋', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '天津 天津市 河北区', 'phone': '18643378229', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213456', 'name': '戴涛', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '湖南省 湘潭市 韶山市', 'phone': '18143278331', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213086', 'name': '李强', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '重庆 重庆市 万盛区', 'phone': '13447822451', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213255', 'name': '赵平', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '北京 北京市 顺义区', 'phone': '13927542146', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213487', 'name': '胡敏', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '湖南省 岳阳市 临湘市', 'phone': '18185030519', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213336', 'name': '康平', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '吉林省 辽源市 西安区', 'phone': '13265218867', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213944', 'name': '邵桂英', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '香港特别行政区 九龙 油尖旺区', 'phone': '18663371743', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213613', 'name': '汤杰', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '山西省 忻州市 宁武县', 'phone': '18149754321', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213179', 'name': '徐洋', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '青海省 玉树藏族自治州 囊谦县', 'phone': '18177414931', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213460', 'name': '马芳', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '山东省 泰安市 新泰市', 'phone': '13405336585', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213225', 'name': '龚敏', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '贵州省 贵阳市 花溪区', 'phone': '18654384835', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213341', 'name': '郝磊', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '海外 海外 -', 'phone': '18651883463', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213051', 'name': '江勇', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '福建省 莆田市 仙游县', 'phone': '18106826812', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213363', 'name': '郑娟', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '宁夏回族自治区 石嘴山市 平罗县', 'phone': '18172984957', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213724', 'name': '尹敏', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '江苏省 连云港市 连云区', 'phone': '19815601474', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213912', 'name': '蒋丽', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '重庆 重庆市 江北区', 'phone': '19882388302', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213921', 'name': '史伟', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '江苏省 徐州市 丰县', 'phone': '18182688168', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213448', 'name': '罗娜', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '江西省 吉安市 吉水县', 'phone': '18176715877', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213505', 'name': '崔娟', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '辽宁省 营口市 西市区', 'phone': '18165497246', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213328', 'name': '贺伟', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '湖南省 常德市 澧县', 'phone': '18172061668', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213737', 'name': '孙丽', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '青海省 果洛藏族自治州 班玛县', 'phone': '18168725462', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213268', 'name': '乔强', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '甘肃省 甘南藏族自治州 夏河县', 'phone': '18132012747', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213453', 'name': '许秀兰', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '内蒙古自治区 通辽市 库伦旗', 'phone': '13847001496', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213769', 'name': '邱娜', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '宁夏回族自治区 固原市 泾源县', 'phone': '19883294281', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213527', 'name': '乔磊', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '湖北省 荆门市 其它区', 'phone': '18162248782', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213368', 'name': '胡丽', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '广西壮族自治区 梧州市 苍梧县', 'phone': '18628338781', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213855', 'name': '田芳', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '吉林省 白山市 长白朝鲜族自治县', 'phone': '18155393857', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213104', 'name': '丁涛', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '内蒙古自治区 巴彦淖尔市 乌拉特前旗', 'phone': '13115287981', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213399', 'name': '杨娟', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '西藏自治区 昌都地区 丁青县', 'phone': '18126605477', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213190', 'name': '邹强', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '陕西省 汉中市 留坝县', 'phone': '19882234402', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213896', 'name': '毛娜', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '河南省 新乡市 牧野区', 'phone': '18197118375', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213693', 'name': '赖军', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '湖南省 娄底市 新化县', 'phone': '18617639685', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213796', 'name': '孙强', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '香港特别行政区 九龙 油尖旺区', 'phone': '19838575217', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213359', 'name': '阎芳', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '湖北省 襄阳市 谷城县', 'phone': '13512381425', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213833', 'name': '阎明', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '澳门特别行政区 澳门半岛 -', 'phone': '19836313993', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213813', 'name': '马秀英', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '青海省 海东市 互助土族自治县', 'phone': '18163162377', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213863', 'name': '邓娟', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '宁夏回族自治区 石嘴山市 大武口区', 'phone': '13927867827', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213630', 'name': '王军', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '山东省 威海市 其它区', 'phone': '18137248463', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213915', 'name': '吕平', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '上海 上海市 嘉定区', 'phone': '19853224185', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213229', 'name': '董艳', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '西藏自治区 林芝地区 林芝县', 'phone': '18139985344', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213854', 'name': '彭磊', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '吉林省 白山市 临江市', 'phone': '13109569984', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213670', 'name': '朱军', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '浙江省 温州市 其它区', 'phone': '18682626638', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213621', 'name': '顾涛', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '云南省 文山壮族苗族自治州 西畴县', 'phone': '18151447783', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213547', 'name': '龙杰', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '浙江省 台州市 黄岩区', 'phone': '18124234479', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213452', 'name': '文明', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '黑龙江省 绥化市 庆安县', 'phone': '13201243756', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213648', 'name': '武秀兰', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '海南省 三亚市 -', 'phone': '19827328185', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213662', 'name': '彭伟', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '澳门特别行政区 离岛 -', 'phone': '18184243872', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213349', 'name': '雷娟', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '山东省 德州市 武城县', 'phone': '18607582588', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213356', 'name': '乔敏', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '江西省 九江市 修水县', 'phone': '18618482528', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213959', 'name': '秦涛', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '吉林省 通化市 二道江区', 'phone': '13778392534', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213922', 'name': '孟洋', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '青海省 果洛藏族自治州 其它区', 'phone': '18163134004', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213483', 'name': '韩勇', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '江西省 上饶市 婺源县', 'phone': '18111514463', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213018', 'name': '唐杰', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '河南省 南阳市 新野县', 'phone': '18663965288', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213023', 'name': '石杰', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '青海省 黄南藏族自治州 泽库县', 'phone': '18162288651', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213886', 'name': '龙伟', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '山东省 滨州市 无棣县', 'phone': '18125931723', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213913', 'name': '顾娜', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '山西省 长治市 城区', 'phone': '18681474556', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213197', 'name': '梁军', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '广西壮族自治区 百色市 那坡县', 'phone': '18691871624', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213428', 'name': '赖超', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '辽宁省 盘锦市 双台子区', 'phone': '18167485732', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213451', 'name': '江娟', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '新疆维吾尔自治区 和田地区 皮山县', 'phone': '18174318210', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213170', 'name': '于丽', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '新疆维吾尔自治区 昌吉回族自治州 奇台县', 'phone': '18191376731', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213702', 'name': '白强', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '浙江省 杭州市 淳安县', 'phone': '18696793578', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213150', 'name': '秦强', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '四川省 资阳市 简阳市', 'phone': '18614756515', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213865', 'name': '钱强', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '台湾 屏东县 竹田乡', 'phone': '18153012878', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213381', 'name': '邹军', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '四川省 乐山市 井研县', 'phone': '13771332327', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213009', 'name': '秦洋', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '台湾 连江县 东引乡', 'phone': '18175211631', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213269', 'name': '蔡敏', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '吉林省 白山市 临江市', 'phone': '18184253150', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213266', 'name': '钱明', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '陕西省 延安市 延长县', 'phone': '18178327623', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213821', 'name': '段勇', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '青海省 果洛藏族自治州 达日县', 'phone': '13267667364', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213357', 'name': '武涛', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '辽宁省 本溪市 明山区', 'phone': '18636280646', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213119', 'name': '乔敏', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '天津 天津市 西青区', 'phone': '18152075268', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213976', 'name': '廖磊', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '青海省 果洛藏族自治州 玛多县', 'phone': '19838796465', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213461', 'name': '孟强', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '山东省 东营市 垦利县', 'phone': '18115833181', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213599', 'name': '郝秀兰', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '湖南省 永州市 道县', 'phone': '19844542187', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213955', 'name': '邹勇', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '湖北省 孝感市 应城市', 'phone': '18604172342', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213514', 'name': '崔丽', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '四川省 巴中市 通江县', 'phone': '18132645427', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213853', 'name': '姚敏', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '内蒙古自治区 呼伦贝尔市 根河市', 'phone': '19876580546', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213890', 'name': '薛强', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '广东省 湛江市 麻章区', 'phone': '18114734457', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213675', 'name': '阎刚', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '广东省 深圳市 南山区', 'phone': '18195421645', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213727', 'name': '乔静', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '云南省 德宏傣族景颇族自治州 其它区', 'phone': '18144723843', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213904', 'name': '武洋', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '山西省 忻州市 静乐县', 'phone': '18137339021', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213032', 'name': '史刚', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '湖北省 黄冈市 麻城市', 'phone': '13662617420', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213856', 'name': '顾刚', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '贵州省 铜仁市 德江县', 'phone': '18105374884', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213788', 'name': '顾洋', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '河南省 焦作市 济源市', 'phone': '18609155166', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213927', 'name': '邱娟', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '河南省 平顶山市 卫东区', 'phone': '18183594859', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213147', 'name': '汪秀英', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '澳门特别行政区 澳门半岛 -', 'phone': '18129984132', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213748', 'name': '叶秀英', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '北京 北京市 顺义区', 'phone': '18102223016', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213960', 'name': '高霞', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '江苏省 无锡市 江阴市', 'phone': '13998708597', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213798', 'name': '赖强', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '浙江省 金华市 浦江县', 'phone': '18174943751', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213105', 'name': '朱磊', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '重庆 重庆市 巴南区', 'phone': '18613814248', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213573', 'name': '锺洋', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '湖南省 岳阳市 临湘市', 'phone': '18611817258', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213607', 'name': '马敏', 'departments': '计算机科学与技术学院', 'major': '数据科学与大数据技术', 'address': '四川省 攀枝花市 东区', 'phone': '19827662874', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213512', 'name': '罗刚', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '江西省 赣州市 宁都县', 'phone': '18106083687', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213331', 'name': '黎军', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '云南省 玉溪市 元江哈尼族彝族傣族自治县', 'phone': '18135858646', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213649', 'name': '周洋', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '台湾 台北市 内湖区', 'phone': '18141484700', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213669', 'name': '钱平', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '河北省 唐山市 迁西县', 'phone': '18136334559', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213736', 'name': '苏杰', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '辽宁省 阜新市 清河门区', 'phone': '18157273225', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213934', 'name': '蒋秀兰', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '内蒙古自治区 巴彦淖尔市 乌拉特前旗', 'phone': '19884724637', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213718', 'name': '陈芳', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '西藏自治区 阿里地区 普兰县', 'phone': '19848433787', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213092', 'name': '任静', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '台湾 连江县 莒光乡', 'phone': '18146328171', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213352', 'name': '唐明', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '青海省 黄南藏族自治州 尖扎县', 'phone': '18117742589', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213765', 'name': '杨秀英', 'departments': '计算机科学与技术学院', 'major': '计算机科学与技术', 'address': '甘肃省 金昌市 永昌县', 'phone': '18131678343', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213975', 'name': '秦军', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '浙江省 湖州市 安吉县', 'phone': '18181814188', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213478', 'name': '余芳', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '湖北省 恩施土家族苗族自治州 咸丰县', 'phone': '18681641347', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213404', 'name': '罗芳', 'departments': '计算机科学与技术学院', 'major': '信息安全', 'address': '江西省 抚州市 崇仁县', 'phone': '18133849833', 'sex': '女', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    },
    {'studentId': '08213963', 'name': '萧伟', 'departments': '计算机科学与技术学院', 'major': '人工智能', 'address': '贵州省 黔东南苗族侗族自治州 剑河县', 'phone': '18654721352', 'sex': '男', 'avatar': '"https://q1.qlogo.cn/g?b=qq&nk=2365539910&s=100"'
    }
]
sql5="update user set identity='admin' where studentId='02210621';"
sql6="update user set identity='admin' where studentId='08213101';"
conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="hua114514",charset="utf8",db="studentall")
cursor=conn.cursor()

for i in dict:
    try:    
        conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="hua114514",charset="utf8",db="studentall")
        cursor=conn.cursor()
        #print(i)
        id=i.get("studentId")
        name=i.get("name",0)
        departments=i.get("departments",0)
        major=i.get("major",0)
        address=i.get("address",0)
        phone=i.get("phone",0)
        sex=i.get("sex",0)
        avatar=i.get("avatar",0).strip('"')
        sql="INSERT INTO student_view values ('%s','%s','%s','%s','%s','%s','%s','%s');"%(id,name,departments,major,address,phone,sex,avatar)
    #    sql3="""INSERT INTO user ('studentId', 'name') SELECT 'studentId', 'name' FROM student_view;"""
     #   print(i)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        pass



conn=pymysql.connect(host="127.0.0.1", port=3306,user="root",passwd="hua114514",charset="utf8",db="studentall")
cursor=conn.cursor()
sql3="""INSERT INTO user (studentId,name) SELECT studentId,name FROM student_view;"""
cursor.execute(sql3)
cursor.execute(sql5)
cursor.execute(sql6)
conn.commit()
cursor.close()
conn.close()