# AWS
# Project-1:
    # aws-glue:
      Project description: 
          1. An ETL pipeline, performing transformations, storing processed data into Redshift and raw data back to target S3 bucket.
          2. Connect Athena to Glue catalog performing basic data analysis.
        This folder contains a programmatic approach of using AWS services 

     Project workflow:
         1. Files are uploaded into S3 source bucket
         2. Lambda function, when a s3 object lands into the source bucket triggers the Glue job.
         3. The Glue crawler performs transformation on the data using Python and Pyspark.
         4. The raw data is stored back into target S3 bucket, whereas the transformed data is stored in Redshift.
