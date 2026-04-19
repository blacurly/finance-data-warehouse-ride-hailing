SELECT
    r.ride_id,
    r.driver_id,
    r.city,
    r.distance_km,
    r.base_fare,
    p.amount,
    p.status,
    r.timestamp
FROM {{ ref('stg_rides') }} r
LEFT JOIN {{ ref('stg_payments') }} p
ON r.ride_id = p.ride_id
