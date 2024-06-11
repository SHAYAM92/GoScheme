from django.db import models

class EduEligibility(models.Model):
    SSLC = 'SSLC'
    HSC = 'HSC'
    DIPLOMA = 'DIPLOMA'
    PROFESSIONAL = 'PROFESSIONAL'
    ARTS = 'ARTS'
    PG = 'P.G'
    PHD = 'PH.D'
    
    EDUCATION_CHOICES = [
        (SSLC, 'SSLC'),
        (HSC, 'HSC'),
        (DIPLOMA, 'Diploma'),
        (PROFESSIONAL, 'Professional'),
        (ARTS, 'ARTS'),
        (PG, 'P.G'),
        (PHD, 'Ph.D'),
    ]
    
    choice = models.CharField(
        max_length=20,
        choices=EDUCATION_CHOICES,
        
    )
    
    def __str__(self):
        return self.choice

class CasteEligibility(models.Model):
    ALL='ALL_CASTE'
    MBC = 'MBC'
    BC = 'BC'
    OC = 'OC'
    SC = 'SC'
    ST = 'ST'
    
    CASTE_CHOICES = [
        (ALL,'ALL_CASTE'),
        (MBC, 'MBC'),
        (BC, 'BC'),
        (OC, 'OC'),
        (SC, 'SC'),
        (ST, 'ST'),
    ]
    
    choice = models.CharField(
        max_length=20,
        choices=CASTE_CHOICES,
        unique=True
    )
    
    def __str__(self):
        return self.choice

class Scheme(models.Model):
    BOTH = 'BOTH'
    FEMALE = 'FEMALE'
    MALE = 'MALE'
    
    
    GENDER_CHOICES = [
        (BOTH, 'BOTH'),
        (FEMALE, 'FEMALE'),
        (MALE, 'MALE'),
        
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        
    )
    start_date = models.DateField()
    end_date = models.DateField()
    link = models.URLField()
    procedure_to_apply = models.TextField()
    edu_eligibility = models.ForeignKey(EduEligibility, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    

class SchemeCasteMapping(models.Model):
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)
    caste = models.ForeignKey(CasteEligibility, on_delete=models.CASCADE)
    min_age = models.IntegerField()
    max_age = models.IntegerField()

    class Meta:
        unique_together = ('scheme', 'caste')

    def __str__(self):
        return f"{self.scheme.name} - {self.caste.choice}"
    
  