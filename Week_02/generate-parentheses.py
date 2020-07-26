# 22. 括号生成
# 时间复杂度O(n),递归树的深度，空间复杂度O(n),开了一个数组


def generate_valid_parentheses(n):
    left = 0
    right = 0
    result = []
    s = ""

    def generate_parentheses(left, right, s, result):
        # terminator
        if left + right >= 2 * n:
            result.append(s)
            return
            # level

        # drill down
        if left < n:
            generate_parentheses(left+1,right, s + "(", result)
        if right < left:
            generate_parentheses(left,right+1, s + ")", result)
        # reserve current level

    generate_parentheses(left,right, s, result)
    return result


result = generate_valid_parentheses(1)
print(result)
