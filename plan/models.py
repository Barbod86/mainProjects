from django.db import models
from django.contrib.auth.models import User

day_status = (
        (1, ("Saturday")),
        (2, ("Sunday")),
        (3, ("Monday")),
        (4, ("Tuesday")),
        (5, ("Wednesday")),
        (6, ("Thursday")),
        (7, ("Friday"))
    )
workout_status = (
    ('arm day', ("Arm")),
    ('shoulder day', ("Shoulser")),
    ('back day', ("Back")),
    ('chest day', ("Chest")),
    ('leg day', ("Leg"))
)


class WorkoutPlans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=40, blank=True)
    arm_day = models.TextField(max_length=1000, blank=True)
    shoulder_day = models.TextField(max_length=1000, blank=True)
    back_day = models.TextField(max_length=1000, blank=True)
    chest_day = models.TextField(max_length=1000, blank=True)
    leg_day = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title



