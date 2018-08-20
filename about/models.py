"""
about.models
~~~~~~~~~~~~

This module implements the models for user profile.
:author: Siva R
"""

from django.db import models

from common.models import User

    
class Profile(models.Model):
    """ Various details of user object. """

    user = models.OneToOneField('common.User', primary_key=True, on_delete=models.CASCADE)
    passout_year = models.DateField(blank=True, null=True)

    current_address = models.TextField(max_length=500, blank=True, null=True)
    permanent_address = models.TextField(max_length=500, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Profiles'
        ordering = ['user']


    @classmethod
    def create(cls, user_id, passout_year, current_address, permanent_address):
        """ 
        Create a new profile instance 
        
        :param user_id: ID of the user object.
        :param passout_year: Year of passing out.
        :param current_address: Address of current residence.
        :param permanent_address: Address of permanent residence.

        :return: Profile instance, error on failure
        :rtype: :profile:
        """

        try:
            user = User.objects.get(id = user_id)

            try:
                profile = Profile(user, passout_year, current_address,
                                  permanent_address)
                profile.save()
                return profile

            except Exception:
                return "Error while creating profile."

        except Exception:
            return "Invalid User ID"

    @classmethod
    def update_permanent_address(cls, user_id, permanent_address):
        try:
            user = User.objects.get(id=user_id)
            try:
                profile = cls.objects.get(user=user)

                try:
                    profile.permanent_address = permanent_adress
                    profile.save()

                except Exception:
                    return "Error while saving new permanent address"

            except Exception:
                return "Error, profile does not exist"

        except Exception:
            return "Invalid User ID"


    @classmethod
    def update_current_address(cls, user_id, current_address):
        try:
            user = User.objects.get(id=user_id)
            try:
                profile = cls.objects.get(user=user)

                try:
                    profile.current_address = current_adress
                    profile.save()

                except Exception:
                    return "Error while saving new current address"

            except Exception:
                return "Error, profile does not exist"

        except Exception:
            return "Invalid User ID"

        
    def get_passout_year(self):
        """ 
        Return the passout year of the user 
        """
        
        return passout_year

    def get_current_address(self):
        """ 
        Return current address of the user 
        """

        return current_address

    def get_permanent_address(self):
        """
        Return permanent address of the user.
        """

        return permanent_address

    def to_dict(self):
        """
        Return dictionary representation of params.
        """

        return {
            'passout_year': self.passout_year,
            'current_address': self.current_address,
            'permanent_address': self.permanent_address
            }
    
class WorkExperience(models.Model):
    """ Schema of Work Experience object """

    profile = models.OneToOneField('Profile', primary_key=True, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    time_period = models.CharField(max_length=50)
    comments = models.TextField(max_length=500)

    @classmethod
    def create(cls, user_id, company, position, time_period, comments):
        """
        Create a new Work Exp instance
        
        :param user_id: The ID of the user.
        :param company: The company working for.
        :param position: The designation held.
        :param time_period: The time frame for which the user worked for.
        :param comments: Review of the company.

        :return: Work Experience instance, error codes on failure.
        :rtype: :WorkExperience:
        """

        try:
            user = User.objects.get(user=user_id)

            try:
                profile = Profile.objects.get(user=user)

                try:
                    work_exp = WorkExperience(profile, company, position,
                                              time_period, comments)
                    work_exp.save()
                    return work_exp

                except Exception:
                    return "Error while creating work experience"

            except Exception:
                return "Profile does not exist"
            
        except Exception:
            return "Invalid User ID"


        def to_dict(self):
            """ 
            Dict representation of params.
            """

            return {
                'company': company,
                'position': position,
                'time_period': time_period,
                'comments': comments
                }
        
class Education(models.Model):
    """ Schema of education object """

    profile = models.OneToOneField('Profile', primary_key=True, on_delete=models.CASCADE)
    institution = models.CharField(max_length=80)

    
    COURSE_CHOICES = (
         ('X', 'Secondary'),
         ('XII', 'Higher Secondary'),
         ('BTech', 'Bachelor of Technology'),
         ('MTech', 'Master of Technology'),
         ('Phd', 'Doctorate'),
        )

    course = models.CharField(max_length=20, choices=COURSE_CHOICES)

    @classmethod
    def create(cls, user_id, institution, course):
        """
        Create an Education instance.

        :param user_id: The ID of the user.
        :param institution: The name of the institution.
        :param course: The course studied.
        
        :return: Education instance on success, error codes on failure.
        :rtype: class :Education:
        """
        
        try:
            user = User.objects.get(id=user_id)

            try:
                profile = Profile.objects.get(user=user)

                try:
                    education = Education(profile, institution, course)
                    education.save()
                    return education

                except Exception:
                    return "Could not create education object"

            except Exception:
                return "Profile does not exist"

        except Exception:
            return "Invalid User ID"

        
class Telegram(models.Model):
    """ Schema of telegram field """

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    handle = models.CharField(max_length=40)
    

    @classmethod
    def create(cls, user_id, institution, course):
        """
        Create an Education instance.

        :param user_id: The ID of the user.
        :param handle: Telegram handle name.
        
        :return: Telegram instance on success, error codes on failure.
        :rtype: class :Telegram:
        """
        
        try:
            user = User.objects.get(id=user_id)

            try:
                profile = Profile.objects.get(user=user)

                try:
                    telegram = telegram(profile, handle)
                    telegram.save()
                    return telegram

                except Exception:
                    return "Could not create education object"

            except Exception:
                return "Profile does not exist"

        except Exception:
            return "Invalid User ID"


    @classmethod
    def update_handle(cls, user_id, handle):
        try:
            user = User.objects.get(id=user_id)

            try:
                profile = Profile.objects.get(user=user)

                try:
                    telegram = Telegram.objects.get(profile=profile)
                    telegram.handle = handle
                    telegram.save()
                    return telegram
                
                except Exception:
                    return "Cannot update handle"

            except Exception:
                return "Error, Profile does not exist"

        except Exception:
            return "Invalid User ID"
        
    def get_handle(self):
        """
        Return telegram handle of user.
        """

        return self.handle

    
    

class Email(models.Model):
    """ Schema of email field """

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    id = models.EmailField(max_length=80, primary_key=True)

    @classmethod
    def create(cls, user_id, email_id):
        """
        Create an Education instance.

        :param user_id: The ID of the user.
        :param email_id: The email address of the user
        
        :return: Email instance on success, error codes on failure.
        :rtype: class :Email:
        """
        
        try:
            user = User.objects.get(id=user_id)

            try:
                profile = Profile.objects.get(user=user)

                try:
                    email = Email(profile, email_id)
                    email.save()
                    return email

                except Exception:
                    return "Could not create email object"

            except Exception:
                return "Profile does not exist"

        except Exception:
            return "Invalid User ID"
    
    @classmethod
    def update_email(cls, user_id, email_id):
        try:
            user = User.objects.get(id=user_id)

            try:
                profile = Profile.objects.get(user=user)

                try:
                    email = Email.objects.get(profile=profile)
                    email.id = email_id
                    telegram.save()
                    return email
                
                except Exception:
                    return "Cannot update email"

            except Exception:
                return "Error, Profile does not exist"

        except Exception:
            return "Invalid User ID"

    def get_email(self):
        """
        Return email address of user.
        """

        return self.id

    
class Phone(models.Model):
    """ Schema of phone field """

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    number = models.CharField(max_length=15)

    @classmethod
    def create(cls, user_id, number):
        """
        Create a Phone instance.

        :param user_id: The ID of the user.
        :param phone: The phone number of the user.
        
        :return: Phone instance on success, error codes on failure.
        :rtype: class :Phone:
        """
        
        try:
            user = User.objects.get(id=user_id)

            try:
                profile = Profile.objects.get(user=user)

                try:
                    phone = Phone(profile, number)
                    phone.save()
                    return phone

                except Exception:
                    return "Could not create phone object"

            except Exception:
                return "Profile does not exist"

        except Exception:
            return "Invalid User ID"

    @classmethod
    def update_number(cls, user_id, number):
        try:
            user = User.objects.get(id=user_id)

            try:
                profile = Profile.objects.get(user=user)

                try:
                    phone = Phone.objects.get(profile=profile)
                    phone.number = number
                    phone.save()
                    return phone
                
                except Exception:
                    return "Cannot update number"

            except Exception:
                return "Error, Profile does not exist"

        except Exception:
            return "Invalid User ID"

    def get_number(self):
        """
        Return phone number
        """
        
        return self.number
