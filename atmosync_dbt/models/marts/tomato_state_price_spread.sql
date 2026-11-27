-- Historical tomato price spread by state.
-- Provisional threshold excludes unusually low market averages.
-- Price spread does not represent actual arbitrage profit.

SELECT
    STATE,
    COUNT(*) AS MARKET_COUNT,
    MIN(AVG_MODAL_PRICE) AS LOWEST_PRICE,
    MAX(AVG_MODAL_PRICE) AS HIGHEST_PRICE,
    MAX(AVG_MODAL_PRICE) - MIN(AVG_MODAL_PRICE)
        AS STATE_PRICE_SPREAD
FROM {{ ref('market_arbitrage') }}
WHERE COMMODITY = 'Tomato'
AND AVG_MODAL_PRICE >= 100
GROUP BY STATE
HAVING COUNT(*) >= 2