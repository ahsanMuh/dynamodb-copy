from tqdm import tqdm

from utils import create_boto_client
import config


db = create_boto_client('dynamodb')

src_tbl = config.src_tbl
dst_tbl = config.dst_tbl


def get_item_count(table_name):
  """
  Retrieves the approximate item count for a DynamoDB table.

  Args:
      table_name: Name of the DynamoDB table.
      client: Boto3 DynamoDB client object.

  Returns:
      The approximate item count as an integer.
  """
  response = db.describe_table(TableName=table_name)
  return response['Table']['ItemCount']


def copy_tbl():
    # Scan the source table and iterate over items
    src_tbl_count = get_item_count(src_tbl)
    dst_tbl_count = get_item_count(dst_tbl)
    print('Source table items count: ', src_tbl_count)
    print('Destination table items count: ', dst_tbl_count,
          end='\n\n')
    
    if src_tbl_count == dst_tbl_count:
        print('Looks like these tables are already copied!')
        return

    paginator = db.get_paginator('scan')
    i = 0 
    for page in paginator.paginate(TableName=src_tbl):
        print(f'Working on page-{i} ...')
        for item in tqdm(page['Items']):
            # Put the item in the destination table
            ret = db.put_item(TableName=dst_tbl, Item=item)

    print(f"Successfully copied items from '{src_tbl}' to '{dst_tbl}'.")


copy_tbl()