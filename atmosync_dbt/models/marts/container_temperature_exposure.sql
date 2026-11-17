
SELECT
    CONTAINER_ID,

    COUNT(*) AS TOTAL_READINGS,

    COUNT_IF(TEMPERATURE_C > 10) AS READINGS_ABOVE_10C,

    ROUND(
        100.0 * COUNT_IF(TEMPERATURE_C > 10)
        / NULLIF(COUNT(*), 0),
        2
    ) AS PERCENT_READINGS_ABOVE_10C,

    ROUND(AVG(TEMPERATURE_C), 2) AS AVG_TEMPERATURE_C,

    ROUND(
        AVG(
            LEAST(
                100,
                GREATEST(0, (TEMPERATURE_C - 10) * 5)
            )
        ),
        2
    ) AS DEMO_TEMPERATURE_DEGRADATION_SCORE

FROM {{ ref('stg_container_telemetry') }}

GROUP BY CONTAINER_ID
