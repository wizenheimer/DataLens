def generate_dialect(category=None):
    # Dialect names include the identifying name of the SQLAlchemy dialect, a name such as sqlite, mysql, postgresql, oracle, or mssql
    if category is None:
        dialect = "DBAPI"
    elif category == "MySQL":
        dialect = "mysql"
    elif category == "PostgreSQL" or category == "Amazon Redshift":
        dialect = "postgresql"
    elif category == "Oracle":
        dialect = "oracle"
    elif category == "Microsoft SQL Server":
        dialect = "mssql"
    else:
        raise ValueError("Unsupported Category")

    return dialect


def generate_driver(dialect):
    driver = ""
    if dialect == "mssql":
        driver = "pyodbc"
    return driver


def parse_password(password=None):
    if password is None:
        return ValueError("Password must be specified")

    import urllib.parse

    return urllib.parse.quote_plus(password)


def generate_config_url(**kwargs):
    """
    dialect+driver://username:password@host:port/database
    """
    dialect = generate_dialect(kwargs.get("category", None))
    driver = generate_driver(dialect)
    username = kwargs.get("username", None)
    password = parse_password(kwargs.get("password", None))
    host = kwargs.get("host", None)
    port = kwargs.get("port", None)
    database_name = kwargs.get("database_name", None)
    return f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database_name}"


def generate_schema(url):
    """
        {
        "schema1": {
            "table1": {
                "column1": {"type": "type1", "name": "column1"},
                "column2": {"type": "type2", "name": "column2"},
                ...
            },
            "table2": {
                "column1": {"type": "type1", "name": "column1"},
                "column2": {"type": "type2", "name": "column2"},
                ...
            },
            ...
        },
        "schema2": {
            "table1": {
                "column1": {"type": "type1", "name": "column1"},
                "column2": {"type": "type2", "name": "column2"},
                ...
            },
            "table2": {
                "column1": {"type": "type1", "name": "column1"},
                "column2": {"type": "type2", "name": "column2"},
                ...
            },
            ...
        },
        ...
    }

    """
    from sqlalchemy import inspect, create_engine

    engine = create_engine(url)
    inspector = inspect(engine)
    schemas = inspector.get_schema_names()

    schema_dict = {}

    for schema in schemas:
        schema_tables = {}
        for table_name in inspector.get_table_names(schema=schema):
            columns = {}
            for column in inspector.get_columns(table_name, schema=schema):
                columns[column["name"]] = {
                    "name": column["name"],
                    "type": column["type"],
                }
            schema_tables[table_name] = columns
        schema_dict[schema] = schema_tables

    return schema_dict


def run_query(raw_sql, url):
    """Runs a query against the database and returns pandas dataframe"""
    from sqlalchemy.sql import text
    from sqlalchemy import create_engine
    import pandas as pd

    # create a sqlalchemy engine
    engine = create_engine(url)

    # execute the raw sql query using sqlalchemy's text function
    query = text(raw_sql)
    result_proxy = engine.execute(query)

    # convert the result proxy into a pandas dataframe
    df = pd.DataFrame(result_proxy.fetchall(), columns=result_proxy.keys())

    # close the database connection
    result_proxy.close()

    return df
