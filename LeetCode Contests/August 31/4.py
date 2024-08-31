def minDamage(power, damage, health):

    res = 0

    while health:
        md = max(damage)
        ind = damage.index(md)
        
        mul = health[ind] // power

        if health[ind] % power != 0:
            mul += 1


        res += mul * sum(damage)
        health.pop(ind)
        damage.pop(ind)

    return res

power = 62
damage = [80,79]
health = [86,13] # 319
print(minDamage(power, damage, health))
