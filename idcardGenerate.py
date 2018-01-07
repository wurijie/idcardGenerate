#--*-- encoding: UTF-8 --*--
import random
import time

#类定义
class idcardGenerate():
    areaCodes = []

    #初始化，获取区域信息
    def __init__(self):
        with open("code.txt", 'r') as fd:
            self.areaCodes = fd.read().split("\n")

    #随机获取区域代码
    def getAreaCode(self):
        rand = random.randint(0, len(self.areaCodes) - 1)

        return self.areaCodes[rand]

    #随机获取年份，从当前年份的上一年开始，往前包含80年
    def getYear(self):
        yearNow = int(time.strftime("%Y", time.localtime()))
        yearEnd = yearNow - 1
        yearStart = yearNow - 81

        year = random.randint(yearStart, yearEnd)

        return str(year)

    #随机获取月份
    def getMonth(self):
        month = random.randint(1, 12)

        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)

        return month

    #随机获取日,根据输入的年份与月份判断当月能随机的最大天数
    def getDay(self, year, month):
        year = int(year)
        month = int(month)

        #判断是否闰年，得到每个月的天数
        if ((not year%4) and year%100) or (not year%400):
            monthDayArr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            monthDayArr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        #根据传入的月份，得到当月最大天数，并随机天数
        days = monthDayArr[month - 1]
        day = random.randint(1, days)
        if day < 10:
            day = '0' + str(day)

        return str(day)

    #随机获取顺序码
    def getSquence(self):
        squence = str(random.randint(1, 999))

        if int(squence) < 10:
            squence = '00' + squence
        elif int(squence) < 100:
            squence = '0' + squence

        return squence

    #生成最后一位校验位
    def generalCheck(self, randStr):
        yinshu = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
        checkNum = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]

        sum = 0
        for i in range(len(randStr)):
            sum += int(randStr[i]) * yinshu[i]

        modNum = sum%11

        return str(checkNum[modNum])

    #校验身份证号码是否合法
    def checkId(self):


        return True


#主程序开始
idcard = idcardGenerate()

#获取随机的年月日
areaCode = idcard.getAreaCode()
year = idcard.getYear()
month = idcard.getMonth()
day = idcard.getDay(year, month)

# 获取随机的顺序号
sequence = idcard.getSquence()

#拼装随机的数据，并得到校验位
randStr = areaCode + year + month + day + sequence
checkCode = idcard.generalCheck(randStr)

#生成最终长度的身份证号码
idnum = randStr + checkCode

print("随机生成的身份证号码：" + idnum)