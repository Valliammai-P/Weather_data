from sqlalchemy.sql import func

class WeatherStats(Base):
    __tablename__ = 'weather_stats'
    id = Column(Integer, primary_key=True)
    station_id = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    avg_max_temp = Column(Float)
    avg_min_temp = Column(Float)
    total_precipitation = Column(Float)
    __table_args__ = (UniqueConstraint('station_id', 'year', name='_station_year_uc'),)

Base.metadata.create_all(engine)

def calculate_stats():
    results = session.query(
        WeatherData.station_id,
        func.extract('year', WeatherData.date).label('year'),
        func.avg(WeatherData.max_temp).label('avg_max_temp'),
        func.avg(WeatherData.min_temp).label('avg_min_temp'),
        func.sum(WeatherData.precipitation).label('total_precipitation')
    ).group_by(
        WeatherData.station_id,
        func.extract('year', WeatherData.date)
    ).all()

    for result in results:
        stat_record = WeatherStats(
            station_id=result.station_id,
            year=result.year,
            avg_max_temp=result.avg_max_temp / 10.0 if result.avg_max_temp is not None else None,
            avg_min_temp=result.avg_min_temp / 10.0 if result.avg_min_temp is not None else None,
            total_precipitation=result.total_precipitation / 100.0 if result.total_precipitation is not None else None
        )
        session.merge(stat_record)
    session.commit()

calculate_stats()
