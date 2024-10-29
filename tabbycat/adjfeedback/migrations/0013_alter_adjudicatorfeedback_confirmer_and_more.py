# Generated by Django 4.0.6 on 2022-09-24 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('participants', '0019_auto_20201216_1415'),
        ('adjfeedback', '0012_adjudicatorfeedback_private_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='confirmer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_confirmed', to=settings.AUTH_USER_MODEL, verbose_name='confirmer'),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='participant_submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_participant_submitted', to='participants.person', verbose_name='from participant'),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_submitted', to=settings.AUTH_USER_MODEL, verbose_name='submitter'),
        ),
    ]
