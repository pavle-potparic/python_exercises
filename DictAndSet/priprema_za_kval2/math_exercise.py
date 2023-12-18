import math

# math.ceil(x)
result_ceil = math.ceil(4.3) # zaukruzuje broj na veci ili jednaki ceo broj
print(result_ceil)  # Output: 5

# math.comb(n, k)
result_comb = math.comb(5, 2) # binomi
print(result_comb)  # Output: 10

# math.copysign(x, y)
result_copysign = math.copysign(2.5, -1) # menja znakove data dva broja
print(result_copysign)  # Output: -2.5

# math.fabs(x)
result_fabs = math.fabs(-3.14) # isto kao abs() ali radi samo sa float
print(result_fabs)  # Output: 3.14

# math.factorial(n)
result_factorial = math.factorial(5) # mnozenje brojeva od 1 do datog broja
print(result_factorial)  # Output: 120

# math.floor(x)
result_floor = math.floor(4.8) # zaokruzuje broj na manji ili jednaki ceo broj
print(result_floor)  # Output: 4

# math.fmod(x, y)
result_fmod = math.fmod(10, 3) # vraca ostatak pri deljenju dva data broja radi po principu modula i rezultat moze biti negativan (u minusu)
print(result_fmod)  # Output: 1.0

# math.frexp(x)
result_frexp = math.frexp(16.0) # vraca tuple koji ima dva elementa mantis i eksponent
print(result_frexp)  # Output: (0.5, 5)

# math.fsum(iterable)
result_fsum = math.fsum([0.1, 0.2, 0.3]) # precizniji od sum() (smanjenje verovatnoce greske)
print(result_fsum)  # Output: 0.6

# math.gcd(*integers)
result_gcd = math.gcd(36, 48)
print(result_gcd)  # Output: 12

# math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
result_isclose = math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-09) # prema parametrima proverava da li su brojevi "priblizno slicni"
print(result_isclose)  # Output: True

# math.isfinite(x)
result_isfinite = math.isfinite(42)
print(result_isfinite)  # Output: True

# math.isinf(x)
result_isinf = math.isinf(float('inf'))
print(result_isinf)  # Output: True

# math.isnan(x)
result_isnan = math.isnan(float('nan'))
print(result_isnan)  # Output: True

# math.isqrt(n)
result_isqrt = math.isqrt(25)
print(result_isqrt)  # Output: 5

# math.lcm(*integers)
result_lcm = math.lcm(12, 18)
print(result_lcm)  # Output: 36

# math.ldexp(x, i)
result_ldexp = math.ldexp(2.0, 3)
print(result_ldexp)  # Output: 16.0

# math.modf(x)
result_modf = math.modf(3.14)
print(result_modf)  # Output: (0.14000000000000012, 3.0)

# math.nextafter(x, y, steps=1)
result_nextafter = math.nextafter(1.0, math.inf)
print(result_nextafter)  # Output: 1.0000000000000002

# math.perm(n, k=None)
result_perm = math.perm(5, 2)
print(result_perm)  # Output: 20

# math.prod(iterable, *, start=1)
result_prod = math.prod([2, 3, 4])
print(result_prod)  # Output: 24

# math.remainder(x, y)
result_remainder = math.remainder(10, 3)
print(result_remainder)  # Output: 1.0

# math.trunc(x)
result_trunc = math.trunc(4.8)
print(result_trunc)  # Output: 4

# math.ulp(x)
result_ulp = math.ulp(2.0)
print(result_ulp)  # Output: 2.220446049250313e-16
