import json
class Emp:
    def _init_(self):
        self.__data=None
    def connect(self,file1):
        with open(file1) as f1:
            self.__data=json.load(f1)
    def retrivedata(self,ename):
        for e in self.__data['emp']:
            if e['name']==ename:
                return e