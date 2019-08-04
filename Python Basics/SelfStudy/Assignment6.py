#Patient
class Patient:
    def setId(self,id):
        self.id = id
    def setName(self,name):
        self.name = name
    def setSsn(self,ssn):
        self.ssn = ssn
    def getId(self):
        return(self.id)
    def getName(self):
        return(self.name)
    def getSsn(self):
        return(self.ssn)

p1 = Patient()
p1.setId("01")
p1.setName("Rock")
p1.setSsn(123456)

print("Details of Patients are:\n ID: ", p1.getId(), "\n Name: ", p1.getName(), "\n SSN: ", p1.getSsn())
