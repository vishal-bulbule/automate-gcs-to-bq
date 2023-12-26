from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "prj-poc-001"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
    "jobName": "bq-load",  # Provide a unique name for the job
    "parameters": {
        "javascriptTextTransformGcsPath": "gs://bkt-df-metadata/udf.js",
        "JSONPath": "gs://bkt-df-metadata/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "prj-poc-001:user_data.users",
        "inputFilePattern": "gs://bkt-landing-zone/user.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://bkt-df-metadata"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

