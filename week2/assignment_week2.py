print("----------要求一----------")

# 要求一 ok
from multiprocessing import managers
from unittest import result


def calculate(min, max, step):
    sum = min # 加總值(直接把開頭先放進去)
    i = min # 起始值
    while i<=max:
        i = i + step # 1
        if i > max:
            break 
        sum = sum + i # 0 
    print(sum)        
    

    
    
    
# 請用你的程式補完這個函式的區塊
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

print("----------要求二----------")
#要求二 ok
# 完成以下函式，正確計算出非 manager 的員工平均薪資，
# 所謂非 manager 就是在資料中
# manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，
# 程式需考慮員工資料數量不定的情況。
def avg(data):
    # print(data["employees"][0]["manager"])
    
    employees = data["employees"]
    # length = len(employees)
    # print(length)
    
    n = 0
    sum = 0 # 薪資總和
    num = 0 # 人數

    # while n <= length:     
    #     print(employees[n]["manager"])
    #     n=n+1
    
    for n in employees:
        # print(n["manager"])
        if n["manager"] == True:
            n["salary"] = 0
        elif n["manager"] == False:
            num = num +1
            # print('新增的薪資:',n["salary"])
            
        

        sum = sum + n["salary"]
        # print('薪資總和:',sum)
        # print('不是manager的人數:',num)
    average = sum / num
    print(average) #非manager的平均薪資


# 請用你的程式補完這個函式的區塊
# employees 是一個超大dictionary
# employees 的value裡面，有一個List
# List 的每一個資料都是 dictionary


avg({
    "employees":[
        {
        "name":"John",
        "salary":30000,
        "manager":False
        },
        {
        "name":"Bob",
        "salary":60000,
        "manager":True
        },
        {
        "name":"Jenny",
        "salary":50000,
        "manager":False
        },
        {
        "name":"Tony",
        "salary":40000,
        "manager":False
        }
    ]
}) # 呼叫 avg 函式


print("----------要求三----------")

# 要求三 ok

def func(a):
    def f(b,c):
        answer = a + ( b * c )
        print(answer)

    return f   
# 請用你的程式補完這個函式的區塊
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


print("----------要求四----------")

# 要求四 ok

def maxProduct(nums):
    numlist = []
    for i in nums:
        # print('乘數:',i) #i 乘數
        for j in nums:
            if j != i : #j 被乘數
                n1 = i * j
                # print ('互乘後的值',n1)
                numlist = numlist + [n1]
                # print('值列表:',numlist)
            elif j == i :
                break
    result = max(numlist)
    print(result)
    
# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

print("----------要求五----------")

#要求五ok
def twoSum(nums, target):
    # print(nums)
    # print(target)
    # print(nums.index(11)) 列表名稱.index(資料) 可以搜尋列表某資料的位置
    for n in nums:
        # print('第一個數字:',n)
        answer = target - n
        for m in nums:
            # print('第二個數字:',m)
            if(m == answer):
                # print('符合的n:',n)
                # print('符合的m:',m)
                k = (nums.index(n))
                j = (nums.index(m))
                return [k,j]
            
# your code here
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


print("----------要求六----------")
# 給定只會包含 0 或 1 兩種數字的列表 (Python) 
# 或陣列 (JavaScript)，計算連續出現 0 的最大
# 長度。

def maxZeros(nums):
    # print(nums)
    sum = 0
    list = [0]
    for n in nums:
        if n == 0:
            sum = sum +1
        elif n != 0:
            sum = 0
        
        # print('計算出現0的次數為:',sum)
    
        list = list +[sum]
    # print(list)    
    maxresult = max(list)
    print(maxresult)
# 請用你的程式補完這個函式的區塊
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3