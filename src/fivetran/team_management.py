import requests as requests_http
from . import utils
from fivetran.models import operations
from typing import Any, Optional

class TeamManagement:
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
        
    def add_team_membership_in_connector(self, request: operations.AddTeamMembershipInConnectorRequest) -> operations.AddTeamMembershipInConnectorResponse:
        r"""Add connector membership
        Adds a connector role within a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.AddTeamMembershipInConnectorRequest, base_url, '/v1/teams/{teamId}/connectors', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "membership_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddTeamMembershipInConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.add_team_membership_in_connector_201_application_json_any = out

        return res

    def add_team_membership_in_group(self, request: operations.AddTeamMembershipInGroupRequest) -> operations.AddTeamMembershipInGroupResponse:
        r"""Add group membership
        Adds a group membership in a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.AddTeamMembershipInGroupRequest, base_url, '/v1/teams/{teamId}/groups', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "membership_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddTeamMembershipInGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.add_team_membership_in_group_201_application_json_any = out

        return res

    def add_user_to_team(self, request: operations.AddUserToTeamRequest) -> operations.AddUserToTeamResponse:
        r"""Add a user to a team
        Assigns a user role within a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.AddUserToTeamRequest, base_url, '/v1/teams/{teamId}/users', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "team_membership_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AddUserToTeamResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.add_user_to_team_201_application_json_any = out

        return res

    def create_team(self, request: operations.CreateTeamRequest) -> operations.CreateTeamResponse:
        r"""Create a team
        Creates a new team in your Fivetran account
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/teams'
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "team_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateTeamResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.create_team_201_application_json_any = out

        return res

    def delete_team(self, request: operations.DeleteTeamRequest) -> operations.DeleteTeamResponse:
        r"""Delete a team
        Deletes a team from your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteTeamRequest, base_url, '/v1/teams/{teamId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteTeamResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_team_200_application_json_any = out

        return res

    def delete_team_membership_in_account(self, request: operations.DeleteTeamMembershipInAccountRequest) -> operations.DeleteTeamMembershipInAccountResponse:
        r"""Delete team role in account
        Removes a team role within your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteTeamMembershipInAccountRequest, base_url, '/v1/teams/{teamId}/role', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteTeamMembershipInAccountResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_team_membership_in_account_200_application_json_any = out

        return res

    def delete_team_membership_in_connector(self, request: operations.DeleteTeamMembershipInConnectorRequest) -> operations.DeleteTeamMembershipInConnectorResponse:
        r"""Delete connector membership
        Removes connector membership in a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteTeamMembershipInConnectorRequest, base_url, '/v1/teams/{teamId}/connectors/{connectorId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteTeamMembershipInConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_team_membership_in_connector_200_application_json_any = out

        return res

    def delete_team_membership_in_group(self, request: operations.DeleteTeamMembershipInGroupRequest) -> operations.DeleteTeamMembershipInGroupResponse:
        r"""Delete group membership
        Removes group membership in a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteTeamMembershipInGroupRequest, base_url, '/v1/teams/{teamId}/groups/{groupId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteTeamMembershipInGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_team_membership_in_group_200_application_json_any = out

        return res

    def delete_user_from_team(self, request: operations.DeleteUserFromTeamRequest) -> operations.DeleteUserFromTeamResponse:
        r"""Delete a user from a team
        Removes a user from a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteUserFromTeamRequest, base_url, '/v1/teams/{teamId}/users/{userId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteUserFromTeamResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_user_from_team_200_application_json_any = out

        return res

    def get_team_membership_in_connector(self, request: operations.GetTeamMembershipInConnectorRequest) -> operations.GetTeamMembershipInConnectorResponse:
        r"""Retrieve connector membership
        Returns a connector membership within a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetTeamMembershipInConnectorRequest, base_url, '/v1/teams/{teamId}/connectors/{connectorId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTeamMembershipInConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_team_membership_in_connector_200_application_json_any = out

        return res

    def get_team_membership_in_group(self, request: operations.GetTeamMembershipInGroupRequest) -> operations.GetTeamMembershipInGroupResponse:
        r"""Retrieve group membership
        Returns a group membership within a team.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetTeamMembershipInGroupRequest, base_url, '/v1/teams/{teamId}/groups/{groupId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTeamMembershipInGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_team_membership_in_group_200_application_json_any = out

        return res

    def get_team_memberships_in_connectors(self, request: operations.GetTeamMembershipsInConnectorsRequest) -> operations.GetTeamMembershipsInConnectorsResponse:
        r"""List all connector memberships
        Returns connector memberships within a team.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetTeamMembershipsInConnectorsRequest, base_url, '/v1/teams/{teamId}/connectors', request)
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.GetTeamMembershipsInConnectorsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTeamMembershipsInConnectorsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_team_memberships_in_connectors_200_application_json_any = out

        return res

    def get_team_memberships_in_groups(self, request: operations.GetTeamMembershipsInGroupsRequest) -> operations.GetTeamMembershipsInGroupsResponse:
        r"""List all group memberships
        Returns a group membership within a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetTeamMembershipsInGroupsRequest, base_url, '/v1/teams/{teamId}/groups', request)
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.GetTeamMembershipsInGroupsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTeamMembershipsInGroupsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_team_memberships_in_groups_200_application_json_any = out

        return res

    def get_user_in_team(self, request: operations.GetUserInTeamRequest) -> operations.GetUserInTeamResponse:
        r"""Retrieve user membership in a team
        Returns the user role a user has within a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetUserInTeamRequest, base_url, '/v1/teams/{teamId}/users/{userId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserInTeamResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_user_in_team_200_application_json_any = out

        return res

    def list_all_teams(self, request: operations.ListAllTeamsRequest) -> operations.ListAllTeamsResponse:
        r"""List all teams
        Returns a list of all teams within your Fivetran account
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/teams'
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.ListAllTeamsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAllTeamsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_all_teams_200_application_json_any = out

        return res

    def list_users_in_team(self, request: operations.ListUsersInTeamRequest) -> operations.ListUsersInTeamResponse:
        r"""List all user memberships
        Returns a list of users and their roles within a team in your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListUsersInTeamRequest, base_url, '/v1/teams/{teamId}/users', request)
        
        headers = utils.get_headers(request)
        query_params = utils.get_query_params(operations.ListUsersInTeamRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListUsersInTeamResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_users_in_team_200_application_json_any = out

        return res

    def modify_team(self, request: operations.ModifyTeamRequest) -> operations.ModifyTeamResponse:
        r"""Modify a team
        Updates information for an existing team within your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ModifyTeamRequest, base_url, '/v1/teams/{teamId}', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "team_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyTeamResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_team_200_application_json_any = out

        return res

    def team_details(self, request: operations.TeamDetailsRequest) -> operations.TeamDetailsResponse:
        r"""Retrieve team details
        Returns information for a given team within your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.TeamDetailsRequest, base_url, '/v1/teams/{teamId}', request)
        
        headers = utils.get_headers(request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TeamDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.team_details_200_application_json_any = out

        return res

    def update_team_membership_in_connector(self, request: operations.UpdateTeamMembershipInConnectorRequest) -> operations.UpdateTeamMembershipInConnectorResponse:
        r"""Update connector membership
        Updates connector membership in a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateTeamMembershipInConnectorRequest, base_url, '/v1/teams/{teamId}/connectors/{connectorId}', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "update_membership_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateTeamMembershipInConnectorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.update_team_membership_in_connector_200_application_json_any = out

        return res

    def update_team_membership_in_group(self, request: operations.UpdateTeamMembershipInGroupRequest) -> operations.UpdateTeamMembershipInGroupResponse:
        r"""Update group membership
        Updates group membership in a team
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateTeamMembershipInGroupRequest, base_url, '/v1/teams/{teamId}/groups/{groupId}', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "update_membership_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateTeamMembershipInGroupResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.update_team_membership_in_group_200_application_json_any = out

        return res

    def update_user_membership(self, request: operations.UpdateUserMembershipRequest) -> operations.UpdateUserMembershipResponse:
        r"""Modify a user membership
        Updates a user role within a team in your Fivetran account
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateUserMembershipRequest, base_url, '/v1/teams/{teamId}/users/{userId}', request)
        
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, "update_membership_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateUserMembershipResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.update_user_membership_200_application_json_any = out

        return res

    