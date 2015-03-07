http://www.networkerror.org/component/content/article/44-googles-undocumented-finance-api.html


Google's Undocumented Finance API
Written by: NetworkError, on 18-05-2013 16:25
Last update: 18-05-2013 16:25
Published in: Public, Technical Wootness
Views: 11105

I've been playing around with the undocumented Google Finance API. It provides intra-day data for
the past 10 days and day-granularity data going back for years. Handy!

There are lots of web pages that attempt to describe how this thing works. I've pulled together a
bunch of data from them, as well as a few of my own observations. You can watch this thing in action
by popping open FireBug while messing about on with the google finance chart. It will make AJAX
requests to this API.

Here's an example URL to pull all historical data for GOOG at daily granularity:

::

    http://www.google.com/finance/getprices?q=GOOG&x=NASD&i=86400&p=40Y&f=d,c,v,k,o,h,l&df=cpct&auto=0&ei=Ef6XUYDfCqSTiAKEMg

What do all the parameters mean? Here's a partial list:

  q - Stock symbol
  x - Stock exchange symbol on which stock is traded (ex: NASD)
  i - Interval size in seconds (86400 = 1 day intervals)
  p - Period. (A number followed by a "d" or "Y", eg. Days or years. Ex: 40Y = 40 years.)
  f - What data do you want? d (date - timestamp/interval, c - close, v - volume, etc...)
  Note: Column order may not match what you specify here

  df - ??
  auto - ??
  ei - ??
  ts - Starting timestamp (Unix format). If blank, it uses today.

::

  http://www.google.com/finance/getprices?q=GOOG&x=NASD&i=86400&p=40Y&f=d,c,v,k,o,h,l&df=cpct&auto=0&ei=Ef6XUYDfCqSTiAKEMg

The output includes a header that describes the columns, timezone offset, and a few other
interesting bits of information. The data rows are basically CSV format.

One tricky bit with the first column (the date column) is the full and partial timestamps. The full
timestamps are denoted by the leading 'a'. Like this: a1092945600 The number after the 'a' is a Unix
timestamp. (Google it if you're not sure what it is.) The numbers without a leading 'a' are
"intervals". So, for example, the second row in the data set below has an interval of 1. You can
multiply this number by our interval size (a day, in this example) and add it to the last Unix
Timestamp. That gives you the date for the current row. (So our second row is 1 day after the first
row. Easy.)

Sample output format:

::

    EXCHANGE%3DNASDAQ
    MARKET_OPEN_MINUTE=570
    MARKET_CLOSE_MINUTE=960
    INTERVAL=86400
    COLUMNS=DATE,CLOSE,HIGH,LOW,OPEN,VOLUME,CDAYS
    DATA=
    TIMEZONE_OFFSET=-240
    a1092945600,100.335,104.06,95.96,100.01,22353092,1 <-- a##### denotes a unix time stamp.

    1,108.31,109.08,100.5,101.48,11429498,1 <-- The first column (1) * interval (1 day) + last full unix time stamp = date
    4,109.4,113.48,109.05,110.76,9140244,1
    5,104.87,111.6,103.57,111.24,7632224,1
    6,106,108,103.88,104.96,4599110,1
    7,107.91,107.95,104.66,104.95,3551168,1
    8,106.15,108.62,105.69,108.1,3108977,1
    11,102.01,105.49,102.01,105.49,2601620,1 <-- Note:  We jumped from 8 to 11.  We skipped 2 days.  This was a weekend.
    12,102.37,103.71,102.16,102.32,2463427,1

Hopefully this gives you what you need to build your own stock data-feed. Happy hacking!
