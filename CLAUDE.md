This is the starting point of this repository.

I want to make an app that queries the Rhode Island DMV appointment maker to see when appointments are available. This is still in exploratory stages. I have two possible use-cases so far. The first is that I run a cron job that queries the available appointments every minute or so, so I can look at the data after a week or two and observe patterns (e.g. when are new appointments added?). The second is a notifier for public use (or at least private use), so that the data is queried every minute and if a slot becomes available, the user receives a text so they can make an appointment.

## Sample API Response

Endpoint: `https://ridmvreservations.ri.gov/WebAPI/reservation/slots?visitTypeId=20`

```json
{
  "reservationSlots": [
    {
      "availableSlotCount": 0,
      "location": "Middletown",
      "officeId": 3,
      "reservationId": 0,
      "scheduleDate": "2026-03-02T00:00:00",
      "startTime": "00:00:00"
    },
    {
      "availableSlotCount": 0,
      "location": "Cranston",
      "officeId": 19,
      "reservationId": 0,
      "scheduleDate": "2026-03-02T00:00:00",
      "startTime": "00:00:00"
    },
    {
      "availableSlotCount": 0,
      "location": "Woonsocket",
      "officeId": 5,
      "reservationId": 0,
      "scheduleDate": "2026-03-02T00:00:00",
      "startTime": "00:00:00"
    },
    {
      "availableSlotCount": 0,
      "location": "Wakefield",
      "officeId": 4,
      "reservationId": 0,
      "scheduleDate": "2026-03-02T00:00:00",
      "startTime": "00:00:00"
    },
    {
      "availableSlotCount": 0,
      "location": "Wakefield",
      "officeId": 4,
      "reservationId": 0,
      "scheduleDate": "2026-03-03T00:00:00",
      "startTime": "00:00:00"
    },
    {
      "availableSlotCount": 0,
      "location": "Middletown",
      "officeId": 3,
      "reservationId": 0,
      "scheduleDate": "2026-03-03T00:00:00",
      "startTime": "00:00:00"
    },
    {
      "availableSlotCount": 0,
      "location": "Woonsocket",
      "officeId": 5,
      "reservationId": 0,
      "scheduleDate": "2026-03-03T00:00:00",
      "startTime": "00:00:00"
    },
    {
      "availableSlotCount": 0,
      "location": "Cranston",
      "officeId": 19,
      "reservationId": 0,
      "scheduleDate": "2026-03-03T00:00:00",
      "startTime": "00:00:00"
    },
    {
      "availableSlotCount": 7,
      "location": "Middletown",
      "officeId": 3,
      "reservationId": 360126,
      "scheduleDate": "2026-03-04T00:00:00",
      "startTime": "15:15:00"
    },
    {
      "availableSlotCount": 2,
      "location": "Woonsocket",
      "officeId": 5,
      "reservationId": 360121,
      "scheduleDate": "2026-03-04T00:00:00",
      "startTime": "..."
    }
  ]
}
```
