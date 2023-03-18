<div align="center">
    <img src="https://user-images.githubusercontent.com/68016351/223284832-d571065b-026c-46d4-88a6-a895afeb8c97.png" width="500">
    <p>Fivetran makes access to data as simple and reliable as electricity, and our REST API makes it automatable! With our API, you can build a data-driven applications on top of our platform with Powered by Fivetran </p>
    <a href="https://developers.fivetran.com/openapi/reference/v1/overview/"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
    <a href="https://github.com/speakeasy-sdks/fivetran-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/fivetran-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
    <a href="https://github.com/speakeasy-sdks/fivetran-python-sdk/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/fivetran-python-sdk?sort=semver&style=for-the-badge"/></a>
</div>

## Authentication

Account Administrators in Free, Standard, Enterprise, and Business Critical accounts can manage the API configuration settings. To access the API configuration settings:

1) Log in to [Fivetran](https://fivetran.com/login).
2) In the bottom left menu, click on your username, then click API Key to access your user-level API key and secret.

Fivetran REST API uses API Key authentication. For each request to the API provide an Authorization HTTP header with the following value: Basic `{api_key}:{api_secret}`. The `{api_key}:{api_secret}` part should be base64 encoded.

For instance, for API key `d9c4511349dd4b86` and API secret `1f6f2d161365888a1943160ccdb8d968`, encode d`9c4511349dd4b86:1f6f2d161365888a1943160ccdb8d968` to base64 `(ZDljNDUxMTM0OWRkNGI4NjoxZjZmMmQxNjEzNjU4ODhhMTk0MzE2MGNjZGI4ZDk2OA==)` and use the following Authorization HTTP header value:

`Basic ZDljNDUxMTM0OWRkNGI4NjoxZjZmMmQxNjEzNjU4ODhhMTk0MzE2MGNjZGI4ZDk2OA==`

NOTE: The API key is unique for the account and Account Administrator user pair. Different Account Administrators have different API keys.

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install fivetran-python-sdk
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import fivetran
from fivetran.models import operations, shared

s = fivetran.Fivetran(
    security=shared.Security(
        password="YOUR_PASSWORD_HERE",
        username="YOUR_USERNAME_HERE",
    ),
)


req = operations.ApproveCertificateRequest(
    accept="application/json",
    trust_certificate_request=shared.TrustCertificateRequest(
        connector_id="unde",
        destination_id="deserunt",
        encoded_cert="porro",
        hash="nulla",
    ),
)
    
res = s.certificate_management.approve_certificate(req)

if res.approve_certificate_200_application_json_any is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### certificate_management

* `approve_certificate` - Approve a certificate
* `approve_fingerprint` - Approve a fingerprint

### connector_management

* `connect_card` - Connect Card
* `connector_details` - Retrieve Connector Details
* `create_connector` - Create a Connector
* `delete_connector` - Delete a Connector
* `metadata_connector_config` - Retrieve connector configuration metadata
* `metadata_connectors` - Retrieve source metadata
* `modify_connector` - Modify a Connector
* `resync_connector` - Re-sync Connector Data (Historical Sync)
* `run_setup_tests` - Run connector setup tests
* `sync_connector` - Sync Connector Data

### connector_schema_management

* `connector_column_config` - Retrieve Source Table Columns Config
* `connector_schema_config` - Retrieve a Connector Schema Config
* `modify_connector_column_config` - Modify a Connector Column Config
* `modify_connector_database_schema_config` - Modify a Connector Database Schema Config
* `modify_connector_schema_config` - Modify a Connector Schema Config
* `modify_connector_table_config` - Modify a Connector Table Config
* `reload_connector_schema_config` - Reload a Connector Schema Config
* `resync_tables` - Re-sync Connector Table Data

### dbt_transformation_management

* `create_dbt_project` - Create DBT Project
* `create_dbt_transformation` - Create DBT Transformation
* `dbt_model_details` - Retrieve DBT Model Details
* `dbt_project_details` - Retrieve DBT Project Details
* `dbt_transformation_details` - Retrieve DBT Transformation Details
* `delete_dbt_transformation` - Delete DBT Transformation
* `list_dbt_project_models` - List All DBT Models
* `list_dbt_project_transformations` - List All DBT Transformations
* `list_dbt_projects` - List All DBT Projects
* `modify_dbt_transformation` - Modify DBT Transformation
* `test_dbt_project` - Test DBT Project

### destination_management

* `create_destination` - Create destination
* `delete_destination` - Delete a destination
* `destination_details` - Retrieve Destination Details
* `modify_destination` - Modify a Destination
* `run_destination_setup_tests` - Run Destination Setup Tests

### group_management

* `add_user_to_group` - Add a User to a Group
* `create_group` - Create a Group
* `delete_group` - Delete a group
* `delete_user_from_group` - Remove a User from a Group
* `group_details` - Retrieve Group Details
* `list_all_connectors_in_group` - List All Connectors within a Group
* `list_all_groups` - List All Groups
* `list_all_users_in_group` - List All Users within a Group
* `modify_group` - Modify a Group

### metadata_management

* `column_metadata` - Retrieve column metadata
* `schema_metadata` - Retrieve schema metadata
* `table_metadata` - Retrieve table metadata

### role_management

* `list_all_roles` - List all roles

### team_management

* `add_team_membership_in_connector` - Add connector membership
* `add_team_membership_in_group` - Add group membership
* `add_user_to_team` - Add a user to a team
* `create_team` - Create a team
* `delete_team` - Delete a team
* `delete_team_membership_in_account` - Delete team role in account
* `delete_team_membership_in_connector` - Delete connector membership
* `delete_team_membership_in_group` - Delete group membership
* `delete_user_from_team` - Delete a user from a team
* `get_team_membership_in_connector` - Retrieve connector membership
* `get_team_membership_in_group` - Retrieve group membership
* `get_team_memberships_in_connectors` - List all connector memberships
* `get_team_memberships_in_groups` - List all group memberships
* `get_user_in_team` - Retrieve user membership in a team
* `list_all_teams` - List all teams
* `list_users_in_team` - List all user memberships
* `modify_team` - Modify a team
* `team_details` - Retrieve team details
* `update_team_membership_in_connector` - Update connector membership
* `update_team_membership_in_group` - Update group membership
* `update_user_membership` - Modify a user membership

### user_management

* `add_user_membership_in_connector` - Add connector membership
* `add_user_membership_in_group` - Add group membership
* `create_user` - Invite a User
* `delete_user` - Delete a user
* `delete_user_membership_in_account` - Delete user role in account
* `delete_user_membership_in_connector` - Delete connector membership
* `delete_user_membership_in_group` - Delete group membership
* `get_user_membership_in_connector` - Retrieve connector membership
* `get_user_membership_in_group` - Retrieve group membership
* `get_user_memberships_in_connectors` - List all connector memberships
* `get_user_memberships_in_groups` - List all group memberships
* `list_all_users` - List All Users
* `modify_user` - Modify a User
* `update_user_membership_in_connector` - Update connector membership
* `update_user_membership_in_group` - Update group membership
* `user_details` - Retrieve User Details

### webhook_management

* `create_account_webhook` - Create account webhook
* `create_group_webhook` - Create group webhook
* `delete_webhook` - Delete webhook
* `list_all_webhooks` - Retrieve the list of webhooks
* `modify_webhook` - Update webhook
* `test_webhook` - Test webhook
* `webhook_details` - Retrieve webhook details
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
