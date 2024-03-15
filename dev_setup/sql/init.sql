CREATE DATABASE IF NOT EXISTS stock_alertify;

USE stock_alertify;
CREATE TABLE IF NOT EXISTS alerts
(
    id                       UUID            DEFAULT gen_random_uuid() PRIMARY KEY,
    name                     STRING NOT NULL,
    symbol                   STRING NOT NULL,
    threshold_price float NOT NULL,
    created_at               DATE   NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS alert_rules
(
    id                       UUID            DEFAULT gen_random_uuid() PRIMARY KEY,
    name                     STRING NOT NULL,
    symbol                   STRING NOT NULL,
    threshold_price          float NOT NULL,
    is_deleted               BOOLEAN NULL,
    created_at               DATE   NOT NULL DEFAULT now()
);


INSERT INTO alert_rules (name, symbol, threshold_price) VALUES ('Apple Inc', 'AAPL', 173.00), ('Microsoft Corp', 'MSFT', 425.22),
                                                               ('Alphabet Inc Class C', 'GOOG', 144.34), ('Amazon.com Inc', 'AMZN', 178.75),
                                                               ('Meta Platforms Inc', 'META', 491.83);