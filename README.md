
<a name="readme-top"></a>

  <h3 align="center">Smart-City Pipeline</h3>

  <p align="center">
    Implementation of a End To End Data-Pipeline as Part of my Data Engineering Journey!
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


This pipeline project leverages generated vehicular, weather, emergency, gps and traffic data, which is then stored in Kafka and managed by Apache Zookeeper (controlling the Kafka brokers). 

Nextly, there is a consumer with Apache Spark, that is listening to events from Kafka and takes in data, aggregates and processes it. This part is containerized by Docker. 

After that the data is seamlessly transferred into AWS, specifically S3 Buckets. 
AWS Glue, as an ETL service, is then used to prepare and load the data for analytics. The glue crawlers fetch metadata from the data inside the S3 Buckets and stored it in the Data Catalogue. 

In the next step Amazon Redshift, as a data warehouse cloud service is storing the processed data from the S3 buckets. Amazon Athena is additionally used to directly analyze data from the S3 buckets with SQL.
Lastly, the data is analyzed with Power BI/Tableau.

Here you can see the overview of the pipeline structure:

![dateeng](https://github.com/NicoSchultze/Smart-City-Pipeline/assets/87664933/838ffdaa-f8a3-486e-a247-f3dc7d3f7d9a)



### Built With

* Docker
* Kafka
* Zookeeper
* Spark
* AmazonS3 Buckets
* AWS Glue
* Athena



<!-- USAGE EXAMPLES -->
## Usage

This project is used with self-generated vehicular data, since it focuses on the pipeline rather than multiple API accesses. This however would come closer to a real-world application, where API data is used (weather, vehicular, location, emergency and so on).
It really applies to any kind of data, where batch streaming is not enough but real time streaming is needed. This was the target and goal of this project. To build a pipeline that handles real time streamed data with a Docker Image of Kafka, Spark Workers and lastly the AWS S3 Bucket Streaming - to then work with the data in the cloud or databases.


<!-- ROADMAP -->
## Roadmap

- [x] Dockerize Zookeeper and Kafka
- [x] Produce and prepare data for streaming to Kafka
- [x] Dockerize Spark Master and Worker
- [x] Schema creation and spark preprocessing
- [x] Seamless AWS Streaming



<!-- CONTACT -->
## Contact

Nico Schultze - nico.schultze97@gmail.com

Project Link: https://github.com/NicoSchultze/Smart-City-Pipeline


<p align="right">(<a href="#readme-top">back to top</a>)</p>




