#Reference: https://medium.com/google-cloud/data-catalog-hands-on-guide-search-get-lookup-with-python-82d99bfb4056
from google.oauth2 import service_account
from google.cloud import datacatalog

file_name = 'path_to_your_service_account.json_file'

#create datacatalog client using service account auth
datacatalog_client = datacatalog.DataCatalogClient.from_service_account_file(file_name)

scope=datacatalog.SearchCatalogRequest.Scope()
#option to include project_ids
scope.include_project_ids.append('dataflow1-282718')
#option to include org_ids
#scope.include_org_ids.append(<organization-id>)

#search queries can be inserted here
results = datacatalog_client.search_catalog(scope=scope,query='system=bigquery type=dataset')

#output results
fetched_results = [result for result in results]
print(fetched_results)