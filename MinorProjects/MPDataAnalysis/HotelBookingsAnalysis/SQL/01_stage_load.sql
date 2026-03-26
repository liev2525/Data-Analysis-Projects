CREATE DATABASE HOTEL_DB;

--CREATE FILE FORMAT
CREATE OR REPLACE FILE FORMAT FF_CSV
    TYPE = 'CSV'
    FIELD_OPTIONALLY_ENCLOSED_BY = '"' --if any field has quotes then ignore quotes
    SKIP_HEADER = 1   --do not need headings imported here
    NULL_IF = ('NULL', 'null', '')

--CREATE WAITING ROOM FOR FILE (HOLD IN STAGE UNTIL WE PULL INTO FILE)
CREATE OR REPLACE STAGE STG_HOTEL_BOOKINGS
    FILE_FORMAT = FF_CSV;

-- TO CREATE THE BRONZE TABLE > Follow sequence of columns from spreadsheet
CREATE TABLE BRONZE_HOTEL_BOOKING (
    booking_id STRING,
    hotel_id STRING, 
    hotel_city STRING, 
    customer_id STRING, 
    customer_name STRING, 
    customer_email STRING, 
    check_in_date STRING, 
    check_out_date STRING, 
    room_type STRING, 
    num_guests STRING, 
    total_amount STRING, 
    currency STRING, 
    booking_status STRING 
    );
--COPY INTO BRONZE TABLE
    COPY INTO BRONZE_HOTEL_BOOKING
    FROM @STG_HOTEL_BOOKINGS
    FILE_FORMAT = (FORMAT_NAME = FF_CSV)
    ON_ERROR = 'CONTINUE';
--TEST
SELECT * FROM BRONZE_HOTEL_BOOKING LIMIT 50
