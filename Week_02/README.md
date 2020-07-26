# 第二周学习笔记  
复习了第一周的题目，完成了第二周所有作业

二叉搜索树（又名有序二叉树），所有操作的时间复杂度都是O（logn），中序遍历（左根右）是升序  
删除操作：找首个大于被删除节点的节点替换上去  


## 堆Heap  
就是总是以时间复杂度O(1)用来找最大值或最小值，（也就是在一堆数里快速的找到最大的数），面试考的是二叉树方法实现的的堆，插入删除时间复杂度为O(logn)，
而工业应用斐波那契的方法实现的比较多而且删除插入操作时间复杂度更加快能达到O(1) 
  
   
 二叉堆定义：完全二叉树+任意节点大于或等于其子节点，不需要链表即左右儿子这样存，用数组就行了，可以用下标关系确定左右儿子  
 插入：先插入到最后一个节点，然后逐步和当前父子节点比较替换，最坏是从子节点一直走到数根，移动的路径为树的深度所以是O(logn)  
 删除堆顶：删除堆顶，把最后一个节点顶上去堆顶位置，然后比较左右子树哪个大就换哪个上来，直到下去到树尾  
 优先队列heap q是二叉堆的一种实现方式  
 
 ## 图  
 面试不常考。  
 图里面用DFS,BFS记得开头加visited = set(),不会重复的访问某个节点  
 DFS，BFS代码模板一定要熟记，遇到相应的题目，先把模板快速写出  
 
 
 ## python编程  
 from collections import Counter  
 collections.Counter(aryy)函数, 返回一个key为arry元素不重复字典，values为重复的次数  
 k = lambda x:x+1, 这是个匿名函数的写法k是函数名，x是输入，x+1是函数的返回值, k(4)将得到5  
sorted(a, key=lambda x:x[0], reverse=True) a是一个set,set的元素是二维，则按照第一个元素从大到小排序  
map(lambda x: x +1, arry), map会根据第一个参数指定的函数，对第二参数作为输入做映射  
from heapq import heappush, heappop
### heapq优先队列最小堆  
h = []  
heappush(h, (5, 'write code'))  
heappush(h, (7, 'release product'))  
print(heappop(h))  # 输出(5, 'write code')  