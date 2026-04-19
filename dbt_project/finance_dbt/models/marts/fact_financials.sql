SELECT
    ride_id,
    driver_id,
    city,
    timestamp,

    amount AS gross_booking_value,

    CASE 
        WHEN status = 'success' THEN amount
        ELSE 0
    END AS valid_gbv,

    CASE 
        WHEN status = 'success' THEN amount * 0.2
        ELSE 0
    END AS platform_revenue,

    CASE 
        WHEN status = 'success' THEN amount * 0.8
        ELSE 0
    END AS driver_payout

FROM {{ ref('fact_rides') }}
