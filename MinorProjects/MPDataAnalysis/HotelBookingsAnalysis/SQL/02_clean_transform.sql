--CREATE SILVER TABLE TO CLEAN AND STANDARDIZE
CREATE TABLE SILVER_HOTEL_BOOKINGS (
    booking_id VARCHAR,
    hotel_id VARCHAR,
    hotel_city VARCHAR,
    customer_id VARCHAR,
    customer_name VARCHAR,
    customer_email VARCHAR,
    check_in_date DATE,
    check_out_date DATE,
    room_type VARCHAR,
    num_guests INTEGER,
    total_amount FLOAT,
    currency VARCHAR,
    booking_status VARCHAR
);
--CHECK FOR ERRORS IN BRONZE
SELECT customer_email
FROM BRONZE_HOTEL_BOOKING
WHERE customer_email NOT LIKE '%@%.%' OR customer_email IS NULL; -- WE SHOW 'invalid-email' (need to fix this)

--NEXT, CHECK FOR TOTAL AMOUNT < 0 
SELECT TOTAL_AMOUNT
FROM BRONZE_HOTEL_BOOKING
WHERE TOTAL_AMOUNT < 0; --WE SHOW negative total amounts, will need to fix this

--NEXT, CHECK FOR DATE RANGES WHERE CHECK IN SHOULD BE BEFORE CHECK OUT
SELECT check_in_date, check_out_date
FROM BRONZE_HOTEL_BOOKING
WHERE check_out_date < check_in_date;  --we see dates are not same format

--NEXT CHECKING BOOKING STATUS
SELECT DISTINCT booking_status
FROM BRONZE_HOTEL_BOOKING;  --WE SEE ONE ISSUE WITH NAMING 'Confirmeed', and a null

---INSERT DATA FROM BRONZE TO SILVER AND CLEAN IN THE SILVER THE ISSUES WE SAW IN THE BRONZE---
INSERT INTO SILVER_HOTEL_BOOKINGS
SELECT
    booking_id,
    hotel_id,
    INITCAP(TRIM(hotel_city)) AS hotel_city,
    customer_id,
    INITCAP(TRIM(customer_name)) AS customer_name,
    CASE
        WHEN customer_email LIKE '%@%.%' THEN LOWER(TRIM(customer_email))
        ELSE NULL
    END AS customer_email,
    TRY_TO_DATE(NULLIF(check_in_date, '')) AS check_in_date,
    TRY_TO_DATE(NULLIF(check_out_date, '')) AS check_out_date,
    room_type,
    num_guests,
    ABS(TRY_TO_NUMBER(total_amount)) AS total_amount,
    currency,
    CASE
        WHEN LOWER(booking_status) in ('confirmeeed', 'confirmd') THEN 'Confirmed'
        ELSE booking_status
    END AS booking_status
    FROM BRONZE_HOTEL_BOOKING
    WHERE
        TRY_TO_DATE(check_in_date) IS NOT NULL
        AND TRY_TO_DATE(check_out_date) IS NOT NULL
        AND TRY_TO_DATE(check_out_date) >= TRY_TO_DATE(check_in_date);

SELECT * FROM SILVER_HOTEL_BOOKINGS LIMIT 30;
