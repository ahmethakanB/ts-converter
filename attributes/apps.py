import os
import shutil
from pathlib import Path

from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class AttributesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "attributes"

    def ready(self):
        if os.environ.get("RUN_MAIN") != "true":
            return
        if os.environ.get("DJANGO_SKIP_COLUMN_TS"):
            return

        from attributes.exporter import export_all_ts

        target_dir = (
            settings.BASE_DIR / "templates" / "ts_converter"
            if hasattr(settings, "BASE_DIR")
            else Path("templates") / "ts_converter"
        )
        if target_dir.exists():
            shutil.rmtree(target_dir)

        export_all_ts(target_dir)
        try:
            export_all_ts(target_dir)
        except Exception as exc:
            raise ImproperlyConfigured(f"TS files üretilemedi: {exc}") from exc
