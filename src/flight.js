const Swagger = require('swagger-client')
const fs = require('fs')
const swagger_file = '/home/syeung/devel/flight2event/src/schemas/scheduledFlightsService.json'

const flight_num = 'KE82'
const date = '2019-10-04'

const [carrier, number] = flight_num.match(/[A-Za-z]+|[0-9]+/g)
const [year, month, day] = date.split('-')

Swagger({spec : JSON.parse(fs.readFileSync(swagger_file, 'utf8'))})
  .then(client => {
    // byFlight_Arriving2 returns json
    client.apis.default.byFlight_Arriving2({}, {
      parameters: {
        appId: '9a2aa882',
        appKey: '350f0d9341d4dea24bf3fd3c722ba3d3',
        carrier: carrier,
        flightnumber: number,
        year: year,
        month: month,
        day: day
      }
    })
      .then(response => {
        /*
        if ("error" in response.body) {
          throw new Error(response.body.error.errorMessage)
        }
        */
        const mockResponse = {
          scheduleFlight:  {
            carrier: "KE",
            flightNumber: "82",
            departureAirport: "New York JFK",
            departureAirportFsCode: "JFK",
            departureTerminal: "1",
            departureTime: "2019-10-04T18:20:00.00.000Z",
            arrivalAirport: "Seoul Incheon",
            arrivalAirportCode: "ICN",
            arrivalTerminal: "2",
            arrivalTime: "2019-10-05T08:20:00.00.000Z"
          }
        }
        console.log(response)
        console.log(mockResponse)

      })
  })
