import requests as requests_http
from . import utils
from fivetran.models import operations
from typing import Any, Optional

class DBTTransformationManagement:
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
        
    def create_dbt_project(self, request: operations.CreateDbtProjectRequest) -> operations.CreateDbtProjectResponse:
        r"""Create DBT Project
        Creates a new DBT Project within a specified Group.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/dbt/projects'
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateDbtProjectResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.create_dbt_project_201_application_json_any = out

        return res

    def create_dbt_transformation(self, request: operations.CreateDbtTransformationRequest) -> operations.CreateDbtTransformationResponse:
        r"""Create DBT Transformation
        Creates a new DBT Transformation within a specified DBT Project.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/dbt/projects/{projectId}/transformations', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateDbtTransformationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.create_dbt_transformation_201_application_json_any = out

        return res

    def dbt_model_details(self, request: operations.DbtModelDetailsRequest) -> operations.DbtModelDetailsResponse:
        r"""Retrieve DBT Model Details
        Returns a DBT Model details if a valid identifier was provided.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/dbt/models/{modelId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DbtModelDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.dbt_model_details_200_application_json_any = out

        return res

    def dbt_project_details(self, request: operations.DbtProjectDetailsRequest) -> operations.DbtProjectDetailsResponse:
        r"""Retrieve DBT Project Details
        Returns a DBT Project details if a valid identifier was provided.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/dbt/projects/{projectId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DbtProjectDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.dbt_project_details_200_application_json_any = out

        return res

    def dbt_transformation_details(self, request: operations.DbtTransformationDetailsRequest) -> operations.DbtTransformationDetailsResponse:
        r"""Retrieve DBT Transformation Details
        Returns a DBT Transformation details if a valid identifier was provided.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/dbt/transformations/{transformationId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DbtTransformationDetailsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.dbt_transformation_details_200_application_json_any = out

        return res

    def delete_dbt_transformation(self, request: operations.DeleteDbtTransformationRequest) -> operations.DeleteDbtTransformationResponse:
        r"""Delete DBT Transformation
        Deletes a DBT Transformation from your DBT Project.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/dbt/transformations/{transformationId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteDbtTransformationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_dbt_transformation_200_application_json_any = out

        return res

    def list_dbt_project_models(self, request: operations.ListDbtProjectModelsRequest) -> operations.ListDbtProjectModelsResponse:
        r"""List All DBT Models
        Returns a list of all DBT Models within DBT Project.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/dbt/projects/{projectId}/models', request.path_params)
        
        headers = utils.get_headers(request.headers)
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListDbtProjectModelsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_dbt_project_models_200_application_json_any = out

        return res

    def list_dbt_project_transformations(self, request: operations.ListDbtProjectTransformationsRequest) -> operations.ListDbtProjectTransformationsResponse:
        r"""List All DBT Transformations
        Returns a list of all DBT Transformations within DBT Project.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/dbt/projects/{projectId}/transformations', request.path_params)
        
        headers = utils.get_headers(request.headers)
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListDbtProjectTransformationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_dbt_project_transformations_200_application_json_any = out

        return res

    def list_dbt_projects(self, request: operations.ListDbtProjectsRequest) -> operations.ListDbtProjectsResponse:
        r"""List All DBT Projects
        Returns a list of all DBT Projects within your Fivetran account.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/dbt/projects'
        
        headers = utils.get_headers(request.headers)
        query_params = utils.get_query_params(request.query_params)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListDbtProjectsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.list_dbt_projects_200_application_json_any = out

        return res

    def modify_dbt_transformation(self, request: operations.ModifyDbtTransformationRequest) -> operations.ModifyDbtTransformationResponse:
        r"""Modify DBT Transformation
        Updates information for an existing DBT Transformation.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/dbt/transformations/{transformationId}', request.path_params)
        
        headers = utils.get_headers(request.headers)
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._security_client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ModifyDbtTransformationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.modify_dbt_transformation_200_application_json_any = out

        return res

    def test_dbt_project(self, request: operations.TestDbtProjectRequest) -> operations.TestDbtProjectResponse:
        r"""Test DBT Project
        Runs setup tests for DBT Project.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/v1/dbt/projects/{projectId}/test', request.path_params)
        
        headers = utils.get_headers(request.headers)
        
        client = self._security_client
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TestDbtProjectResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.test_dbt_project_200_application_json_any = out

        return res

    