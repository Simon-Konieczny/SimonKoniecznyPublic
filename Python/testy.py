def sum_factors(n):
    ans = 0
    ans_set = set()
    for i in range(1,int(n/2+1)):
        if n%i == 0:
            if i not in ans_set and (n/i) not in ans_set:
                if (i == (n/i)):
                    ans_set.add(i)
                    ans += i
                elif (n/i != n):
                    ans_set.add(i)
                    ans_set.add((n/i))
                    ans += i+(n/i)
                else:
                    ans_set.add(i)
                    ans += i
    
    return ans

def deficients(n):
    counter = 0
    for i in range(1,n):
        if (sum_factors(i)<i):
            counter+=1
    return counter

def excessives(n):
    counter = 0
    for i in range (1,n):
        if (sum_factors(i)>i):
            counter +=1
    return counter