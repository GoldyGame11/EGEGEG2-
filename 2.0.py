class Person:
    name: str
    surname: str
    age: int
    pensione: bool

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.set_pensione(self.age)

    def set_pensione(self, value: int):
        self.pensione = value >= 60

    def info_person(self):
        print(f'Person:\t{self.name} | {self.surname} | {self.age}')


class Teacher(Person):
    subject: str
    hours: int

    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        self.subject = subject
        self.hours = hours
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_teacher(self):
        print(f'Teacher:\t{self.subject} | {self.hours}')

    def info_all(self):
        self.info_person()
        self.info_teacher()


class Student(Person):
    progress: float
    group: str

    def __init__(self, name: str, surname: str, age: int, scholarship: str, progress: float, group: str):
        self.scholarship = scholarship
        self.progress = progress
        self.group = group
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_student(self):
        print(f'Student:\t{self.scholarship} | Progress: {self.progress} | Group: {self.group}')

    def info_all(self):
        self.info_person()
        self.info_student()


class Worker(Person):
    position: str
    duties: str

    def __init__(self, name: str, surname: str, age: int, hourswork: int, position: str, duties: str):
        self.hourswork = hourswork
        self.position = position
        self.duties = duties
        Person.__init__(self, name=name, surname=surname, age=age)

    def info_worker(self):
        print(f'Worker:\tHours Worked: {self.hourswork} | Position: {self.position} | Duties: {self.duties}')

    def info_all(self):
        self.info_person()
        self.info_worker()


student = Student(name='Igor', surname='Ggfad', age=30, scholarship='Hfj', progress=85.5, group='CS-101')
student.info_all()

worker = Worker(name='Igor', surname='Ggfad', age=30, hourswork=1000, position='Engineer', duties='Maintain systems')
worker.info_all()


def atr(cls):
    return [attr for attr in dir(cls) if not callable(getattr(cls, attr))]


def meth(cls):
    return [metoh for metoh in dir(cls) if not callable(getattr(cls, metoh))]

worker_atr = atr(worker)
worker_meth = meth(worker)

student_atr = atr(student)
student_meth = meth(student)

print(f"Student atributes:", student_atr)
print(f"Student metods:", student_meth)
print(f"Worker atributes:", worker_atr)
print(f"Worker metods:", worker_meth)

