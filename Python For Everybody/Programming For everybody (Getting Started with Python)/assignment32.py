hrs = input("Enter Hours:")
rph = input("Enter Rate per Hour:")
try:
    frph = float(rph)
    fhrs = float(hrs)
except:
    print("Please enter numeric input")
    quit()
print("Number of hours:", frph, "Rate per Hour:", fhrs)
pay=(fhrs*frph)
if 40>=fhrs:
    print("Pay is:", pay)
elif fhrs>40:
    overworkpay=(frph*40)+(1.5*(fhrs-40)*(frph))
    print("Pay is:", overworkpay)