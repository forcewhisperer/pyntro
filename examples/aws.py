import boto3


def get_account_info():
    iam = boto3.client('iam')
    account_summary = iam.get_account_authorization_details()

    print account_summary


def cloudformation_outputs(stackname):
    cf = boto3.client('cloudformation')

    stacks = cf.describe_stacks

    stacks = stacks(StackName=stackname)

    print stacks


def main():
    get_account_info()

if __name__ == '__main__':
    main()
