from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer which takes an optional `fields` argument (a list/tuple of
    field names) and only keeps those fields.
    """
    def __init__(self, *args, **kwargs):
        # 1) pop off our custom `fields` kwarg (if any)
        fields = kwargs.pop('fields', None)

        # 2) run DRF's normal __init__, which will populate self.fields
        super().__init__(*args, **kwargs)

        # 3) if the user passed a `fields` list, drop any fields not in it
        if fields is not None:
            allowed = set(fields)
            for field_name in list(self.fields.keys()):
                if field_name not in allowed:
                    self.fields.pop(field_name)
