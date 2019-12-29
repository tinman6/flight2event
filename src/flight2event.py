#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from aadict import aadict
import requests
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


def getAirports(airline, flightno):
  # flightaware uses icao codes instead of iata. using flightstats to
  # supplement data
  flight_url = 'https://www.flightstats.com/v2/api-next/flight-tracker/%s/%s/%s/%s/%s'
  # todo: flightstats only have flight data for the week or so. using an
  #       arbitrary date. this is not perfect since not all flights are daily,
  #       and some flights are seasonal
  d = datetime.date.today()
  r= requests.get(url=(flight_url %
                       (airline, flightno, d.year, d.month, d.day)))
  a = aadict.d2ar(r.json()['data'])
  return {
    'origin': {
      'name': a.departureAirport.name,
      'iata': a.departureAirport.iata,
      'terminal': a.departureAirport.terminal,
      'timezone': a.departureAirport.timeZoneRegionName
    },
    'destination': {
      'name': a.arrivalAirport.name,
      'iata': a.arrivalAirport.iata,
      'terminal': a.arrivalAirport.terminal,
      'timezone': a.arrivalAirport.timeZoneRegionName
    }
  }
