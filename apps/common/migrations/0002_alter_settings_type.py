# Generated by Django 4.2.9 on 2024-03-24 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='type',
            field=models.CharField(choices=[('site_name', 'Site name'), ('copyright', 'Copyright'), ('stripe_pub_key', 'Stripe publishable key'), ('stripe_sec_key', 'Stripe secret key'), ('social_twitter', 'Social twitter'), ('social_instagram', 'Social instagram'), ('social_github', 'Social github'), ('social_facebook', 'Social facebook'), ('legal_privacy', 'Legal privacy'), ('legal_terms', 'Legal terms'), ('legal_help', 'Legal help'), ('hero_video', 'Hero video')], max_length=255, unique=True),
        ),
    ]
