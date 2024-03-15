CREATE DATABASE IF NOT EXISTS stock_alertify;

CREATE TABLE alerts
(
    id                       UUID            DEFAULT gen_random_uuid() PRIMARY KEY,
    name                     STRING NOT NULL,
    symbol                   STRING NOT NULL,
    threshold_price float NOT NULL,
    created_at               DATE   NOT NULL DEFAULT now()
);

CREATE TABLE alert_rules
(
    id                       UUID            DEFAULT gen_random_uuid() PRIMARY KEY,
    name                     STRING NOT NULL,
    symbol                   STRING NOT NULL,
    threshold_price          float NOT NULL,
    is_deleted               BOOLEAN NULL,
    created_at               DATE   NOT NULL DEFAULT now()
);