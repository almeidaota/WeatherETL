create table weatherapi.forecast_data 
    (id int not null auto_increment, 
     day datetime, 
     temp float,
     feels_like float, 
     humidity float, 
     dew_point float, 
     uvi float, 
     clouds int, 
     visibility int, 
     wind_deg float, 
     primary key (id));

create table weatherapi.historical_data 
    (id int not null auto_increment, 
     day datetime, 
     temp float,
     feels_like float, 
     humidity float, 
     dew_point float, 
     uvi float, 
     clouds int, 
     visibility int, 
     wind_deg float, 
     primary key (id));

