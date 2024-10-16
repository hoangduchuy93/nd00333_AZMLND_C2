from azureml.core import Workspace
from azureml.core.webservice import Webservice



subscription_id =  "610d6e37-4747-4a20-80eb-3aad70a55f43"
resource_group =  "aml-quickstarts-268740"
workspace_name =  "quick-starts-ws-268740"

# Requires the config to be downloaded first to the current working directory
ws = Workspace.from_config(path="./config.json")

# Set with the deployment name
name = "demo-model-deploy"

# load existing web service
service = Webservice(name=name, workspace=ws)

# enable application insight
service.update(enable_app_insights=True)

logs = service.get_logs()

for line in logs.split('\n'):
    print(line)
