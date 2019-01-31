import math
import re

#��ѧ������תΪΪfloat����С��,ʹ��������ʽ,reģ��
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
    #����(?P<name>),����ȡ��ƥ������ -?:������1�λ�0�� \d+ƥ����������Σ�\.ƥ��С���� re.I���Դ�Сд
    foundEPower = re.search("(?P<coefficientPart>-?\d+\.\d+)e(?P<ePowerPart>-\d+)", eLogStr, re.I)
    if (foundEPower):
        # ��������
        coefficientPart = foundEPower.group("coefficientPart")
        # С������
        ePowerPart = foundEPower.group("ePowerPart")
        #ת��Ϊfloat
        coefficientValue = float(coefficientPart)
        ePowerValue = float(ePowerPart)
        #���
        wholeOrigValue = coefficientValue * math.pow(10, ePowerValue)
        #�������滻
        print(wholeOrigValue)
        convertedValue =re.sub("-?\d+\.\d+E-\d+",str(wholeOrigValue),eLogStr)
        # print "wholeOrigValue=",wholeOrigValue;
        convertOK=True
        print(convertedValue)
    else:
        (convertOK, convertedValue) = (False, 0.0)
    return (convertOK, convertedValue)