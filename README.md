
## Class CryptoCSV: scrapes a given crypto-currency's <b>daily</b> historical data from coinmarketcap.com and writes to .csv - 2013 to present
<br><br>
All available data from <b>April 28th 2013 to the present day</b> will be added into the .csv file
<br><br>
When the script finishes, a .csv file will be written to the current working directory:<br>
&nbsp; &nbsp;bitcoin20180524.csv
<br><br>
Example Usage:
<br>
<code style=">
python3 crypto_csv_writer.py -c litecoin
</code>
<br>
Simply replace the -c argument with your desired crypto-currency
<br>
It should run on any system with python3 and requests module installed -- tested on Ubuntu
<br><br>
This was developed on Ubuntu 16.04.4 LTS.
<hr>
<b>Author: James Loye Colley  18NOV2018</b><br><br>
Example 1:<br>
<img src="https://github.com/rootVIII/crypto_csv_writer/blob/master/screenshot1.png" alt="example1" height="675" width="950"><hr>
Example 2:<br>
<img src="https://github.com/rootVIII/crypto_csv_writer/blob/master/screenshot2.png" alt="example2" height="1100" width="900">
