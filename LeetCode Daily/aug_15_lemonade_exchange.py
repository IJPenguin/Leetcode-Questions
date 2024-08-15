bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]

def lemonadeChange(bills) -> bool:
        cur = []
        for bill in bills:
            print(cur)
            print(bill)
            print("----------------")
            if bill == 5:
                cur.append(5)
            elif bill == 10:
                if 5 in cur:
                    cur.remove(5)
                    cur.append(10)
                else:
                    return False
            elif bill == 20:
                if 10 in cur and 5 in cur:
                    cur.remove(10)
                    cur.remove(5)
                    cur.append(20)
                elif sum(cur) >= 15:
                    cur.remove(5)
                    cur.remove(5)
                    cur.remove(5)
                    cur.append(20)
                else:
                    return False
        return True

print(lemonadeChange(bills))