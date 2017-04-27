from django.db import models

DEPLOYMENT = (
    ('Production', 'Production'),
    ('Development', 'Development'),
    ('Archived', 'Archived'),
)
SENSITIVEDATA = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

INFRASTRUCTURE = (
    ('RVMI', 'Research VM Infra'),
    ('BS', 'Business VM Infra')
)

# Create your models here.
class Virtual_Machine(models.Model):
    Name = models.CharField(blank=True,null=True, max_length=200)
    Infra = models.CharField(max_length=20, choices=INFRASTRUCTURE)
    Deployment = models.CharField(max_length=20, choices=DEPLOYMENT)
    Function = models.CharField(blank=True,null=True, max_length=200)
    Business_Owner = models.CharField(blank=True,null=True, max_length=200)
    Email = models.EmailField(blank=True,null=True, max_length=200)
    Faculty = models.CharField(blank=True,null=True, max_length=200)
    Contribution = models.CharField(blank=True,null=True, max_length=200)
    Nominated_Admins = models.CharField(blank=True,null=True, max_length=200)
    Isilon = models.CharField(blank=True,null=True, max_length=200)
    Sensitive_Data = models.CharField(max_length=20, choices=SENSITIVEDATA)
    Type = models.CharField(blank=True,null=True, max_length=200)
    OS = models.CharField(blank=True,null=True, max_length=200)
    CPUcores = models.CharField(blank=True,null=True, max_length=200)
    Memory = models.CharField(blank=True,null=True, max_length=200)
    HDD = models.CharField(blank=True,null=True, max_length=200)
    DNS = models.URLField(blank=True,null=True, max_length=200)
    IP_Address = models.GenericIPAddressField(blank=True,null=True)
    Sysadmin1 = models.CharField(blank=True,null=True, max_length=200)
    Sysadmin2 = models.CharField(blank=True,null=True, max_length=200)
    Reference = models.CharField(blank=True,null=True, max_length=200)
    Notes = models.TextField(blank=True,null=True)
    Test = models.CharField(max_length=3, choices=SENSITIVEDATA)

    def __str__(self):
        return self.Name