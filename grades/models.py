from django.db import models

class Subject(models.Model):
    subject_key = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

class Student(models.Model):
    student_key = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.CharField(max_length=10, blank=True)

    def save(self, *args, **kwargs):
        if self.grade >= 75:
            self.remarks = "PASS"
        else:
            self.remarks = "FAIL"
        super().save(*args, **kwargs)
