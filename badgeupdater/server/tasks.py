from badges.models import Badge
from badgeupdater.server.badge_updater import BadgeUpdater
from kcc3.celery import app


@app.task(bind=True)
def update_badge_task(self, badge_id: str):
    badge = Badge.objects.get(id=badge_id)
    BadgeUpdater(badge).update_badge()
