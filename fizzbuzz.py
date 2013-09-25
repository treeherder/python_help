#three one-liners for fizzbuzz
# these are not the best examples, but they will give you a feel for the potential

for x in xrange(100): print x %3 / 2* 'fizz' + x %5 /4 * 'buzz' or x+1
print '\n'.join(['fizz'*(not i%3) + 'buzz'*(not i%5) or str(i) for i in xrange(101)])
[("fizzbuzz" if (x % 15==0) else ("fizz" if x % 3 == 0 else ("buzz" if x % 5 == 0 else str(x)))) for x in xrange(100)]
