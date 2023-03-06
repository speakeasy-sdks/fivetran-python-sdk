import requests as requests_http
from . import utils
from sdk.models import operations
from typing import Any, Optional

class WebhookManagement:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def create_account_webhook(self, request: operations.CreateAccountWebhookRequest) -> operations.CreateAccountWebhookResponse:
        r"""Create account webhook
        This endpoint allows you to create a new webhook for the current account.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/webhooks/account'
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateAccountWebhookResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.create_account_webhook_200_application_json_any = out

        return res

    def create_group_webhook(self, request: operations.CreateGroupWebhookRequest) -> operations.CreateGroupWebhookResponse:
        r"""Create group webhook
        This endpoint allows you to create a new webhook for a given group
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/webhooks/group/{groupId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateGroupWebhookResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.create_group_webhook_200_application_json_any = out

        return res

    def delete_webhook(self, request: operations.DeleteWebhookRequest) -> operations.DeleteWebhookResponse:
        r"""Delete webhook
        This endpoint allows you to delete an existing webhook with a given identifier
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/webhooks/{webhookId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteWebhookResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_webhook_204_application_json_any = out

        return res

    def list_all_webhooks(self, request: operations.ListAllWebhooksRequest) -> operations.ListAllWebhooksResponse:
        r"""Retrieve the list of webhooks
        The endpoint allows you to retrieve the list of existing webhooks available for the current account
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/webhooks'
        
        headers = utils.get_headers(request.headers)
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllWebhooksResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_all_webhooks_200_application_json_any = out

        return res

    def modify_webhook(self, request: operations.ModifyWebhookRequest) -> operations.ModifyWebhookResponse:
        r"""Update webhook
        The endpoint allows you to update the existing webhook with a given identifier
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/webhooks/{webhookId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyWebhookResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_webhook_200_application_json_any = out

        return res

    def test_webhook(self, request: operations.TestWebhookRequest) -> operations.TestWebhookResponse:
        r"""Test webhook
        The endpoint allows you to test an existing webhook. It sends a webhook with a given identifier for a dummy connector with identifier _connector_1
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/webhooks/{webhookId}/test', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TestWebhookResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.test_webhook_200_application_json_any = out

        return res

    def webhook_details(self, request: operations.WebhookDetailsRequest) -> operations.WebhookDetailsResponse:
        r"""Retrieve webhook details
        This endpoint allows you to retrieve details of the existing webhook for a given identifier
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/webhooks/{webhookId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.WebhookDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.webhook_details_200_application_json_any = out

        return res

    