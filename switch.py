from yard import Yard

y = Yard(((1,2),(1,3)), (['a','*','b'],['c','d'],None))

print y.containsEngine(1)
print y.containsEngine(2)

print y.left(2,1)
print y.right(1,2)
