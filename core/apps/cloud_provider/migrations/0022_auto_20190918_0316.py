# Generated by Django 2.1.2 on 2019-09-18 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0013_remove_cluster_terraform_hosts'),
        ('cloud_provider', '0021_auto_20190903_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terraformhost',
            name='host',
        ),
        migrations.DeleteModel(
            name='TerraformHost',
        ),
    ]