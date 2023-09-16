from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Dataflow
from diagrams.aws.database import Database


# Create a Diagram instance named "data_extraction"
with Diagram("Data Extraction and Loading", show=False):  
    # Create a Cluster named "Source of Data"
    with Cluster("Source of Data"):
        sql_db = Database("SQL")
        nosql_db = Database("NoSQL")
        xml_files = Database("XML Files")

    # Create a component for the data extraction process
    extraction = Dataflow("Data Extraction")

    # Create a component for the target destination (data warehouse)
    warehouse = BigQuery("BigQuery")

    # Create a component for data loading
    loading = Dataflow("Data Loading")

    # Connect the data sources to the data extraction process
    sql_db >> extraction
    nosql_db >> extraction
    xml_files >> extraction

    # Connect the data extraction process to the data loading process
    extraction >> loading

    # Connect the data loading process to the data warehouse
    loading >> warehouse

# Render the diagram (if "show=False" is removed, the diagram will be displayed)
# data_extraction.render()




