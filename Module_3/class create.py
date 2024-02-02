class student:
    stid=12
    stnm='yogi'

    def getdata(self):
        print("This is student class ")

    def getsum(self,a,b):
        print("Sum:",a+b)

st=student()
print("Id",st.stid)
print("Name",st.stnm)
st.getdata()
st.getsum(12,23)



