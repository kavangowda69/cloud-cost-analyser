import boto3
import datetime
import json

def lambda_handler(event, context):
    # Setup AWS clients
    ce = boto3.client('ce')
    s3 = boto3.client('s3')

    # Use yesterday and day before yesterday as date range
    today = datetime.date.today()
    end = today - datetime.timedelta(days=1)
    start = today - datetime.timedelta(days=2)

    # Convert to ISO format
    start_str = start.isoformat()
    end_str = end.isoformat()

    try:
        result = ce.get_cost_and_usage(
            TimePeriod={'Start': start_str, 'End': end_str},
            Granularity='DAILY',
            Metrics=['UnblendedCost'],
            GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
        )
    except Exception as e:
        print("Failed to fetch billing data:", e)
        raise e

    # Upload to S3
    try:
        s3.put_object(
            Bucket="billing-data-kavan",  # 🛑 Replace with actual bucket name
            Key=f"billing_data_{start_str}_to_{end_str}.json",
            Body=json.dumps(result, indent=2)
        )
    except Exception as e:
        print("Failed to upload to S3:", e)
        raise e

    return {
        'statusCode': 200,
        'body': f"Billing data from {start_str} to {end_str} uploaded to S3."
    }
