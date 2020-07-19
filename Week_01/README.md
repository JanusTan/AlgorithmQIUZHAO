#本周学习笔记

坚持刷题的目的是，在秋招能够顺顺利利、在规定时间内、以最好的时空复杂度AC每一道面试的代码题。让自己在竞争者中脱颖而出，拿到大厂offers
很高兴自己能够找到这样一个组织，大家互相鼓励帮助，不会那么孤独，还有比自己优秀的大佬给自己传授经验少走了很多弯路，毕竟大厂秋招下个月就开始了
这是正式开始练习算法题的第一周。

1. 本周完成了所有的预习题、实战题、作业题，并分析时间复杂度和和空间复杂度，对比国内外网站的most votes, 修改自己的代码，并收藏到该周目录下
2. 还有做完的题会在24小时后，4天后，亲自在空白脚本文件重写和通过LeetCode测试

听课笔记：
做题误区： 一个题目只做一遍是最大的误区。应该至少五遍，而这五遍出现的时间应该符合自己的记忆曲线（24小时，4天，7天，14天）
面试写代码四步骤：①和面试官讨论，确认一下不了解、不确定的概念，确保自己是理解面试官的意思
               ②提出可能的解决方案，一般从暴力解法出发，然后是想时间复杂度和空间复杂度更优的解法，如hashmap的运用
               ③ Coding
               ④ Testing
               
##课后做题中遇到的一些常用的数据结构和函数：
1. 栈: 栈顶stack[-1]
2. 队列: 
栈和队列都可以用container的库
from collections import deque
deque1 = deque('abc') # 创建deque(['a', 'b', 'c'])
deque1.append('r') # 尾插入
deque1.appendleft(1) # 头插入
deque1.pop() # 尾弹出
deque1.popleft()) # 头弹出
其他常用的函数:
deque1.index('c') # 查c的位置
deque1.insert(3,'g') # 三号下标里插入g
注： list除没有popleft, appendleft外，上述函数append, pop, index, insert均有
优先队列，我用heapq写在了heapq.py


3. hashmap: 
dic = {} # 创建一个字典dic{'key1': 'value1', 'key2': 'value2'}
dic[key1] += 1 # key1对应的value1加一操作
dic[key2] = 1 # 给key2对应的value2赋值value1
dic.values() # 字典里所有的values
if key3 in dic: # 查找key3在不在这个字典里
if value1 in dic.values(): # 查找value1在不在这个字典里



4. sorted(array) # 从小到大排序 sorted(a,reverse=True)是从大到小，sorted('dcab')会得到['a', 'b', 'c', 'd'], 时间复杂度O（nlogn）

##一些题的固定解法总结：
括号类： 栈               
               