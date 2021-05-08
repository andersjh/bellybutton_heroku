
# database = "sqlite"
# database = "mssql"
# database = "mongo"
# database = "postgres_local"
database = "postgres_heroku"

connect_string = ""

if database == "sqlite":
    connect_string = "sqlite:///belly_button.db"
elif database == "mssql":    
    connect_string = "mssql+pymssql://user:pass@server:port/database"
elif database == "postgres_local":
    connect_string = "postgresql+psycopg2://postgres:pgadmin@localhost/bbutton"
elif database == "postgres_heroku":
    connect_string = "postgresql+psycopg2://iolwoflbsdsqcb:23bf159f60dad615f04e2aaa12af912a9cb32660ace95e21bd29996be47fa88f@ec2-107-22-83-3.compute-1.amazonaws.com:5432/d9qgapp7v0mn77"    
elif database == "mongo":        
    connect_string = "mongodb+srv://user:pass@mongo-server/?retryWrites=true&w=majority"
