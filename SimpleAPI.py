class students_record:
    def __init__(self):
        self.details = []

    def add_details(self, name, id, dob, place, age):
        student_one = {
        "name" : name,
        "id" : id,
        "dob" : dob,
        "place" : place,
        "age" : age
        }
        self.details.append(student_one)
        return student_one #even if you comment this line still it shows the output
    
   

    def get_details(self,name):
        for detail in self.details:
            if detail['name'] == name:
                return detail
        return None

if __name__ == "__main__":
    student_record = students_record()

    one = student_record.add_details("Harinika", 1265, "twenty one", "Bangalore", 22 )
    two = student_record.add_details("Harishini", 1064, "Eleven", "Hosur", 18 )
        
    print(student_record.get_details("Harinika")["place"])
        



