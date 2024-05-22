%%bigquery recency

SELECT
days_since_last_purchase
FROM
`online_retail.online_reatail_clv_ml`

recency.describe()

recency.hist(bins=100);
