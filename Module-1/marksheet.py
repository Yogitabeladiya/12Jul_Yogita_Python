s1=int(input("enter subject1 "))
s2=int(input("enter subject2 "))
s3=int(input("enter subject3 "))
s4=int(input("enter subject4 "))

total=s1+s2+s3+s4
print(total)

pr=total/4
print(pr)

if pr>=70:
    print("Resulr:dist.")

elif pr>=60:
    print("Result:first class")

elif pr>=50:
    print("Result:second class")
    
elif pr>=40:
    print("Result:pass class")
else:
    print("fail")