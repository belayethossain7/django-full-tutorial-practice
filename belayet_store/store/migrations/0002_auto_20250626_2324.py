# Generated by Django 4.2.23 on 2025-06-26 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
        INSERT INTO store_collection(title)
                          VALUES('Collection1')
        
        ""","""
        DELETE FROM store_collection
        WHERE title = 'Collection1'
""")
    ]
