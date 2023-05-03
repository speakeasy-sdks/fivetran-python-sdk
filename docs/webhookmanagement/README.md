# webhook_management

### Available Operations

* [create_account_webhook](#create_account_webhook) - Create account webhook
* [create_group_webhook](#create_group_webhook) - Create group webhook
* [delete_webhook](#delete_webhook) - Delete webhook
* [list_all_webhooks](#list_all_webhooks) - Retrieve the list of webhooks
* [modify_webhook](#modify_webhook) - Update webhook
* [test_webhook](#test_webhook) - Test webhook
* [webhook_details](#webhook_details) - Retrieve webhook details

## create_account_webhook

This endpoint allows you to create a new webhook for the current account.

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


req = operations.CreateAccountWebhookRequest(
    accept='application/json',
    webhook_request=shared.WebhookRequest(
        active=False,
        events=[
            'perferendis',
        ],
        secret='amet',
        url='optio',
    ),
)

res = s.webhook_management.create_account_webhook(req)

if res.create_account_webhook_200_application_json_object is not None:
    # handle response
```

## create_group_webhook

This endpoint allows you to create a new webhook for a given group

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


req = operations.CreateGroupWebhookRequest(
    accept='application/json',
    webhook_request=shared.WebhookRequest(
        active=False,
        events=[
            'ad',
            'saepe',
            'suscipit',
            'deserunt',
        ],
        secret='provident',
        url='minima',
    ),
    group_id='repellendus',
)

res = s.webhook_management.create_group_webhook(req)

if res.create_group_webhook_200_application_json_object is not None:
    # handle response
```

## delete_webhook

This endpoint allows you to delete an existing webhook with a given identifier

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


req = operations.DeleteWebhookRequest(
    accept='application/json',
    webhook_id='totam',
)

res = s.webhook_management.delete_webhook(req)

if res.delete_webhook_204_application_json_object is not None:
    # handle response
```

## list_all_webhooks

The endpoint allows you to retrieve the list of existing webhooks available for the current account

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


req = operations.ListAllWebhooksRequest(
    accept='application/json',
    cursor='similique',
    limit=55,
)

res = s.webhook_management.list_all_webhooks(req)

if res.list_all_webhooks_200_application_json_object is not None:
    # handle response
```

## modify_webhook

The endpoint allows you to update the existing webhook with a given identifier

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


req = operations.ModifyWebhookRequest(
    accept='application/json',
    webhook_request=shared.WebhookRequest(
        active=False,
        events=[
            'quaerat',
            'tempora',
            'vel',
            'quod',
        ],
        secret='officiis',
        url='qui',
    ),
    webhook_id='dolorum',
)

res = s.webhook_management.modify_webhook(req)

if res.modify_webhook_200_application_json_object is not None:
    # handle response
```

## test_webhook

The endpoint allows you to test an existing webhook. It sends a webhook with a given identifier for a dummy connector with identifier _connector_1

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


req = operations.TestWebhookRequest(
    accept='application/json',
    webhook_test_request=shared.WebhookTestRequest(
        event='a',
    ),
    webhook_id='esse',
)

res = s.webhook_management.test_webhook(req)

if res.test_webhook_200_application_json_object is not None:
    # handle response
```

## webhook_details

This endpoint allows you to retrieve details of the existing webhook for a given identifier

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


req = operations.WebhookDetailsRequest(
    accept='application/json',
    webhook_id='harum',
)

res = s.webhook_management.webhook_details(req)

if res.webhook_details_200_application_json_object is not None:
    # handle response
```
