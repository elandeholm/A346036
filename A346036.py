def swaps(l, start = 0):
  if len(l) == 0:
    return 0

  n = start + 1

  if l[0] != n:
    for i, x in enumerate(l):
      if x == n:
        l[0], l[i] = l[i], l[0]
        return 1 + swaps(l[1:], n)
    else:
      raise
  else:
    return swaps(l[1:], n)

def T(l):
  n = len(l)
  l.reverse()
  l.append(n + 1)
  return l

if __name__ == "__main__":
  l = [ ]

  for n in range(1, 100):
    l = T(l)
    n_swaps = swaps(l[:])

    print("{}, ".format(n_swaps), end="")
