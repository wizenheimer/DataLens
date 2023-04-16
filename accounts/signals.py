from django.db.models import signals
from django.dispatch import receiver
from .models import TeamAssignment, SnippetAssignment, SchemaAssignment
from django.core.mail import send_mail


@receiver(signals.pre_save, sender=TeamAssignment)
def notify_team_assignment(sender, instance, **kwargs):
    team = instance.team
    user = instance.user
    can_add_teammate = instance.can_add_teammate
    can_remove_teammate = instance.can_remove_teammate
    # message composer
    if TeamAssignment.objects.filter(team=team, user=user).exists():
        message = "Permissions changed for the team."
    else:
        message = "You've been added to the team."
    subject = message

    if can_add_teammate:
        message += "\nPermission: Can Add Teammates."
    else:
        message += "\nPermission: Can't Add Teammates."

    if can_remove_teammate:
        message += "\nPermission: Can Remove Teammates."
    else:
        message += "\nPermission: Can't Remove Teammates."

    send_mail(
        subject=subject,
        message=message,
        from_email="djangomailer@mail.com",
        recipient_list=[
            user.email,
        ],
    )


@receiver(signals.pre_save, sender=SchemaAssignment)
def notify_schema_assignment(sender, instance, **kwargs):
    schema = instance.schema
    user = instance.user
    can_view_schema = instance.can_view_schema
    can_edit_schema = instance.can_edit_schema
    # message composer
    if SchemaAssignment.objects.filter(schema=schema, user=user).exists():
        message = "Permissions changed for the Schema."
    else:
        message = "You've been added to the Schema."
    subject = message

    if can_view_schema:
        message += "\nPermission: Can view Schema."
    else:
        message += "\nPermission: Can't view Schema."

    if can_edit_schema:
        message += "\nPermission: Can edit Schema."
    else:
        message += "\nPermission: Can't edit Schema."

    send_mail(
        subject=subject,
        message=message,
        from_email="djangomailer@mail.com",
        recipient_list=[
            user.email,
        ],
    )


@receiver(signals.pre_save, sender=SnippetAssignment)
def notify_snippet_assignment(sender, instance, **kwargs):
    snippet = instance.snippet
    user = instance.user
    can_view_snippet = instance.can_view_snippet
    can_edit_snippet = instance.can_edit_snippet
    # message composer
    if SnippetAssignment.objects.filter(snippet=snippet, user=user).exists():
        message = "Permissions changed for the Snippet."
    else:
        message = "You've been added to the Snippet."
    subject = message

    if can_view_snippet:
        message += "\nPermission: Can view snippet."
    else:
        message += "\nPermission: Can't view snippet."

    if can_edit_snippet:
        message += "\nPermission: Can edit snippet."
    else:
        message += "\nPermission: Can't edit snippet."

    send_mail(
        subject=subject,
        message=message,
        from_email="djangomailer@mail.com",
        recipient_list=[
            user.email,
        ],
    )
