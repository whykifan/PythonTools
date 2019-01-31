import math
import re

#科学记数法转为为float类型小数,使用正则表达式,re模块
def ConvertELogStrToValue(eLogStr):
    """
    convert string of natural logarithm base of E to value
    return (convertOK, convertedValue)
    eg:
    input:  -1.1694737e-03
    output: -0.001169
    input:  8.9455025e-04
    output: 0.000895
    """
    (convertOK, convertedValue) = (False, 0.0)
    #分组(?P<name>),方便取出匹配内容 -?:正负号1次或0次 \d+匹配数字任意次，\.匹配小数点 re.I忽略大小写
    foundEPower = re.search("(?P<coefficientPart>-?\d+\.\d+)e(?P<ePowerPart>-\d+)", eLogStr, re.I)
    if (foundEPower):
        # 整数部分
        coefficientPart = foundEPower.group("coefficientPart")
        # 小数部分
        ePowerPart = foundEPower.group("ePowerPart")
        #转化为float
        coefficientValue = float(coefficientPart)
        ePowerValue = float(ePowerPart)
        #结果
        wholeOrigValue = coefficientValue * math.pow(10, ePowerValue)
        #将内容替换
        print(wholeOrigValue)
        convertedValue =re.sub("-?\d+\.\d+E-\d+",str(wholeOrigValue),eLogStr)
        # print "wholeOrigValue=",wholeOrigValue;
        convertOK=True
        print(convertedValue)
    else:
        (convertOK, convertedValue) = (False, 0.0)
    return (convertOK, convertedValue)