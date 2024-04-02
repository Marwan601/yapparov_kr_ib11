sol = input()
ky = input()
sin = input()
solx = set(sol.split())
kyx = set(ky.split())
sinx = set(sin.split())
dizz = kyx | sinx
aria = solx - dizz
print(" - ".join(aria))
print(sum(map(int,aria)) / len(aria))
