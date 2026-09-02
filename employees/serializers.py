# TODO (candidate): Define DepartmentSerializer and EmployeeSerializer here
# using rest_framework.serializers.ModelSerializer, once the Department and
# Employee models exist in models.py.
#
# Remember the API must reject:
#   - duplicate employee email
#   - invalid email format
#   - negative salary
#   - a department id that doesn't exist
#
# Model-level constraints (unique=True, MinValueValidator, EmailField) are
# inherited automatically by ModelSerializer in most cases, but confirm this
# with your own tests.
