def solve(numheads, numlegs):
   rabbits = (numlegs - 2 * numheads) / 2
   chickens = numheads - rabbits
   print(rabbits, chickens)
solve(35, 94)