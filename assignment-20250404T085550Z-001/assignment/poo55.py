class Doctor:
    def __init__(self, Code, Name, Specialization, Availability):
        self.__code = Code
        self.__name = Name
        self.__specialization = Specialization
        self.__availability = Availability
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, Code):
        self.__code = Code

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, Name):
        self.__name = Name
    @property
    def specialization(self):
        return self.__specialization
    @specialization.setter
    def specialization(self, Specialization):
        self.__specialization = Specialization
    @property
    def availability(self):
        return self.__availability
    @availability.setter
    def availability(self, Availability):
        self.__availability = Availability
    @
    def update_info(self, name=None, specialization=None, availability=None):
        if name:
            self.name = name
        if specialization:
            self.specialization = specialization
        if availability is not None and availability >= 0:
            self.availability = availability

    def display_info(self):
        return f"Code: {self.__code}, Name: {self.__name}, Specialization: {self.__specialization}, Availability: {self.__availability}"


class DoctorManagement:
    def __init__(self):
        self.doctors = {}

    def add_doctor(self, code, name, specialization, availability):
        if code in self.doctors:
            print("Doctor code already exists.")
            return
        self.doctors[code] = Doctor(code, name, specialization, availability)
        print("Doctor added successfully.")

    def update_doctor(self, code):
        if code not in self.doctors:
            print("Doctor code does not exist.")
            return
        doctor = self.doctors[code]
        name = input(f"Enter new name ({doctor.name}): ") or doctor.name
        specialization = input(f"Enter new specialization ({doctor.specialization}): ") or doctor.specialization
        availability = input(f"Enter new availability ({doctor.availability}): ")
        doctor.update_info(name, specialization, int(availability) if availability else doctor.availability)
        print("Doctor updated successfully.")

    def delete_doctor(self, code):
        if code in self.doctors:
            del self.doctors[code]
            print("Doctor deleted successfully.")
        else:
            print("Doctor code does not exist.")

    def search_doctor(self, search_string):
        search_string = search_string.lower()
        found_doctors = [doctor.display_info() for doctor in self.doctors.values() if search_string in doctor.name.lower() or search_string in doctor.specialization.lower()]
        if found_doctors:
            print("\n".join(found_doctors))
        else:
            print("No doctors found.")

    def display_menu(self):
        while True:
            print("\nWELCOME TO DOCTOR MANAGEMENT SYSTEM")
            print("1. Add Doctor")
            print("2. Update Doctor")
            print("3. Delete Doctor")
            print("4. Search Doctor")
            print("5. Exit")
            choice = input("Your choice: ")

            if choice == "1":
                code = input("Enter doctor code: ")
                name = input("Enter doctor name: ")
                if name.isalnum()==True:
                    print("Error! retype the correct name.")
                    continue
                specialization = input("Enter specialization: ")
                if specialization.isalnum()==True:
                    print("Error! retype the correct specialization.")
                    continue
                availability = int(input("Enter availability: "))
                if availability
                self.add_doctor(code, name, specialization, availability)
            elif choice == "2":
                code = input("Enter doctor code to update: ")
                self.update_doctor(code)
            elif choice == "3":
                code = input("Enter doctor code to delete: ")
                self.delete_doctor(code)
            elif choice == "4":
                search_string = input("Enter search term: ")
                self.search_doctor(search_string)
            elif choice == "5":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = DoctorManagement()
    manager.display_menu()