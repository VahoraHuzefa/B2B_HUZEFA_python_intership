P=float(input("enter principal amount(P): "))
R=float(input("enter Rate of Interest(R): "))
T=float(input("enter Time period(T): "))
SI=(P*R*T)/100
print(SI)
CI=P*(1+R/100)**T-P
print(CI)
print("Simple Interest =", int(SI), int(CI))
