import requests as requests_http
from . import utils
from fivetran.models import operations, shared
from typing import Any, Optional

class UserManagement:
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
        
    def add_user_membership_in_connector(self, request: operations.AddUserMembershipInConnectorRequest) -> operations.AddUserMembershipInConnectorResponse:
        r"""Add connector membership
        Adds a connector membership
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/connectors', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddUserMembershipInConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.MembershipResponse])
                res.membership_response = out

        return res

    def add_user_membership_in_group(self, request: operations.AddUserMembershipInGroupRequest) -> operations.AddUserMembershipInGroupResponse:
        r"""Add group membership
        Adds a group membership.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/groups', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddUserMembershipInGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.add_user_membership_in_group_201_application_json_any = out
        elif http_res.status_code == 400:
            pass
        elif http_res.status_code == 404:
            pass

        return res

    def create_user(self, request: operations.CreateUserRequest) -> operations.CreateUserResponse:
        r"""Invite a User
        Invites a new user to your Fivetran account. The invited user will have access to the account only after accepting the invitation. Invited user details are still accessible through the API.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/users'
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.create_user_201_application_json_any = out
        elif http_res.status_code == 400:
            pass

        return res

    def delete_user(self, request: operations.DeleteUserRequest) -> operations.DeleteUserResponse:
        r"""Delete a user
        Deletes a user from your Fivetran account. You will be unable to delete an account owner user if there is only one remaining.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_user_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def delete_user_membership_in_account(self, request: operations.DeleteUserMembershipInAccountRequest) -> operations.DeleteUserMembershipInAccountResponse:
        r"""Delete user role in account
        Removes a user's role in account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/role', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteUserMembershipInAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_user_membership_in_account_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def delete_user_membership_in_connector(self, request: operations.DeleteUserMembershipInConnectorRequest) -> operations.DeleteUserMembershipInConnectorResponse:
        r"""Delete connector membership
        Removes connector membership.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/connectors/{connectorId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteUserMembershipInConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_user_membership_in_connector_200_application_json_any = out

        return res

    def delete_user_membership_in_group(self, request: operations.DeleteUserMembershipInGroupRequest) -> operations.DeleteUserMembershipInGroupResponse:
        r"""Delete group membership
        Removes group membership.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/groups/{groupId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteUserMembershipInGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_user_membership_in_group_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def get_user_membership_in_connector(self, request: operations.GetUserMembershipInConnectorRequest) -> operations.GetUserMembershipInConnectorResponse:
        r"""Retrieve connector membership
        Returns a connector membership object.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/connectors/{connectorId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserMembershipInConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_user_membership_in_connector_200_application_json_any = out

        return res

    def get_user_membership_in_group(self, request: operations.GetUserMembershipInGroupRequest) -> operations.GetUserMembershipInGroupResponse:
        r"""Retrieve group membership
        Returns a group membership object.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/groups/{groupId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserMembershipInGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_user_membership_in_group_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def get_user_memberships_in_connectors(self, request: operations.GetUserMembershipsInConnectorsRequest) -> operations.GetUserMembershipsInConnectorsResponse:
        r"""List all connector memberships
        Returns all connector membership objects for a user within your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/connectors', request.path_params)
        
        headers = utils.get_headers(request.headers)
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserMembershipsInConnectorsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_user_memberships_in_connectors_200_application_json_any = out

        return res

    def get_user_memberships_in_groups(self, request: operations.GetUserMembershipsInGroupsRequest) -> operations.GetUserMembershipsInGroupsResponse:
        r"""List all group memberships
        Returns all group membership objects for a user within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/groups', request.path_params)
        
        headers = utils.get_headers(request.headers)
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserMembershipsInGroupsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_user_memberships_in_groups_200_application_json_any = out

        return res

    def list_all_users(self, request: operations.ListAllUsersRequest) -> operations.ListAllUsersResponse:
        r"""List All Users
        Returns a list of all users within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/users'
        
        headers = utils.get_headers(request.headers)
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllUsersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_all_users_200_application_json_any = out

        return res

    def modify_user(self, request: operations.ModifyUserRequest) -> operations.ModifyUserResponse:
        r"""Modify a User
        Updates information for an existing user within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_user_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def update_user_membership_in_connector(self, request: operations.UpdateUserMembershipInConnectorRequest) -> operations.UpdateUserMembershipInConnectorResponse:
        r"""Update connector membership
        Updates connector membership.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/connectors/{connectorId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateUserMembershipInConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.update_user_membership_in_connector_200_application_json_any = out

        return res

    def update_user_membership_in_group(self, request: operations.UpdateUserMembershipInGroupRequest) -> operations.UpdateUserMembershipInGroupResponse:
        r"""Update group membership
        Updates group membership.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}/groups/{groupId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateUserMembershipInGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.update_user_membership_in_group_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    def user_details(self, request: operations.UserDetailsRequest) -> operations.UserDetailsResponse:
        r"""Retrieve User Details
        Returns a user object if a valid identifier was provided.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/users/{userId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UserDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.user_details_200_application_json_any = out
        elif http_res.status_code == 404:
            pass

        return res

    