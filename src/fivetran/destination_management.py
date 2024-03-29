"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from fivetran.models import operations
from typing import Any, Optional

class DestinationManagement:
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
        
    def create_destination(self, request: operations.CreateDestinationRequest) -> operations.CreateDestinationResponse:
        r"""Create destination
        Creates a new destination within a specified group in your Fivetran account.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/destinations'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "new_destination_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateDestinationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.create_destination_201_application_json_any = out
        elif http_res.status_code in [400, 500]:
            pass

        return res

    def delete_destination(self, request: operations.DeleteDestinationRequest) -> operations.DeleteDestinationResponse:
        r"""Delete a destination
        Deletes a destination from your Fivetran account.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteDestinationRequest, base_url, '/v1/destinations/{destinationId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteDestinationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_destination_200_application_json_any = out
        elif http_res.status_code in [404, 409]:
            pass

        return res

    def destination_details(self, request: operations.DestinationDetailsRequest) -> operations.DestinationDetailsResponse:
        r"""Retrieve Destination Details
        Returns a destination object if a valid identifier was provided.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DestinationDetailsRequest, base_url, '/v1/destinations/{destinationId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DestinationDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.destination_details_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def modify_destination(self, request: operations.ModifyDestinationRequest) -> operations.ModifyDestinationResponse:
        r"""Modify a Destination
        Updates information for an existing destination within your Fivetran account.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ModifyDestinationRequest, base_url, '/v1/destinations/{destinationId}', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "update_destination_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyDestinationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_destination_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def run_destination_setup_tests(self, request: operations.RunDestinationSetupTestsRequest) -> operations.RunDestinationSetupTestsResponse:
        r"""Run Destination Setup Tests
        Runs the setup tests for an existing destination within your Fivetran account.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RunDestinationSetupTestsRequest, base_url, '/v1/destinations/{destinationId}/test', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "run_setup_tests_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RunDestinationSetupTestsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.run_destination_setup_tests_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    