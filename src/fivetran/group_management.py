import requests as requests_http
from . import utils
from fivetran.models import operations
from typing import Any, Optional

class GroupManagement:
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
        
    def add_user_to_group(self, request: operations.AddUserToGroupRequest) -> operations.AddUserToGroupResponse:
        r"""Add a User to a Group
        Adds an existing user to a group in your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.AddUserToGroupRequest, base_url, '/v1/groups/{groupId}/users', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddUserToGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.add_user_to_group_200_application_json_any = out

        return res

    def create_group(self, request: operations.CreateGroupRequest) -> operations.CreateGroupResponse:
        r"""Create a Group
        Creates a new group in your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/groups'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.create_group_201_application_json_any = out

        return res

    def delete_group(self, request: operations.DeleteGroupRequest) -> operations.DeleteGroupResponse:
        r"""Delete a group
        Deletes a group from your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteGroupRequest, base_url, '/v1/groups/{groupId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_group_200_application_json_any = out

        return res

    def delete_user_from_group(self, request: operations.DeleteUserFromGroupRequest) -> operations.DeleteUserFromGroupResponse:
        r"""Remove a User from a Group
        Removes an existing user from a group in your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteUserFromGroupRequest, base_url, '/v1/groups/{groupId}/users/{userId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteUserFromGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_user_from_group_200_application_json_any = out

        return res

    def group_details(self, request: operations.GroupDetailsRequest) -> operations.GroupDetailsResponse:
        r"""Retrieve Group Details
        Returns a group object if a valid identifier was provided.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GroupDetailsRequest, base_url, '/v1/groups/{groupId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GroupDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.group_details_200_application_json_any = out

        return res

    def list_all_connectors_in_group(self, request: operations.ListAllConnectorsInGroupRequest) -> operations.ListAllConnectorsInGroupResponse:
        r"""List All Connectors within a Group
        Returns a list of information about all connectors within a group in your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListAllConnectorsInGroupRequest, base_url, '/v1/groups/{groupId}/connectors', request)
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.ListAllConnectorsInGroupRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllConnectorsInGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_all_connectors_in_group_200_application_json_any = out

        return res

    def list_all_groups(self, request: operations.ListAllGroupsRequest) -> operations.ListAllGroupsResponse:
        r"""List All Groups
        Returns a list of all groups within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/groups'
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.ListAllGroupsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllGroupsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_all_groups_200_application_json_any = out

        return res

    def list_all_users_in_group(self, request: operations.ListAllUsersInGroupRequest) -> operations.ListAllUsersInGroupResponse:
        r"""List All Users within a Group
        Returns a list of information about all users within a group in your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListAllUsersInGroupRequest, base_url, '/v1/groups/{groupId}/users', request)
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.ListAllUsersInGroupRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllUsersInGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_all_users_in_group_200_application_json_any = out

        return res

    def modify_group(self, request: operations.ModifyGroupRequest) -> operations.ModifyGroupResponse:
        r"""Modify a Group
        Updates information for an existing group within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ModifyGroupRequest, base_url, '/v1/groups/{groupId}', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_group_200_application_json_any = out

        return res

    