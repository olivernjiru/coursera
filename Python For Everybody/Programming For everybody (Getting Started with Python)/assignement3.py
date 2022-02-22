hrs = input("Enter Hours:")
fhrs = float(hrs)
rph = input("Enter Rate per Hour:")
frph = float(rph)
pay=float(fhrs*frph)
if 40>=fhrs:
    print(pay)
elif fhrs>40:
    overworkpay=(frph*40)+(1.5*(fhrs-40)*(frph))
    print(overworkpay)