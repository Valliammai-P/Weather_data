import os
import glob
import logging
from sqlalchemy import create_engine, Column, Integer, String, Date, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the database model
Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    station_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    max_temp = Column(Integer)
    min_temp = Column(Integer)
    precipitation = Column(Integer)
    __table_args__ = (UniqueConstraint('station_id', 'date', name='_station_date_uc'),)

# Database connection
DATABASE_URI = 'postgresql://username:password@localhost/weather_db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Create the table
Base.metadata.create_all(engine)

def ingest_data(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            date, max_temp, min_temp, precipitation = line.strip().split('\t')
            if int(max_temp) == -9999:
                max_temp = None
            if int(min_temp) == -9999:
                min_temp = None
            if int(precipitation) == -9999:
                precipitation = None
            weather_record = WeatherData(
                station_id=os.path.basename(file_path).split('.')[0],
                date=date,
                max_temp=max_temp,
                min_temp=min_temp,
                precipitation=precipitation
            )
            session.merge(weather_record)
        session.commit()

def main():
    wx_data_dir = 'wx_data'
    file_paths = glob.glob(os.path.join(wx_data_dir, '*.txt'))
    for file_path in file_paths:
        logger.info(f'Starting ingestion for {file_path}')
        ingest_data(file_path)
        logger.info(f'Completed ingestion for {file_path}')

if __name__ == '__main__':
    main()
