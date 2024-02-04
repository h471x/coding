memo = {} #an array to stored already computed values

def min_ignore(a, b):
  if a is None:
    return b
  if b is None:
   return a
  return min(a, b)

def min_coin(m, coins):
  if m in memo:
    return memo[m]

  if m == 0:
    ans = 0
  else:
    ans = None
    for coin in coins:
      sub = m - coin
      if sub < 0:
        continue
      ans = min_ignore(ans, min_coin(sub, coins) + 1)
  memo[m] = ans
  return ans
print(min_coin(13, [1,4,5]))
