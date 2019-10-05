const ics = require('ics')


const mockResponse = {
  scheduleFlight:  {
    carrier: "KE",
    flightNumber: "82",
    departureAirport: "New York JFK",
    departureAirportFsCode: "JFK",
    departureTerminal: "1",
    departureTime: "2019-10-04T18:20:00Z",
    arrivalAirport: "Seoul Incheon",
    arrivalAirportCode: "ICN",
    arrivalTerminal: "2",
    arrivalTime: "2019-10-05T08:20:00Z"
  }
}
const f = mockResponse.scheduleFlight

const departure = new Date(f.departureTime)
const arrival = new Date(f.arrivalTime)
const duration = (arrival - departure)/1000
const hours = Math.floor(duration/3600)
const mins = duration % 3600

const event = {
  // is there a better way to get date array?
  start: [departure.getFullYear(),
          departure.getMonth()+1,
          departure.getDate(),
          departure.getHours(),
          departure.getMinutes() ],
  duration: { hours: hours, minutes :mins },
  title: `${f.carrier}${f.flightNumber}: ${f.departureAirportFsCode}-${f.arrivalAirportCode}`,
  description: `From: ${f.departureAirport}: Terminal: ${f.departureTerminal}\nTo: ${f.arrivalAirport} Terminal: ${f.arrivalTerminal}`
}

ics.createEvent(event, (error, value) => {
  if (error) {
    console.log(error)
    return
  }
  
  console.log(value)
})

