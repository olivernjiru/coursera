#assignment 4.6
hrs=input("Please enter the number of hours")
rph=input("Please enter your rate per hour")
fhrs=float(hrs),frph=float(rph)
pay=float(fhrs*frph)
def computepay(frph, fhrs):
    if 40>=fhrs:
        print(pay)
    elif fhrs>40:
        overworkpay=(frph*40)+(1.5*(fhrs-40)*(frph))
        print(overworkpay)
p=computepay()
