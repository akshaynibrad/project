from django.db import models
from django.utils import timezone

IS_DELETED = (
    (True, True),
    (False, False)
)

class info(models.Model):
    eid = models.IntegerField(blank=False)
    ename = models.CharField(max_length=50, blank=True)
    created_by = models.CharField(max_length=50, blank=False, null=False)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(choices=IS_DELETED, default=False)

    def __unicode__(self):
        return unicode(self.ename)


class salary(models.Model):
    info=models.ForeignKey(info,blank=True,null=True)
    sid = models.IntegerField(blank=False)
    salary = models.FloatField(max_length=50, blank=True)
    created_by = models.CharField(max_length=50, blank=False, null=False)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return unicode(self.salary)
