#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from suds.client import Client  # suds-jurko

def getSchedule(airline, flightno, dt):
  username = ''
  apiKey = ''
  url = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'
  api = Client(url, username=username, password=apiKey)

  results = api.service.AirlineFlightSchedules(
    airline=airline,
    flightno=flightno,
    startDate=int(dt.timestamp()),
    endDate=int(dt.timestamp()+86400),  # cap search at one day
    howMany=1
  )
  r = results.data[0]
  return {
    'ident': r.ident,
    'origin': r.origin,
    'departureTime': r.departuretime,
    'destination': r.destination,
    'arrivalTime': r.arrivaltime,
    # 'aircrafttype': r.aircrafttype  # excluded for now
  }


