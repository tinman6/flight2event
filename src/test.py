# -*- coding: utf-8 -*-

import unittest

from flight2event import flight2event

class TestFlight2Event(unittest.TestCase):
  # getSchedule('KE','82', datetime.datetime(2020,2,22))
  ke82_schedule = {
    'ident': 'KAL82',
    'origin': 'KJFK',
    'departureTime': 1582390800, # February 22, 2020 5:00:00 PM
    'destination': 'RKSI',
    'arrivalTime': 1582442700 # February 23, 2020 7:25:00 AM
  }

  # getSchedule('AF','007', datetime.datetime(2020,2,22))
  af007_schedule = {
    'ident': 'ROT9526',
    'departuretime': 1582414800,
    'arrivaltime': 1582441200,
    'origin': 'KJFK',
    'destination': 'LFPG'
  }

  # getAirports('KE', '82')
  ke82_airport = {
    'origin': {
      'name': 'John F. Kennedy International Airport',
      'iata': 'JFK',
      'terminal': '1',
      'timezone': 'America/New_York'
    },
    'destination': {
      'name': 'Incheon International Airport',
      'iata': 'ICN',
      'terminal': '2',
      'timezone': 'Asia/Seoul'
    }
  }

  # getAirport('AF', '007')
  af007_airport = {
    'origin': {
      'name': 'John F. Kennedy International Airport',
      'iata': 'JFK',
      'terminal': '1',
      'timezone': 'America/New_York'
    },
    'destination': {
    'name': 'Charles de Gaulle Airport',
      'iata': 'CDG',
      'terminal': '2E',
      'timezone': 'Europe/Paris'
    }
  }


  def testFligh2tEvent(self):
    c = flight2event('KE', '82', self.ke82_schedule, self.ke82_airport, 'A1B2C3')
    self.assertIn('DTSTART:20200222T170000Z', c)
    self.assertIn('DTEND:20200223T072500Z', c)
    self.assertIn('SUMMARY:KE82: JFK-ICN', c)
    self.assertIn('DESCRIPTION:From: John F. Kennedy International Airport\\, Terminal: 1\\nTo: Incheon International Airport\\, Terminal: 2\\nConfirmation: A1B2C3', c)


  @unittest.skip('todo')
  def testFligh2tEventNoAirportTerminal(self):
    pass


  def testFligh2tEventNoConfirmation(self):
    c = flight2event('KE', '82', self.ke82_schedule, self.ke82_airport)
    self.assertIn('DTSTART:20200222T170000Z', c)
    self.assertIn('DTEND:20200223T072500Z', c)
    self.assertIn('SUMMARY:KE82: JFK-ICN', c)
    self.assertIn('DESCRIPTION:From: John F. Kennedy International Airport\\, Terminal: 1\\nTo: Incheon International Airport\\, Terminal: 2', c)


if __name__ == '__main__':
  unittest.main()
