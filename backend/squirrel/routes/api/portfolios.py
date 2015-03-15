from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import json

from squirrel.routes import app


@app.route("/api/portfolios", methods=['GET'])
def route_portfolios(request):
    request.setHeader('Content-Type', 'application/json')

    data = [
        {
            'name': "CTO Fortuneo",
            'broker': 'Fortuneo',
            'description': "Compte Titre Ordinaire (uniq. Euronext Paris)",
            'class:': 'Actions',
            'type': 'CTO',
            'creation_date': '01/03/2014',
            'deposit': {
                'value': 800.00,
                'currency': 'euro',
            },
            'supports': {
                'quotes': {
                    'value': 0,
                    'currency': 'euro',
                },
                'bonds':  {
                    'value': 755.90,
                    'currency': 'euro',
                },
            },
            'valorisation': {
                'value': 755.90,
                'currency': 'euro',
            },
            'profit': {
                'value': -44.10,
                'currency': 'euro',
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
