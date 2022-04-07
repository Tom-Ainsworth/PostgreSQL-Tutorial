from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# 3 /// mean that the database is hosted locally in our environment
db = create_engine('postresql:///chinook')

meta = MetaData(db)

