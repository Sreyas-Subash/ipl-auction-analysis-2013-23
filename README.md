# ipl-auction-analysis-2013-23

Data was scraped from IPL's official website using 'BeautifulSoup' library. It was then cleaned and transformed using pandas library.

For these datasets, data warehouse to tables were created in Snowflake. The resultant player and team datasets were then uploaded to their respective tables using snowflake connector in Pycharm.

This relational database was then connected from snowflake to power bi for the creation of the following interactive dashboard.
