grsincome=float(input("Enter gross income(in $):"))
deps=int(input("Enter number of dependents:"))
if grsincome<=10000 :
    print("No income tax charged.")
else:
    taxincome=grsincome-10000-(deps*3000)
    Tax=taxincome*0.2
    print("Total taxable income=",taxincome)
    print("Total tax charged=",Tax)
