
CREATE TABLE IF NOT EXISTS zhaav.iranian_plate_generated(
						chap INT
						char_en VARCHAR(120),
						char_fa VARCHAR(120),
						rast INT,
						car_model VARCHAR(120),
						age INT,
						first_name VARCHAR(120),
                        last_name VARCHAR(120)
						) 
                     UNIQUE KEY(chap,char_en,char_fa,rast,car_model,age,first_name,last_name)
                     DISTRIBUTED BY HASH(chap) BUCKETS 20