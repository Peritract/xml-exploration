from os import mkdir
from os.path import isdir

from dotenv import dotenv_values
from boto3 import Session

if __name__ == "__main__":

    config = dotenv_values()
    aws_session = Session(aws_access_key_id=config["AWS_ACCESS_KEY_ID"],
                          aws_secret_access_key=config["AWS_SECRET_ACCESS_KEY"])

    s3 = aws_session.client("s3")

    if not isdir(config["DATA_FOLDER"]):
        mkdir(config["DATA_FOLDER"])
    
    s3.download_file(config["S3_BUCKET_NAME"],
                     config["SOURCE_FILE"],
                     f"./data/{config['DST_FILE']}")