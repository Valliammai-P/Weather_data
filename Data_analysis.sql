CREATE TABLE weather_stats (
    id SERIAL PRIMARY KEY,
    station_id VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    avg_max_temp FLOAT,
    avg_min_temp FLOAT,
    total_precipitation FLOAT,
    UNIQUE(station_id, year)
);
