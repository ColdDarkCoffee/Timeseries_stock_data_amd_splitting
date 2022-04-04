import time
import datetime
import pandas as pd


from datetime import datetime as date_data # must rename because "scaping stock data wont 
from datetime import timedelta             # work because the need of "datetime.datetime"
# since we are getting information at the end of the data "Closing price" 
# we are going to get yesterdays date to be the most recent date 
yesterday = datetime.datetime.strftime(datetime.datetime.now() - timedelta(1), '%Y-%m-%d')
