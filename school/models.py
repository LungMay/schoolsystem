from django.db import models
from sre_constants import CATEGORY

class ExamScore(models.Model):

    allsubject = (('math', 'ຄະນິດສາດ'),
                  ('sci', 'ວິທະຍາສາດ'),
                  ('art', 'ສີລະປະ'),
                  ('eng', 'ພາສາອັງກິດ'),
                  ('physics', 'ຟີຊິກ'),
                  ('bio', 'ຊີວະສາດ'))

    subject = models.CharField(max_length=200, choices=allsubject, default='math')
    student_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

def __str__(self):
    return self.student_name +'-'+ self.subject
