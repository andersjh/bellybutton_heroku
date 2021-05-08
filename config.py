
# database = "sqlite"
# database = "mssql"
# database = "mongo"
database = "postgres_local"
# database = "postgres_heroku"

connect_string = ""

if database == "sqlite":
    connect_string = "sqlite:///belly_button.db"
elif database == "mssql":    
    connect_string = "mssql+pymssql://user:pass@server:port/database"
elif database == "postgres_local":
    connect_string = "postgresql+psycopg2://postgres:pgadmin@localhost/bbutton"
elif database == "postgres_heroku":
    connect_string = "postgresql+psycopg2://user:pass@server/database"    
elif database == "mongo":        
    connect_string = "mongodb+srv://user:pass@mongo-server/?retryWrites=true&w=majority"
