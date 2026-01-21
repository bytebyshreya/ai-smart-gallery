from django.db.models.signals import post_delete
from django.dispatch import receiver
from gallery.models import Photo, Event, PersonGroup, Face
@receiver(post_delete, sender=Photo)
def delete_empty_event(sender, instance, **kwargs):
    event = instance.event
    if event and event.photos.count() == 0:
        event.delete()
@receiver(post_delete, sender=Face)
def delete_empty_person_group(sender, instance, **kwargs):
    person = instance.person_group
    if person and person.faces.count() == 0:
        person.delete()
