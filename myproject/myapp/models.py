from django.db import models

class NamespaceStatus(models.Model):
    NF_TYPE_CHOICES = [
        ('policy', 'Policy'),
        ('bsf', 'BSF'),
    ]

    PRIORITY_CHOICES = [
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    IS_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]

    s_no = models.AutoField(primary_key=True)
    nf_type = models.CharField(max_length=20, choices=NF_TYPE_CHOICES)
    release_tag = models.CharField(max_length=30)
    ats_release_tag = models.CharField(max_length=30, blank=True, null=True)
    namespace = models.CharField(max_length=50)
    is_csar = models.CharField(max_length=3, choices=IS_CHOICES)
    is_asm = models.CharField(max_length=3, choices=IS_CHOICES)
    is_tgz = models.CharField(max_length=3, choices=IS_CHOICES)
    is_internal_ats = models.CharField(max_length=3, choices=IS_CHOICES)
    is_occ = models.CharField(max_length=3, choices=IS_CHOICES)
    is_pcf = models.CharField(max_length=3, choices=IS_CHOICES)
    is_converged = models.CharField(max_length=3, choices=IS_CHOICES)
    upg_rollback = models.CharField(max_length=3, choices=IS_CHOICES)
    offical_build = models.CharField(max_length=3, choices=IS_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=50, blank=True, null=True)
    allocation_lock = models.CharField(max_length=3, choices=IS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'namespace_status'
