
from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Dataflow
from diagrams.aws.database import Database
from diagrams.azure.database import SQLDatawarehouse
from diagrams.aws.analytics import Analytics

# Create a Diagram instance named "data_sources"
with Diagram("ETL Process", show=False):  # "show=False" hides the diagram display, you can remove it if you want to display the diagram

    # Create a Cluster named "Source of Data"
    with Cluster("Source of Data"):
        sql_db = Database("SQL")
        nosql_db = Database("NoSQL")
        xml_files = Database("XML Files")

# Render the diagram (if "show=False" is removed, the diagram will be displayed)
# data_sources.render()

    extraction=Dataflow('Data Extraction')
    load_data=SQLDatawarehouse('Data Loading to Warehouse')
    analytics=Analytics('Analyze')


    sql_db>>extraction
    nosql_db>>extraction
    xml_files>>extraction

    extraction>>load_data
    load_data>>analytics





 
