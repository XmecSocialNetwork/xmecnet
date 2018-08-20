"""
common.models
~~~~~~~~~~~~~

This module implements the models for user authentication.
:author: Siva R, Jeswin Cyriac
"""

from django.db import models
from django.contrib.auth.hashers import make_password, check_password

import datetime


class User(models.Model):
    """ Schema of user object. """
    
    email = models.EmailField(max_length=100, primary_key=True, db_index=True)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()

    BRANCH_CHOICES = (
            ('CS', 'Computer Science and Engineering'),
            ('BME', 'Biomedical Engineering'),
            ('EC', 'Electronics & Communication Engineering'),
            ('EEE', 'Electrical Engineering'),
        )

    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES,
                              blank=True, null=True)
    profilepic = models.FileField(default="", blank=True, null=True)

    def __str__(self):
        """ Generate an string representation of the object. """
        
        return '<{0} {1}>'.format(self.name, self.email)

    class Meta:
        """ Extra options for class User. """
        
        verbose_name_plural = 'Users'
        ordering = ['name']


    @classmethod
    def create(cls, email, name, password, dobday, dobmonth, dobyear, branch, roll_no=None):
        """ Create a user object.

        :param email: Email of the user.
        :param name: Name of the user.
        :param password: Password set by the user.
        :param dobday: Day of birth.
        :param dobmonth: Month of birth
        :param dobyear: Year of birth
        :param branch: Branch opted by the user (CS, EC, EEE, BME)
        :param roll_no: (default=None) optional field, specifying the roll no
                        of the user during his undergraduation.
        :return: An instance of User, or Error on failure.
        :rtype: class :User:
        """
        
        try:
            dob = self.generate_date(dobday, dobmonth, dobyear)

            user = cls(email=email,
                       name=name,
                       password=make_password(password),
                       roll_no=roll_no,
                       date_of_birth=dob,
                       branch=branch
            )
            
            user.save()

            return user

        except Exception as e:
            raise Exception("Error while creating user")

    @classmethod
    def login(cls, email, password):
        """ Authenticates the user.

        :param email: Email of the user.
        :param password: Password set by the user.

        :return: User object on successful login, false otherwise.
        :rtype: class :User:
        """
        
        try:
            user = cls.objects.get(email=email)

            if check_password(password, user.password):
                return user
            else:
                return False

        except Exception as e:
            raise Exception("Error while login")

    def generate_date(self, day, month, year):
        """ Return date object from string.
        
        :param day: Day of the date.
        :param month: Month of the date.
        :param year: Year of the date.

        :return: An instance of type date.
        :rtype: class :Date:
        """
        
        return datetime.date(year=year, month=month, day=day)
    
