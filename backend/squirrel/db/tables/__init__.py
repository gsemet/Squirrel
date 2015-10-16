from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# force import all table here to register them, so they ll be created with the
# create_all function.
from squirrel.db.tables.currencies import TableCurrencies
from squirrel.db.tables.plugin_importers import TablePluginImporters
from squirrel.db.tables.portfolios import TablePortfolios
from squirrel.db.tables.stocks import TableStocks
from squirrel.db.tables.tickers import TableTickers
from squirrel.db.tables.ticks import TableTicks
from squirrel.db.tables.users import TableUsers

__all__ = [
    'TableCurrencies',
    'TablePluginImporters',
    'TablePortfolios',
    'TableStocks',
    'TableTickers',
    'TableTicks',
    'TableUsers',
]

[TableCurrencies, TablePluginImporters, TablePortfolios,
 TableStocks, TableTickers, TableTicks, TableUsers]
