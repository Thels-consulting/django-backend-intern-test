# TODO (candidate): Define DepartmentViewSet and EmployeeViewSet here using
# rest_framework.viewsets.ModelViewSet, once your models and serializers
# exist.
#
# Requirements to implement on the views:
#   - Unauthenticated users may GET (list/retrieve) employees and departments.
#   - Only authenticated users may POST/PUT/DELETE.
#   - Employee list must support filtering by `department` and `is_active`,
#     e.g. GET /api/employees/?department=1&is_active=true
#   - Employee list must support search across first_name, last_name, email,
#     and job_title, e.g. GET /api/employees/?search=john
#
# See the README for the full endpoint and permission spec.
