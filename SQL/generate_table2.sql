-- 1. Customers
CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- 2. Drivers
CREATE TABLE driver (
    driver_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- 3. Payment methods  (must exist before rides)
CREATE TABLE payment_method (
    payment_method_id SERIAL PRIMARY KEY,
    method_name TEXT NOT NULL,
    eligible BOOLEAN DEFAULT TRUE   -- TRUE = counts for loyalty
);

-- 4. Rides (references customer, driver, payment_method)
CREATE TABLE rides (
    ride_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customer(customer_id),
    driver_id INT REFERENCES driver(driver_id),
    ride_date DATE NOT NULL,
    payment_method_id INT REFERENCES payment_method(payment_method_id)
);

-- 5. Ratings (references rides)
CREATE TABLE ratings (
    rating_id SERIAL PRIMARY KEY,
    ride_id INT REFERENCES rides(ride_id),
    customer_id INT REFERENCES customer(customer_id),
    rating INT CHECK (rating BETWEEN 1 AND 5)
);

-- Customers
INSERT INTO customer (name)
SELECT 'Customer ' || g FROM generate_series(1,50) g;

-- Drivers
INSERT INTO driver (name)
SELECT 'Driver ' || g FROM generate_series(1,10) g;

-- Payment methods
INSERT INTO payment_method (method_name, eligible) VALUES
('Credit Card', TRUE),
('Wallet', TRUE),
('Cash', FALSE);  -- Cash not eligible for loyalty

-- 100 random rides
INSERT INTO rides (customer_id, driver_id, ride_date, payment_method_id)
SELECT
    floor(random()*50 + 1)::INT,
    floor(random()*10 + 1)::INT,
    CURRENT_DATE - (floor(random()*30))::INT,
    floor(random()*3 + 1)::INT
FROM generate_series(1,100);

-- Ratings for roughly half the rides
INSERT INTO ratings (ride_id, customer_id, rating)
SELECT
    ride_id,
    r.customer_id,
    floor(random()*5 + 1)::INT
FROM rides r
WHERE random() < 0.5;

