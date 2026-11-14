WITH market_prices AS (
    SELECT
        COMMODITY,
        STATE,
        DISTRICT,
        MARKET,
        AVG(MODAL_PRICE) AS AVG_MODAL_PRICE
    FROM {{ ref('stg_agricultural_prices') }}
    WHERE MODAL_PRICE IS NOT NULL
    GROUP BY COMMODITY, STATE, DISTRICT, MARKET
),

arbitrage AS (
    SELECT
        COMMODITY,
        STATE,
        DISTRICT,
        MARKET,
        AVG_MODAL_PRICE,
        MIN(AVG_MODAL_PRICE) OVER (
            PARTITION BY COMMODITY
        ) AS MIN_MARKET_PRICE,
        MAX(AVG_MODAL_PRICE) OVER (
            PARTITION BY COMMODITY
        ) AS MAX_MARKET_PRICE
    FROM market_prices
)

SELECT
    *,
    MAX_MARKET_PRICE - MIN_MARKET_PRICE AS PRICE_DIFFERENCE
FROM arbitrage
