import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f"Event: {json.dumps(event)}")
    context_dict = {
        'request_id': context.aws_request_id,
        'function_name': context.function_name,
        'function_version': context.function_version,
        'invoked_function_arn': context.invoked_function_arn,
        'memory_limit_in_mb': context.memory_limit_in_mb,
        'remaining_time_in_millis': context.get_remaining_time_in_millis()
    }
    logger.info(f"Context: {json.dumps(context_dict, default=str)}")

    return {
        'statusCode': 200,
        'body': json.dumps('Logged successfully')
    }
