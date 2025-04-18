# Generated by Django 5.0.6 on 2024-11-06 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_alter_btc_balance_alter_dash_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='discussion_board',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='student',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='result',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='student',
            name='favorite_subject',
        ),
        migrations.RemoveField(
            model_name='student',
            name='level',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lga',
        ),
        migrations.RemoveField(
            model_name='student',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='state_of_origin',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='DiscussionBoard',
        ),
        migrations.DeleteModel(
            name='Hostel',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
