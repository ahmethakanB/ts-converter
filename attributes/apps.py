import os
from pathlib import Path
from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

class AttributesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "attributes"

    def ready(self):
        # Otomatik reload sürecini atla, ama gerçek runserver esnasında devam et
        if os.environ.get("RUN_MAIN") != "true":
            return
        if os.environ.get("DJANGO_SKIP_COLUMN_TS"):
            return

        from attributes.exporter import export_all_ts

        target = (
            settings.BASE_DIR / "templates" / "ts_converter" / "columns.ts"
            if hasattr(settings, "BASE_DIR")
            else Path("columns.ts")
        )
        # önceki dosyayı sil
        if target.exists():
            target.unlink()
        # klasörü yarat
        target.parent.mkdir(parents=True, exist_ok=True)

        try:
            export_all_ts(target)
        except Exception as exc:
            raise ImproperlyConfigured(f"columns.ts üretilemedi: {exc}") from exc
