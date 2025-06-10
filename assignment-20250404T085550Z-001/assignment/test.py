from email.headerregistry import Address

class Experience:
    count=0
    listBirthDate_exp = []
    listCandidateId_exp = []
    listFirstName_exp = []
    listLastName_exp = []
    listAddress_exp = []
    listPhone_exp = []
    listEmail_exp = []
    listCandidateType_exp = []
    listExpInyear_exp = []
    listProSkill_exp = []
    def __init__(self,FirstName,LastName,BirthDate,Address,Phone,Email,Candidatetype,ExpInYear,ProSkill):
        Experience.count += 1
        self.__candidateId=Experience.count
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__BirthDate = BirthDate
        self.__Address = Address
        self.__Phone = Phone
        self.__Email = Email
        self.__Candidatetype = Candidatetype
        self.__ExpInYear = ExpInYear
        self.__ProSkill = ProSkill

    @property
    def candidateId(self):
        return self.__candidateId

    @candidateId.setter
    def candidateId(self, candidateId):
        self.__candidateId = candidateId

    @property
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self.__FirstName = FirstName

    @property
    def LastName(self):
        return self.__LastName

    @LastName.setter
    def LastName(self, LastName):
        self.__LastName = LastName

    @property
    def BirthDate(self):
        return self.__BirthDate

    @BirthDate.setter
    def BirthDate(self, BirthDate):
        self.__BirthDate = BirthDate

    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, Address):
        self.__Address = Address

    @property
    def Phone(self):
        return self.__Phone

    @Phone.setter
    def Phone(self, Phone):
        self.__Phone = Phone

    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self, Email):
        self.__Email = Email

    @property
    def Candidatetype(self):
        return self.__Candidatetype

    @Candidatetype.setter
    def Candidatetype(self, Candidatetype):
        self.__Candidatetype = Candidatetype

    @property
    def ExpInYear(self):
        return self.__ExpInYear

    @ExpInYear.setter
    def ExpInYear(self, ExpInYear):
        self.__ExpInYear = ExpInYear

    @property
    def ProSkill(self):
        return self.__ProSkill

    @ProSkill.setter
    def ProSkill(self, ProSkill):
        self.__ProSkill = ProSkill
    #---------------------Methods
    #def create_exp_candidate(self):
    def create_expCandidate(self):
        Experience.listFirstName_exp.append(self.__FirstName)
        Experience.listLastName_exp.append(self.__LastName)
        Experience.listBirthDate_exp.append(self.__BirthDate)
        Experience.listAddress_exp.append(self.__Address)
        Experience.listPhone_exp.append(self.__Phone)
        Experience.listEmail_exp.append(self.__Email)
        Experience.listCandidateType_exp.append(self.__Candidatetype)
        Experience.listExpInyear_exp.append(self.__ExpInYear)
        Experience.listProSkill_exp.append(self.__ProSkill)
        print("\a")
        print(Experience.listFirstName_exp,Experience.listLastName_exp,Experience.listEmail_exp)
class Fresher(Experience):
    listBirthDate_fre = []
    listCandidateId_fre = []
    listFirstName_fre = []
    listLastName_fre = []
    listAddress_fre = []
    listPhone_fre = []
    listEmail_fre = []
    listCandidateType_fre = []
    listExpInyear_fre = []
    listProSkill_fre = []
    def __init__(self,candidateId,FirstName,LastName,BirthDate,Address,Phone,
                 Email,Candidatetype,Graduation_date,Graduation_rank,Education):
        self.__Graduation_date = Graduation_date
        self.__Graduation_rank = Graduation_rank
        self.__Education = Education
        super().__init__(candidateId,FirstName,LastName,BirthDate,Address,Phone,
                 Email,Candidatetype)
    def getGraduationDate(self):
        return super().getGraduationDate()+self.__Graduation_date
    def getGraduationRank(self):
        return super().getGraduationRank()+self.__Graduation_rank
    def getEducation(self):
        return super().getEducation()+self.__Education
    def create_freCandidate(self):
        Fresher.listFirstName_fre.append(self.__FirstName)
        Fresher.listLastName_fre.append(self.__LastName)
        Fresher.listBirthDate_fre.append(self.__BirthDate)
        Fresher.listAddress_fre.append(self.__Address)
        Fresher.listPhone_fre.append(self.__Phone)
        Fresher.listEmail_fre.append(self.__Email)
        Fresher.listCandidateType_fre.append(self.__Candidatetype)
        Fresher.listExpInyear_fre.append(self.__ExpInYear)
        Fresher.listProSkill_fre.append(self.__ProSkill)
class Intern(Experience):
    listBirthDate_intern = []
    listCandidateId_intern = []
    listFirstName_intern = []
    listLastName_intern = []
    listAddress_intern = []
    listPhone_intern = []
    listEmail_intern = []
    listCandidateType_intern = []
    listExpInyear_intern = []
    listProSkill_intern = []
    def __init__(self,candidateId,FirstName,LastName,BirthDate,
                 Address,Phone,Email,Candidatetype,Majors, Semester, Universityname):
        self.__Majors = Majors
        self.__Semester = Semester
        self.__Universityname = Universityname
        self.__Candidatetype = Candidatetype
        super().__init__(candidateId, FirstName, LastName, BirthDate, Address, Phone,Email, Candidatetype)
    def create_freCandidate(self):
        Intern.listFirstName_intern.append(self.__FirstName)
        Intern.listLastName_intern.append(self.__LastName)
        Intern.listBirthDate_intern.append(self.__BirthDate)
        Intern.listAddress_intern.append(self.__Address)
        Intern.listPhone_intern.append(self.__Phone)
        Intern.listEmail_intern.append(self.__Email)
        Intern.listCandidateType_intern.append(self.__Candidatetype)
        Intern.listExpInyear_intern.append(self.__ExpInYear)
        Intern.listProSkill_intern.append(self.__ProSkill)
class CandidateManagementSystem:
    listRank=["Excellence","Good","Fair","Poor"]
    def mainScreen(self):
        print("CANDIDATE MANAGEMENT SYSTEM\n\t 1. Experience \n\t 2. Fresher "
              "\n\t 3. Internship \n\t 4. Searching \n\t 5. Exit")
        user=input("Please choose one of the options above: ")
        if user=="1":
            Candidatetype = 0
            print(f"Create a new experience candidate")
            FirstName = input("\tFirst Name: ")
            LastName = input("\tLast Name: ")
            BirthDate = input("\tBirthday: ")
            Phone = input("\tPhone: ")
            Address = input("\tAddress: ")
            Email = input("\tEmail: ")
            YearOfExperience = int(input("\tYear Of Experience: "))
            RankOfGraduation = input("\tRank Of Graduation (Excellence, Good, Fair, Poor): ")
            ProSkill = input("\tProfessional skills: ")
            if len(BirthDate) == 4 and BirthDate.isdigit() == True:
                if len(Phone) >= 10 and Phone.isdigit() == True:
                    if RankOfGraduation in CandidateManagementSystem.listRank:
                        print(BirthDate, Phone)
                        if Email.find('@') != -1:
                            candidate1 = Experience(FirstName, LastName, BirthDate, Address, Phone, Email,
                                                    Candidatetype, YearOfExperience, ProSkill)
                            candidate1.create_expCandidate()
                        else:
                            print("Error! Please check your mail again")
                    else:
                        print("Error! Please check your rank graduation again."
                              "\nThere are only 4 ranks: Excellence, Good, Fair, Poor")
                else:
                    print("Error! Please check your phone number again")
            else:
                print("Error! Please check your birth date again.\nYou only need to type your year of birth")
        elif user=="2":
            print(f"Create a new fresher candidate")
            Candidatetype = 1
            FirstName = input("\tFirst Name: ")
            LastName = input("\tLast Name: ")
            BirthDate = input("\tBirthday: ")
            Phone = input("\tPhone: ")
            Address = input("\tAddress: ")
            Email = input("\tEmail: ")
            GraduationDate = input("Graduation date: ")
            RankOfGraduation = input("\tRank Of Graduation (Excellence, Good, Fair, Poor): ")
            Education = input("Where did you graduate: ")
            if len(BirthDate) == 4 and BirthDate.isdigit() == True:
                if len(Phone) >= 10 and Phone.isdigit() == True:
                    if RankOfGraduation in CandidateManagementSystem.listRank:
                        print(BirthDate, Phone)
                        if Email.find('@') != -1:
                            candidate2 = Fresher(FirstName, LastName, BirthDate, Address, Phone, Email, Candidatetype,
                                                 GraduationDate, RankOfGraduation, Education)
                            candidate2.create_expCandidate()
                        else:
                            print("Error! Please check your mail again")
                    else:
                        print("Error! Please check your rank graduation again."
                              "\nThere are only 4 ranks: Excellence, Good, Fair, Poor")
                else:
                    print("Error! Please check your phone number again")
            else:
                print("Error! Please check your birth date again.\nYou only need to type your year of birth")
        elif user=="3":
            print(f"Create a new intern candidate")
            Candidatetype = 1
            FirstName = input("\tFirst Name: ")
            LastName = input("\tLast Name: ")
            BirthDate = input("\tBirthday: ")
            Phone = input("\tPhone: ")
            Address = input("\tAddress: ")
            Email = input("\tEmail: ")
            Major=input("\tYour major: ")
            Semester=input("\tSemester: ")
            Uniname=input("\tUniversity name: ")
            RankOfGraduation = input("\tRank Of Graduation (Excellence, Good, Fair, Poor): ")
            if len(BirthDate) == 4 and BirthDate.isdigit() == True:
                if len(Phone) >= 10 and Phone.isdigit() == True:
                    if RankOfGraduation in CandidateManagementSystem.listRank:
                        print(BirthDate, Phone)
                        if Email.find('@') != -1:
                            candidate2 = Fresher(FirstName, LastName, BirthDate, Address, Phone, Email, Candidatetype,
                                                 Major,Semester,Uniname)
                            candidate2.create_expCandidate()
                        else:
                            print("Error! Please check your mail again")
                    else:
                        print("Error! Please check your rank graduation again."
                              "\nThere are only 4 ranks: Excellence, Good, Fair, Poor")
                else:
                    print("Error! Please check your phone number again")
            else:
                print("Error! Please check your birth date again.\nYou only need to type your year of birth")

        elif user=="4":
            temp=4
        else:
            exit()
    def check_info(self):
        print(f"Create a new intern candidate")
        Candidatetype = 1
        FirstName = input("\tFirst Name: ")
        LastName = input("\tLast Name: ")
        BirthDate = input("\tBirthday: ")
        Phone = input("\tPhone: ")
        Address = input("\tAddress: ")
        Email = input("\tEmail: ")
        Major = input("\tYour major: ")
        Semester = input("\tSemester: ")
        Uniname = input("\tUniversity name: ")
        RankOfGraduation = input("\tRank Of Graduation (Excellence, Good, Fair, Poor): ")
        if len(BirthDate) == 4 and BirthDate.isdigit() == True:
            if len(Phone) >= 10 and Phone.isdigit() == True:
                if RankOfGraduation in CandidateManagementSystem.listRank:
                    print(BirthDate, Phone)
                    if Email.find('@') != -1:
                        check=True
                    else:
                        print("Error! Please check your mail again")
                else:
                    print("Error! Please check your rank graduation again."
                          "\nThere are only 4 ranks: Excellence, Good, Fair, Poor")
            else:
                print("Error! Please check your phone number again")
        else:
            print("Error! Please check your birth date again.\nYou only need to type your year of birth")
if __name__=="__main__":
    CandidateManagementSystem().mainScreen()