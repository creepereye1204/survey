from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Gamble(models.Model):
    spending_time_on_gambling = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(3)])
    conflict_with_family_or_friends = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(3)])
    difficulty_in_work_or_school = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(3)])
    financial_problems_due_to_gambling = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(3)])
    feel_anxious_when_not_gambling = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(3)])
    gamble_to_recover_lost_money = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(3)])
    health_issues_from_gambling = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(3)])
    legal_issues_due_to_gambling = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(3)])
    difficulty_in_relationships = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(3)])
    result = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(3)])

    def __str__(self):
        return str(self.pk)
