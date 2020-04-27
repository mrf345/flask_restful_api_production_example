import os
from http import HTTPStatus
from flask import request
from flask_restx import abort
from datetime import datetime, timedelta

from ..constants import REQUESTS_LIMIT_PER_HOURS, REQUESTS_LIMIT_HOURS

limits = {}


def requests_limiter():
    if not os.getenv('TESTING'):
        limits.update({
            a: l for a, l in limits.items()
            if (l[0] + timedelta(hours=REQUESTS_LIMIT_HOURS)) > datetime.now()})
        address = request.remote_addr or '127.0.0.1'
        limit = limits.get(address, [datetime.now(), 1])

        if limit[1] >= REQUESTS_LIMIT_PER_HOURS:
            abort(message='Exceededs the amount of requests',
                  code=HTTPStatus.TOO_MANY_REQUESTS)

        if limit[1] >= REQUESTS_LIMIT_PER_HOURS:
            limit[1] += 1

        limits[address] = limit
