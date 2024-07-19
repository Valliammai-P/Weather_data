CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    station_id VARCHAR(50) NOT NULL,
    date DATE NOT NULL,
    max_temp INTEGER,
    min_temp INTEGER,
    precipitation INTEGER,
    UNIQUE(station_id, date)
);
