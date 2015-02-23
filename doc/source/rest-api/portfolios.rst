.. _rest_api_endpoints_api_portfolios:

************************
/api/portfolios REST API
************************

Table of contents

Portfolios Endpoints
********************

Request::

    GET /api/portfolios/ HTTP/1.0

Reponse::

    HTTP/1.1 200 OK
    Content-Disposition: attachment
    Content-Type: application/json; charset=UTF-8

    [
        {
            "name": "This Portfolio",
            "description": "Description of the portfolios",
        },
    ]
