from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    department_numeric = models.IntegerField()
    section= models.CharField(max_length=20)
    creation_date=models.DateTimeField(auto_now_add=True)
    updation_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.department_name} - {self.section}"
    


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20)
    creation_date=models.DateTimeField(auto_now_add=True)
    updation_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject_name} - {self.subject_code}"
    

class Student(models.Model):
    GENDER_CHOICES =(
        ('Male','Male'),
        ('Female','Female'),
    )
    
    name = models.CharField(max_length=100)
    roll_id = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    gender= models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob= models.CharField(max_length=100)
    student_department=models.ForeignKey(Department, on_delete=models.SET_NULL,null=True)
    reg_date=models.DateTimeField(auto_now_add=True)
    updation_date=models.DateTimeField(auto_now=True)
    status=models.IntegerField(default=1)


    def __str__(self):
        return self.name
    


class SubjectCombination(models.Model):
    student_department=models.ForeignKey(Department, on_delete=models.SET_NULL,null=True)
    subject=models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True)
    status=models.IntegerField(default=1)
    creation_date=models.DateTimeField(auto_now_add=True)
    updation_date=models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f"{self.student_department} - {self.subject}"
    

class Result(models.Model):
    
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    student_department=models.ForeignKey(Department, on_delete=models.SET_NULL,null=True)
    subject=models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True)
    marks=models.IntegerField()
    status=models.IntegerField(default=1)
    posting_date=models.DateTimeField(auto_now_add=True)
    updation_date=models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f"{self.student} - {self.subject} - {self.marks}"



class Notices(models.Model):
    
    title = models.CharField(max_length=100)
    details = models.TextField()
    posting_date=models.DateTimeField(auto_now_add=True)
    updation_date=models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.title



    