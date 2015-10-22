# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import arrow
import json

from squirrel.routes import app
from squirrel.routes.api import getSingleArgFromRequest
from squirrel.services.config import Config


@app.route("/api/portfolios/a", methods=['GET'])
def route_portfolios_all(request):
    request.setHeader('Content-Type', 'application/json')

    data = {
        'total_balance': {
            'v': 800.00,
            'c': 'euro',
        },
        'total_invested': {
            'v': 300.00,
            'c': 'euro',
        },
        'total_gains': {
            'v': 400.00,
            'c': 'euro',
        },
        # dividents is already in gains
        'dividends': {
            'v': 400.00,
            'c': 'euro',
        },
        'deposit': {
            'v': 400.00,
            'c': 'euro',
        },
        'withdrawals': {
            'v': 100.00,
            'c': 'euro',
        },
        'other': {
            'v': 0.00,
            'c': 'euro',
        },
        'allocation': {
            'bonds': {
                'v': 700.00,
                'c': 'euro',
            },
            'bonds_pourc':  70,
            'stocks': {
                'v': 100.00,
                'c': 'euro',
            },
            'stock_pourc':  10,
            'gold': {
                'v': 100.00,
                'c': 'euro',
            },
            'gold_pourc':  10,
            'real_estate': {
                'v': 100.00,
                'c': 'euro',
            },
            'real_estate_pourc':  10,
        }
    }

    return json.dumps(data)


@app.route("/api/portfolios/p", methods=['GET'])
def route_portfolios(request):
    request.setHeader('Content-Type', 'application/json')

    data = [
        {
            'id': 1,
            'name': "CTO Fortuneo",
            'broker': 'Fortuneo',
            'description': "Compte Titre Ordinaire (uniq. Euronext Paris)",
            'class:': 'Actions',
            'type': 'CTO',
            'creation_date': arrow.get('01/03/2014', 'DD/MM/YYYY').format("YYYY-MM-DD"),
            'deposit': {
                'v': 800.00,
                'c': 'euro',
            },
            'supports': {
                'quotes': {
                    'v': 0,
                    'c': 'euro',
                },
                'bonds':  {
                    'v': 755.90,
                    'c': 'euro',
                },
            },
            'balance': {
                'v': 755.90,
                'c': 'euro',
            },
            'profit': {
                'v': -44.10,
                'c': 'euro',
            },
            'gain': {
                'percentage': -5.5,
            },
            'gain_annualisation': {
                'average': {
                    'percentage': -5.5
                },
                "years": {
                    2014: {
                        'percentage': -5.5
                    },
                }
            }
        }
    ]
    return json.dumps(data)


def _getAccountTypes():
    data = []
    if not Config().settings.country.fr:
        return None
    for group_name, group_val in Config().settings.country.fr.asset_types.items():
        for name in group_val:
            data.append((group_name, name))
    data = sorted(data, key=lambda x: '{}{}'.format(x[0], x[1]))
    return data


@app.route("/api/portfolios/types", methods=['GET'])
def route_portfolios_types(request):
    request.setHeader('Content-Type', 'application/json')
    return json.dumps(_getAccountTypes())


@app.route("/api/portfolios/p/<path:portfolio_id>", methods=['GET'])
def route_portfolios_get(request, portfolio_id):
    request.setHeader('Content-Type', 'application/json')
    details = getSingleArgFromRequest(request, "details", False)

    data = {
        'id': portfolio_id,
        'name': "CTO Fortuneo",
        'broker': 'Fortuneo',
        'description': "Actions Euronext uniquement",
        'class:': 'Actions',
        'type': {
            'id': 123,
            'short': 'CTO',
            'long': 'Compte Titre Ordinaire (CTO)',
        },
        'creation_date': '01/03/2014',
        'supports': {
            'quotes': {
                'v': 0,
                'c': 'euro',
            },
            'bonds':  {
                'v': 755.90,
                'c': 'euro',
            },
        },
        'portfolio_value': {
            'balance': {
                'v': 755.90,
                'c': 'euro',
            },
            'profit': {
                'v': -44.10,
                'c': 'euro',
            },
            'gain': {
                'percentage': -5.5,
            },
            'gain_annualisation': {
                'average': {
                    'percentage': -5.5
                },
                "years": {
                    2014: {
                        'percentage': -5.5
                    },
                }
            },
        },
        'invested': {
            'total': {
                'v': 850,
                'c': 'euro',
            },
            'deposit': {
                'v': 750,
                'c': 'euro',
            },
            'withdrawals': {
                'v': 100,
                'c': 'euro',
            },
            'other': {
                'v': 0,
                'c': 'euro',
            },
        },
        'earned': {
            'total': {
                'v': 105,
                'c': 'euro',
            },
            'market_change': {
                'v': 70,
                'c': 'euro',
            },
            'dividends': {
                'v': 20,
                'c': 'euro',
            },
            'other': {
                'v': 5,
                'c': 'euro',
            },
        },
        'cash': {
            'deposit': {
                'v': 5254,
                'c': 'euro',
            },
            'balance': {
                'v': 5764,
                'c': 'euro',
            },
            'gain': {
                'percent': 2,
                'value': {
                    'v': 5,
                    'c': 'euro',
                },
            },
        }
    }
    if details:
        data.update({
            'details': [{
                'id': 123,
                'name': 'GDF',
                'shares': 78,
                'ticker': {
                    'source': 'GoogleFinance',
                    'exchange': 'NYSE',
                    'symbol': 'GDF',
                },
                'balance': {
                    'v': 650.90,
                    'c': 'euro',
                },
                'return': {
                    'percent': 3.3,
                    'overall': {
                        'v': 53,
                        'c': 'euro',
                    }
                },
                'last_price': {
                    'v': '123.0',
                    'c': 'euro',
                },
                'cost_basis': {
                    'overall': {
                        'v': 88.0,
                        'c': 'euro',
                    },
                    'unit': {
                        'v': 12,
                        'c': 'euro',
                    },
                },
                'gain': {
                    'percent': 12.5,
                    'overall': {
                        'v': 55,
                        'c': 'euro',
                    },
                    'unit': {
                        'c': 0.2,
                        'v': 'euro',
                    }
                },
            }, {
                'id': 456,
                'name': 'Orange',
                'shares': 78,
                'ticker': {
                        'source': 'GoogleFinance',
                        'exchange': 'NYSE',
                        'symbol': 'FP',
                },
                'balance': {
                    'v': 170.90,
                    'c': 'euro',
                },
                'return': {
                    'percent': 3.3,
                    'overall': {
                        'v': 53,
                        'c': 'euro',
                    }
                },
                'last_price': {
                    'v': '123.0',
                    'c': 'euro',
                },
                'cost_basis': {
                    'overall': {
                        'v': 88.0,
                        'c': 'euro',
                    },
                    'unit': {
                        'v': 12,
                        'c': 'euro',
                    },
                },
                'gain': {
                    'percent': 12.5,
                    'overall': {
                        'v': 55,
                        'c': 'euro',
                    },
                    'unit': {
                        'c': 0.2,
                        'v': 'euro',
                    }
                },
            }, {
                'id': 789,
                'name': 'Total',
                'shares': 78,
                'ticker': {
                        'source': 'GoogleFinance',
                        'exchange': 'NYSE',
                        'symbol': 'FP',
                },
                'balance': {
                    'v': 90.10,
                    'c': 'euro',
                },
                'return': {
                    'percent': 3.3,
                    'overall': {
                        'v': 53,
                        'c': 'euro',
                    }
                },
                'last_price': {
                    'v': 123.0,
                    'c': 'euro',
                },
                'cost_basis': {
                    'overall': {
                        'v': 88.0,
                        'c': 'euro',
                    },
                    'unit': {
                        'v': 12,
                        'c': 'euro',
                    },
                },
                'gain': {
                    'percent': 12.5,
                    'overall': {
                        'v': 55,
                        'c': 'euro',
                    },
                    'unit': {
                        'c': 0.2,
                        'v': 'euro',
                    }
                },
            },
            ],
            'valorisation_history': {
                'c': 'euro',
                'history': [
                    {'e': 1422921600000, 'd': "02/03/2015", 'v': 485},
                    {'e': 1423008000000, 'd': "02/04/2015", 'v': 488},
                    {'e': 1423094400000, 'd': "02/05/2015", 'v': 490},
                    {'e': 1423180800000, 'd': "02/06/2015", 'v': 493},
                    {'e': 1423440000000, 'd': "02/09/2015", 'v': 493},
                    {'e': 1423526400000, 'd': "02/10/2015", 'v': 491},
                    {'e': 1424044800000, 'd': "02/16/2015", 'v': 495},
                    {'e': 1424217600000, 'd': "02/18/2015", 'v': 499},
                    {'e': 1424390400000, 'd': "02/20/2015", 'v': 503},
                    {'e': 1424476800000, 'd': "02/21/2015", 'v': 503},
                    {'e': 1424649600000, 'd': "02/23/2015", 'v': 503},
                    {'e': 1424736000000, 'd': "02/24/2015", 'v': 503},
                    {'e': 1424822400000, 'd': "02/25/2015", 'v': 503},
                    {'e': 1424908800000, 'd': "02/26/2015", 'v': 499},
                    {'e': 1425254400000, 'd': "03/02/2015", 'v': 503},
                    {'e': 1425340800000, 'd': "03/03/2015", 'v': 501},
                    {'e': 1425427200000, 'd': "03/04/2015", 'v': 503},
                    {'e': 1425513600000, 'd': "03/05/2015", 'v': 504},
                    {'e': 1425600000000, 'd': "03/06/2015", 'v': 508},
                    {'e': 1425859200000, 'd': "03/09/2015", 'v': 507},
                    {'e': 1425945600000, 'd': "03/10/2015", 'v': 503},
                    {'e': 1426032000000, 'd': "03/11/2015", 'v': 507},
                    {'e': 1426204800000, 'd': "03/13/2015", 'v': 510},
                    {'e': 1426464000000, 'd': "03/16/2015", 'v': 512},
                    {'e': 1426550400000, 'd': "03/17/2015", 'v': 510},
                    {'e': 1426723200000, 'd': "03/19/2015", 'v': 508},
                    {'e': 1426896000000, 'd': "03/21/2015", 'v': 514},
                    {'e': 1427068800000, 'd': "03/23/2015", 'v': 513},
                    {'e': 1427155200000, 'd': "03/24/2015", 'v': 516},
                    {'e': 1427241600000, 'd': "03/25/2015", 'v': 514},
                    {'e': 1427328000000, 'd': "03/26/2015", 'v': 514},
                    {'e': 1427414400000, 'd': "03/27/2015", 'v': 502},
                    {'e': 1427932800000, 'd': "04/02/2015", 'v': 508},
                    {'e': 1428105600000, 'd': "04/04/2015", 'v': 509},
                    {'e': 1428451200000, 'd': "04/08/2015", 'v': 517},
                ]
            },
        })
    return json.dumps(data)
