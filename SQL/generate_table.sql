CREATE TABLE orders (
    order_id      SERIAL PRIMARY KEY,
    customer_name TEXT NOT NULL,
    product_name  TEXT NOT NULL,
    quantity      INT  NOT NULL,
    price_each    NUMERIC(10,2) NOT NULL,
    order_date    DATE NOT NULL
);


INSERT INTO orders (customer_name, product_name, quantity, price_each, order_date)
SELECT
    'Customer ' || gs AS customer_name,
    (ARRAY['Laptop','Headphones','Mouse','Keyboard','Monitor','Printer'])[floor(random()*6 + 1)],
    (floor(random()*10 + 1))::INT AS quantity,
    round((20 + random()*980)::numeric, 2) AS price_each,  
    CURRENT_DATE - (floor(random()*365))::INT AS order_date
FROM generate_series(1, 500) AS gs;
