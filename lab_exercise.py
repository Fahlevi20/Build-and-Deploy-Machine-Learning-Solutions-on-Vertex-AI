%%bigquery recency

SELECT
days_since_last_purchase
FROM
`online_retail.online_reatail_clv_ml`

recency.describe()

recency.hist(bins=100);

%%bigquery frequency
SELECT
n_purchases
FROM
  `online_retail.online_retail_clv_ml`

frequency.describe()
frequency.hist(bins=100)
