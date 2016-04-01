import boto3
from boto3.dynamodb.conditions import Key, Attr


def get_environment():
    table_name = 'fran-env-mcm-crud'
    environment_ids = ["D99D7426-784F-4E94-BDD3-2E55DC16AFC6",
                       "03946090-E224-439E-83D1-ED9F65FA8A69",
                       "80BCE1C9-7145-4F5A-AB7C-791D5AB031A5"]
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(table_name)
    data = []
    for i in environment_ids:
        inst = table.get_item(
            Key={'customer': '799688', 'environment_id': i}).get('Item')
        if inst is not None:
            data.append(environment(inst))
    print data


def environment(inst):
    return {
        'environment_id': inst['environment_id'],
        'name': inst['stage'],
        'stage': inst['stage'],
        'protected': inst['protected'],
        'deploy_strategy': inst['deploy_strategy'],
        'domain': inst['domain'],
        'next_stage': inst['stage_path'],
        'creation_time': inst['created_at'],
        'status': inst['status'],
        'inputs': inst['inputs']
    }


def main():
    get_environment()


if __name__ == '__main__':
    main()
