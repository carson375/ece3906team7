CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR(32) NOT NULL,
    user_password VARCHAR(32)
    -- Add checks for valid values
);

CREATE TABLE flight(
    flight_no INTEGER PRIMARY KEY,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES user_id(user_id)
);

CREATE TABLE point(
    flight_no INTEGER,
    x_coord float,
    y_coord float,
    sig_val float,
    FOREIGN KEY (flight_no) REFERENCES flight(flight_no)
);
