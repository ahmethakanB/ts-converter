from rest_framework.filters import BaseFilterBackend
from odata_query.django import apply_odata_query

class ODataFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        qp = request.query_params
        qs = queryset

        if '$filter' in qp:
            qs = apply_odata_query(qs, qp['$filter'])

        if '$orderby' in qp:
            qs = apply_odata_query(qs, f"$orderby={qp['$orderby']}")

        if '$skip' in qp:
            qs = qs[int(qp['$skip']):]
        if '$top' in qp:
            qs = qs[: int(qp['$top'])]

        if '$select' in qp:
            setattr(request, '_odata_select', qp['$select'].split(','))

        return qs