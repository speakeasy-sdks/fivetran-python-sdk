# dbt_transformation_management

### Available Operations

* [create_dbt_project](#create_dbt_project) - Create DBT Project
* [create_dbt_transformation](#create_dbt_transformation) - Create DBT Transformation
* [dbt_model_details](#dbt_model_details) - Retrieve DBT Model Details
* [dbt_project_details](#dbt_project_details) - Retrieve DBT Project Details
* [dbt_transformation_details](#dbt_transformation_details) - Retrieve DBT Transformation Details
* [delete_dbt_transformation](#delete_dbt_transformation) - Delete DBT Transformation
* [list_dbt_project_models](#list_dbt_project_models) - List All DBT Models
* [list_dbt_project_transformations](#list_dbt_project_transformations) - List All DBT Transformations
* [list_dbt_projects](#list_dbt_projects) - List All DBT Projects
* [modify_dbt_transformation](#modify_dbt_transformation) - Modify DBT Transformation
* [test_dbt_project](#test_dbt_project) - Test DBT Project

## create_dbt_project

Creates a new DBT Project within a specified Group.

### Example Usage

```python
import fivetran
from fivetran.models import operations, shared

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.CreateDbtProjectRequest(
    accept="application/json",
    new_dbt_project_request=shared.NewDbtProjectRequest(
        dbt_version="error",
        default_schema="temporibus",
        folder_path="laborum",
        git_branch="quasi",
        git_remote_url="reiciendis",
        group_id="voluptatibus",
        target_name="vero",
        threads=468651,
    ),
)

res = s.dbt_transformation_management.create_dbt_project(req)

if res.create_dbt_project_201_application_json_object is not None:
    # handle response
```

## create_dbt_transformation

Creates a new DBT Transformation within a specified DBT Project.

### Example Usage

```python
import fivetran
from fivetran.models import operations, shared

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.CreateDbtTransformationRequest(
    accept="application/json",
    new_transformation_request=shared.NewTransformationRequest(
        dbt_model_id="praesentium",
        run_tests=False,
        schedule=shared.TransformationSchedule(
            days_of_week=[
                "MONDAY",
                "FRIDAY",
                "THURSDAY",
                "SATURDAY",
            ],
            interval=19987,
            schedule_type="INTEGRATED",
            time_of_day="reprehenderit",
        ),
    ),
    project_id="ut",
)

res = s.dbt_transformation_management.create_dbt_transformation(req)

if res.create_dbt_transformation_201_application_json_object is not None:
    # handle response
```

## dbt_model_details

Returns a DBT Model details if a valid identifier was provided.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.DbtModelDetailsRequest(
    accept="application/json",
    model_id="maiores",
)

res = s.dbt_transformation_management.dbt_model_details(req)

if res.dbt_model_details_200_application_json_object is not None:
    # handle response
```

## dbt_project_details

Returns a DBT Project details if a valid identifier was provided.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.DbtProjectDetailsRequest(
    accept="application/json",
    project_id="dicta",
)

res = s.dbt_transformation_management.dbt_project_details(req)

if res.dbt_project_details_200_application_json_object is not None:
    # handle response
```

## dbt_transformation_details

Returns a DBT Transformation details if a valid identifier was provided.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.DbtTransformationDetailsRequest(
    accept="application/json",
    transformation_id="corporis",
)

res = s.dbt_transformation_management.dbt_transformation_details(req)

if res.dbt_transformation_details_200_application_json_object is not None:
    # handle response
```

## delete_dbt_transformation

Deletes a DBT Transformation from your DBT Project.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.DeleteDbtTransformationRequest(
    accept="application/json",
    transformation_id="dolore",
)

res = s.dbt_transformation_management.delete_dbt_transformation(req)

if res.delete_dbt_transformation_200_application_json_object is not None:
    # handle response
```

## list_dbt_project_models

Returns a list of all DBT Models within DBT Project.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.ListDbtProjectModelsRequest(
    accept="application/json",
    cursor="iusto",
    limit=118727,
    project_id="harum",
)

res = s.dbt_transformation_management.list_dbt_project_models(req)

if res.list_dbt_project_models_200_application_json_object is not None:
    # handle response
```

## list_dbt_project_transformations

Returns a list of all DBT Transformations within DBT Project.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.ListDbtProjectTransformationsRequest(
    accept="application/json",
    cursor="enim",
    limit=880476,
    project_id="commodi",
)

res = s.dbt_transformation_management.list_dbt_project_transformations(req)

if res.list_dbt_project_transformations_200_application_json_object is not None:
    # handle response
```

## list_dbt_projects

Returns a list of all DBT Projects within your Fivetran account.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.ListDbtProjectsRequest(
    accept="application/json",
    cursor="repudiandae",
    group_id="quae",
    limit=216822,
)

res = s.dbt_transformation_management.list_dbt_projects(req)

if res.list_dbt_projects_200_application_json_object is not None:
    # handle response
```

## modify_dbt_transformation

Updates information for an existing DBT Transformation.

### Example Usage

```python
import fivetran
from fivetran.models import operations, shared

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.ModifyDbtTransformationRequest(
    accept="application/json",
    update_transformation_request=shared.UpdateTransformationRequest(
        run_tests=False,
        schedule=shared.TransformationSchedule(
            days_of_week=[
                "THURSDAY",
                "THURSDAY",
                "SUNDAY",
            ],
            interval=265389,
            schedule_type="TIME_OF_DAY",
            time_of_day="rem",
        ),
    ),
    transformation_id="voluptates",
)

res = s.dbt_transformation_management.modify_dbt_transformation(req)

if res.modify_dbt_transformation_200_application_json_object is not None:
    # handle response
```

## test_dbt_project

Runs setup tests for DBT Project.

### Example Usage

```python
import fivetran
from fivetran.models import operations

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.TestDbtProjectRequest(
    accept="application/json",
    project_id="quasi",
)

res = s.dbt_transformation_management.test_dbt_project(req)

if res.test_dbt_project_200_application_json_object is not None:
    # handle response
```
