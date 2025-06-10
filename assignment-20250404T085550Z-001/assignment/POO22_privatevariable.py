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
    def candidateid(self):
        return self.__candidateId

    @candidateid.setter
    def candidateid(self, candidateId):
        self.__candidateId = candidateId

    @property
    def firstname(self):
        return self.__FirstName

    @firstname.setter
    def firstname(self, FirstName):
        self.__FirstName = FirstName

    @property
    def lastname(self):
        return self.__LastName

    @lastname.setter
    def lastname(self, LastName):
        self.__LastName = LastName

    @property
    def birthdate(self):
        return self.__BirthDate

    @birthdate.setter
    def birthdate(self, BirthDate):
        self.__BirthDate = BirthDate

    @property
    def address(self):
        return self.__Address

    @address.setter
    def address(self, Address):
        self.__Address = Address

    @property
    def phone(self):
        return self.__Phone

    @phone.setter
    def phone(self, Phone):
        self.__Phone = Phone

    @property
    def email(self):
        return self.__Email

    @email.setter
    def email(self, Email):
        self.__Email = Email

    @property
    def candidatetype(self):
        return self.__Candidatetype

    @candidatetype.setter
    def candidatetype(self, Candidatetype):
        self.__Candidatetype = Candidatetype

    @property
    def expinyear(self):
        return self.__ExpInYear

    @expinyear.setter
    def expinyear(self, ExpInYear):
        self.__ExpInYear = ExpInYear

    @property
    def proskill(self):
        return self.__ProSkill

    @proskill.setter
    def proskill(self, ProSkill):
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
        system=CandidateManagementSystem()
        system.continueDisplay()
        print(Experience.listFirstName_exp,Experience.listLastName_exp)
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
    count = 0
    def __init__(self,FirstName,LastName,BirthDate,Address,Phone,
                 Email,Candidatetype,Graduation_date,Graduation_rank,Education):
        Fresher.count += 1
        self.__candidateId =Fresher.count
        self.__Graduation_date = Graduation_date
        self.__Graduation_rank = Graduation_rank
        self.__Education = Education
        super().__init__(FirstName,LastName,BirthDate,Address,Phone,
                 Email,Candidatetype,ExpInYear=0,ProSkill=" ")

    @property
    def graduation_date(self):
        return self.__Graduation_date

    @graduation_date.setter
    def graduation_date(self, Graduation_date):
        self.__Graduation_date = Graduation_date

    @property
    def graduation_rank(self):
        return self.__Graduation_rank

    @graduation_rank.setter
    def graduation_rank(self, Graduation_rank):
        self.__Graduation_rank = Graduation_rank

    @property
    def education(self):
        return self.__Education

    @education.setter
    def education(self, Education):
        self.__Education = Education

    def create_freCandidate(self):
        Fresher.listFirstName_fre.append(self.firstname)
        Fresher.listLastName_fre.append(self.lastname)
        Fresher.listBirthDate_fre.append(self.birthdate)
        Fresher.listAddress_fre.append(self.address)
        Fresher.listPhone_fre.append(self.phone)
        Fresher.listEmail_fre.append(self.email)
        Fresher.listCandidateType_fre.append(self.candidatetype)
        Fresher.listExpInyear_fre.append(self.expinyear)
        Fresher.listProSkill_fre.append(self.proskill)
        system = CandidateManagementSystem()
        system.continueDisplay()

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
    count = 0
    def __init__(self,FirstName,LastName,BirthDate,
                 Address,Phone,Email,Candidatetype,Majors, Semester, Universityname):
        Intern.count += 1
        self.__candidateId = Intern.count
        self.__Majors = Majors
        self.__Semester = Semester
        self.__Universityname = Universityname
        self.__Candidatetype = Candidatetype
        super().__init__(FirstName, LastName, BirthDate, Address, Phone,Email, Candidatetype,ExpInYear=0,ProSkill=" ")

    @property
    def major(self):
        return self.__Majors

    @major.setter
    def major(self, Majors):
        self.__Majors = Majors

    @property
    def semester(self):
        return self.__Semester

    @semester.setter
    def semester(self, Semester):
        self.__Semester = Semester

    @property
    def universityname(self):
        return self.__Universityname

    @universityname.setter
    def universityname(self, Universityname):
        self.__Universityname = Universityname

    def create_internCandidate(self):
        Intern.listFirstName_intern.append(self.firstname)
        Intern.listLastName_intern.append(self.lastname)
        Intern.listBirthDate_intern.append(self.birthdate)
        Intern.listAddress_intern.append(self.address)
        Intern.listPhone_intern.append(self.phone)
        Intern.listEmail_intern.append(self.email)
        Intern.listCandidateType_intern.append(self.candidatetype)
        Intern.listExpInyear_intern.append(self.expinyear)
        Intern.listProSkill_intern.append(self.proskill)
        system = CandidateManagementSystem()
        system.continueDisplay()

class CandidateManagementSystem:
    listRank=["Excellence","Good","Fair","Poor"]
    def mainScreen(self):
        print("CANDIDATE MANAGEMENT SYSTEM\n\t 1. Experience \n\t 2. Fresher "
              "\n\t 3. Internship \n\t 4. Searching \n\t 5. Exit")
        user=input("Please choose one of the options above: ")
        if user=="1":
            self.experience_method()
        elif user=="2":
            self.fresher_method()
        elif user=="3":
            self.intern_method()
        elif user=="4":
            self.search_method()
        else:
            exit()
    def experience_method(self):
        Candidatetype = 0
        print(f"CREATE A NEW EXPERIENCE CANDIDATE")
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
                    if Email.find('@') != -1:
                        candidate1 = Experience(FirstName, LastName, BirthDate, Address, Phone, Email,
                                                Candidatetype, YearOfExperience, ProSkill)
                        candidate1.create_expCandidate()
                    else:
                        print("Error! Please check your mail again")
                        system=CandidateManagementSystem()
                        system.mainScreen()
                else:
                    print("Error! Please check your rank graduation again."
                          "\nThere are only 4 ranks: Excellence, Good, Fair, Poor")
                    system=CandidateManagementSystem()
                    system.mainScreen()
            else:
                print("Error! Please check your phone number again")
                system=CandidateManagementSystem()
                system.mainScreen()
        else:
            print("Error! Please check your birth date again.\nYou only need to type your year of birth")
            system=CandidateManagementSystem()
            system.mainScreen()

    def fresher_method(self):

        print(f"CREATE A NEW FRESHER CANDIDATE")
        Candidatetype = 1
        FirstName = input("\tFirst Name: ")
        LastName = input("\tLast Name: ")
        BirthDate = input("\tBirthday: ")
        Phone = input("\tPhone: ")
        Address = input("\tAddress: ")
        Email = input("\tEmail: ")
        GraduationDate = input("\tGraduation date: ")
        RankOfGraduation = input("\tRank Of Graduation (Excellence, Good, Fair, Poor): ")
        Education = input("\tWhere did you graduate: ")
        if len(BirthDate) == 4 and BirthDate.isdigit() == True:
            if len(Phone) >= 10 and Phone.isdigit() == True:
                if RankOfGraduation in CandidateManagementSystem.listRank:
                    if Email.find('@') != -1:
                        candidate2 = Fresher(FirstName, LastName, BirthDate, Address, Phone, Email, Candidatetype,
                                             GraduationDate, RankOfGraduation, Education)
                        candidate2.create_freCandidate()
                    else:
                        print("Error! Please check your mail again")
                        self.mainScreen()
                else:
                    print("Error! Please check your rank graduation again."
                          "\nThere are only 4 ranks: Excellence, Good, Fair, Poor")
                    self.mainScreen()
            else:
                print("Error! Please check your phone number again")
                system = CandidateManagementSystem()
                system.mainScreen()
        else:
            print("Error! Please check your birth date again.\nYou only need to type your year of birth")
            system = CandidateManagementSystem()
            system.mainScreen()
    def intern_method(self):
        print(f"CREATE A NEW INTERN CANDIDATE")
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
                    if Email.find('@') != -1:
                        candidate3 = Intern(FirstName, LastName, BirthDate, Address, Phone, Email, Candidatetype,
                                             Major,Semester,Uniname)
                        candidate3.create_internCandidate()
                    else:
                        print("Error! Please check your mail again")
                        system = CandidateManagementSystem()
                        system.mainScreen()
                else:
                    print("Error! Please check your rank graduation again."
                          "\nThere are only 4 ranks: Excellence, Good, Fair, Poor")
                    system = CandidateManagementSystem()
                    system.mainScreen()
            else:
                print("Error! Please check your phone number again")
                system = CandidateManagementSystem()
                system.mainScreen()
        else:
            print("Error! Please check your birth date again.\nYou only need to type your year of birth")
            system = CandidateManagementSystem()
            system.mainScreen()
    def search_method(self):
        print("-------- SEARCH --------")
        name = input("Enter Candidate First or Last Name to search: ")
        candidate_type = input("Enter Candidate Type (0: Experience, 1: Fresher, 2: Intern): ")

        print("-------- LIST OF CANDIDATES --------")
        print("==================EXPERIENCE CANDIDATE=========================================")
        for i in range(len(Experience.listFirstName_exp)):
            print(f"Name: {Experience.listFirstName_exp[i]} {Experience.listLastName_exp[i]}, ")
        print("==================FRESHER CANDIDATE=========================================")
        for i in range(len(Fresher.listFirstName_fre)):
            print(f"Name: {Fresher.listFirstName_fre[i]} {Fresher.listLastName_fre[i]}, ")
        print("==================INTERN CANDIDATE=========================================")
        for i in range(len(Intern.listFirstName_intern)):
            print(f"Name: {Intern.listFirstName_intern[i]} {Intern.listLastName_intern[i]}, ")

        print("-------- THE CANDIDATE FOUND --------")
        found = False
        if candidate_type == "0":
            for i in range(len(Experience.listFirstName_exp)):
                if name == Experience.listFirstName_exp[i] or name == Experience.listLastName_exp[i]:
                    found = True
                    print(f"Name: {Experience.listFirstName_exp[i]} {Experience.listLastName_exp[i]}"
                          f"|{Experience.listBirthDate_exp[i]}|{Experience.listAddress_exp[i]}"
                          f"|{Experience.listPhone_exp[i]}|{Experience.listEmail_exp[i]}"
                          f"|{candidate_type}")
            system = CandidateManagementSystem()
            system.mainScreen()
        elif candidate_type == "1":
            for i in range(len(Fresher.listFirstName_fre)):
                if name == Fresher.listFirstName_fre[i] or name == Fresher.listLastName_fre[i]:
                    found = True
                    print(f"Name: {Fresher.listFirstName_fre[i]} {Fresher.listLastName_fre[i]}, "
                          f"|{Fresher.listBirthDate_fre[i]}|{Fresher.listAddress_fre[i]}, "
                          f"|{Fresher.listPhone_fre[i]}|{Fresher.listEmail_fre[i]}, "
                          f"|{candidate_type}")
            system = CandidateManagementSystem()
            system.mainScreen()
        elif candidate_type == "2":
            for i in range(len(Intern.listFirstName_intern)):
                if name == Intern.listFirstName_intern[i] or name == Intern.listLastName_intern[i]:
                    found = True
                    print(f"{Intern.listFirstName_intern[i]}|{Intern.listLastName_intern[i]}, "
                          f"|{Intern.listBirthDate_intern[i]}|{Intern.listAddress_intern[i]}, "
                          f"|{Intern.listPhone_intern[i]}|{Intern.listEmail_intern[i]}, "
                          f"|{candidate_type}")
            system = CandidateManagementSystem()
            system.mainScreen()
        else:
            print("Invalid candidate type. Please enter 0, 1, or 2.")
            system = CandidateManagementSystem()
            system.mainScreen()

        if not found:
            print("No matching candidate found.")
            system = CandidateManagementSystem()
            system.mainScreen()
    def continueDisplay(self):
        user=input("Do you want to continue? \n1.Yes \n2.No")
        if user == "1":
            system = CandidateManagementSystem()
            system.mainScreen()

if __name__=="__main__":
    system=CandidateManagementSystem()
    system.mainScreen()
