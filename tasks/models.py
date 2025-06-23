from django.db import models

class Tasks(models.Model):
    PRIORITY = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    STATUS = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    due_date = models.DateField()
    priority = models.CharField(max_length=30, choices=PRIORITY)
    status = models.CharField(max_length=30, choices=STATUS)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "tasks"
  
