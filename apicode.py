from SimpleAPI import students_record

class library:
    def __init__(self,student_record):
        self.student_record = student_record

    def add_copy(self, name, id, dob, place, age):
        student_one = self.student_record.add_details(name, id, dob, place, age)
        return student_one
    
if __name__ == "__main__":
    student_record = students_record()

    a = library(student_record)
    a.add_copy("sri", 1055, 2005, "Krishnagiri" , 55)

    print(student_record.get_details("sri")["age"])
        