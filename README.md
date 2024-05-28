# Dynamo-dopy:

Copy items from one dynamo db table to other.

## Steps:
1. Install requirements using `requirements.txt`.
2. Update `config.py` with your tables, and AWS secrets.
3. Run the script `copy_table.py`

**Note:** The destination table won't immediately show the update, after few minutes open the table in **Explore items** tab in the console.