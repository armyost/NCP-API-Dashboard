from sqlalchemy import text

class apiDao:
    def __init__(self, database):
        self.db=database

    def insert_data_serverInstance(self, row):
        self.db.execute(text("""
        INSERT INTO testtable (
            val1,
            val2,
            val3,
            val4,
            val5,
            val6
        ) VALUES (
            :serverInstanceNo,
            :serverName,
            :cpuCount,
            :memorySize,
            :serverDescription,
            :serverDescription
        )
        """),
        {   'serverInstanceNo': row['serverInstanceNo'],
            'serverName' : row['serverName'],
            'cpuCount' : row['cpuCount'],
            'memorySize' : row['memorySize'],
            'serverDescription' : row['serverDescription']} )