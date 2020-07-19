# 66. 加一


def plusOne(digits):
    # 倒序遍历整个数组，如果遇到不是9就直接返回最后一位加一的
    # 否则遇到9，就先把该位改成0，在判断最高位是否变成0了，是的话就得最高位前添加1
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            if digits[0] == 0:
                digits.insert(0, 1)
                return digits


a = [9, 9, 9, 9]
print(plusOne(a))
