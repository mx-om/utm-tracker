# Generated by Django 3.2.13 on 2023-10-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utm_tracker', '0009_alter_leadsource_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadsource',
            name='enrollment',
            field=models.CharField(choices=[('INCOMPLETE', 'Incomplete'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], default='INCOMPLETE', max_length=150),
        ),
        migrations.AddField(
            model_name='leadsource',
            name='session_id',
            field=models.CharField(default=None, help_text='session_id: Session id of the user', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leadsource',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
