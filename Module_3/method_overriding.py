'''class student :
    def getdata(self,id,name):
        print("Id",id)
        print("Name",name)

class ostudent(student):
    def getdata(self, id, name):
        return super().getdata(id, name)
    
st=student()
st.getdata(1,'yy')
ot=ostudent()
ot.getdata(2,'bb')'''


class student:
    def getdata(self,id,name):
        print("id",id)
        print("name",name)
class osstudent(student):
    def getdata(self, id, name):
        return super().getdata(id, name)
os=student()
os.getdata(2,'rinku')  
st=osstudent()
st.getdata(1,'yy')
    


