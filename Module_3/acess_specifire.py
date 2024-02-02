class student:
    __id=12
    __name='yogita'

    def __getdata(self):
        print("This is getdata.")

        print("ID:",self.__id)
        print("Name",self.__name)
     
    def printdata(self):
        self.__getdata()


s=student()
#print(st.id)
#print(st.name)
s.printdata()

