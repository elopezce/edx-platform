from collections import namedtuple

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from config_models.models import ConfigurationModel


class Schedule(TimeStampedModel):
    enrollment = models.OneToOneField('student.CourseEnrollment', null=False)
    active = models.BooleanField(
        default=True,
        help_text=_('Indicates if this schedule is actively used')
    )
    start = models.DateTimeField(
        db_index=True,
        help_text=_('Date this schedule went into effect')
    )
    upgrade_deadline = models.DateTimeField(
        blank=True,
        db_index=True,
        null=True,
        help_text=_('Deadline by which the learner must upgrade to a verified seat')
    )

    class Meta(object):
        verbose_name = _('Schedule')
        verbose_name_plural = _('Schedules')


class ScheduleConfig(ConfigurationModel):
    enqueue_recurring_generic = models.BooleanField(default=False)
    deliver_recurring_generic = models.BooleanField(default=False)
