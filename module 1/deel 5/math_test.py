from math_operations import increment, decrement, add, substract, multiply, divide
from test_lib import test, report

nr1 = 3.0
nr2 = 17.0

expected = nr2 + 1
calculated = increment(nr2)
test('increment', expected, calculated)

expected = nr2 - 1
calculated = decrement(nr2)
test('decrement', expected, calculated)

expected = nr1 + nr2
calculated = (nr1 + nr2)
test('add', expected, calculated)
 
expected = nr2 - nr1
calculated = (nr2 - nr1)
test('substract', expected, calculated)

expected = nr1 * nr2
calculated = (nr1 * nr2)
test('multiply', expected, calculated)
try:
    expected = nr1 / nr2
    calculated = (nr1 / nr2)
    test('divide', expected, calculated)
except:
    expected = None
    calculated = divide(nr1, 0)
    test('divide by zero', expected, calculated)

report()


