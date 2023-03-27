#https://leetcode.com/contest/biweekly-contest-100/problems/distribute-money-to-maximum-children/

def distribute_money(money, children):
    total_money = money
    children_money = []

    for i in range(money):
        if sum(children_money) < money:
            children_money.append(8)
        if sum(children_money) > money:
            children_money.pop()
    
    if sum(children_money) != money:
        children_money.append(1)
        
    #to fill in the last element
    for i in range(money):
        if sum(children_money) != money:
            children_money[-1] = children_money[-1] + 1
    
    #check for number 4
    if 4 in children_money:
        children_money[-1] = children_money[-1] - 1
        children_money[-2] = children_money[-2] + 1
            
            
    print(children_money)
    
    freq_of_8 = children_money.count(8)
    print(freq_of_8)
