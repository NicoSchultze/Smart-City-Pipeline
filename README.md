This pipeline project leverages different types of structured and unstructured data, which is then stored in Kafka and managed by Apache Zookeeper (controlling the Kafka brokers). 
Nextly, there is a consumer with Apache Spark, that is listening to events from Kafka and takes in data, aggregates and processes it. This part is containerized by Docker. After that the data is seamlessly transferred into AWS, specifically S3 Buckets. 
AWS Glue, as an ETL service, is then used to prepare and load the data for analytics. The glue crawlers fetch metadata from the data inside the S3 Buckets and stored it in the Data Catalogue. 
In the next step Amazon Redshift, as a data warehouse cloud service is storing the processed data from the S3 buckets. Amazon Athena is additionally used to directly analyze data from the S3 buckets with SQL.
Lastly, the data is analyzed with Power BI/Tableau.

