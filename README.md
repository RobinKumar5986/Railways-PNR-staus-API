I have created an API for getting the Indian railway PNR statis.
[Yoc can try the API at ](https://pnr-status-for-railways-api.onrender.com/docs)

Note the above link is for docs for integration in your application you can use the below link

[API(cahage the pnr number according to your needs)](https://pnr-status-for-railways-api.onrender.com/status?pnr=1234567890)

Note : this API may not work in future so, you can refer the code because this API is created by doing webscraping over some webpage who can show the PNR status.

This is only of ptrsional project. 
Please do not use this commercially.

feel free to contact me for any issus.

Sample Working response 

{
    "ShowBlaBlaAd": false,
    "ShowCab": false,
    "Ads": [],
    "WebsiteEvents": [
        "ga('send', 'event', 'pnrpage-skyscanner-ad', 'pnrpage-skyscanner-ad-shown')"
    ],
    "PnrAlternativeAdPosition": 1,
    "WebsiteAds": null,
    "SponsoredButtons": [],
    "Pnr": "4361365838",
    "TrainNo": "18638",
    "TrainName": "SMVB HTE EXP",
    "InformationMessage": null,
    "Doj": "13-02-2024",
    "BookingDate": "25-01-2024",
    "Quota": "GN",
    "DestinationDoj": "14-02-2024",
    "SourceDoj": "13-02-2024",
    "From": "SMVB",
    "To": "HTE",
    "ReservationUpto": "HTE",
    "BoardingPoint": "SMVB",
    "Class": "3A",
    "ChartPrepared": false,
    "BoardingStationName": "SMVT BENGALURU",
    "TrainStatus": "",
    "TrainCancelledFlag": false,
    "ReservationUptoName": "Hatia",
    "PassengerCount": 1,
    "PassengerStatus": [
        {
            "ReferenceId": null,
            "Pnr": null,
            "Number": 1,
            "Prediction": "67% Chance",
            "PredictionPercentage": "67",
            "ConfirmTktStatus": "Probable",
            "Coach": "",
            "Berth": 4,
            "BookingStatus": "GNWL  72",
            "CurrentStatus": "GNWL  4",
            "CoachPosition": null,
            "BookingBerthNo": "72",
            "BookingCoachId": "",
            "BookingStatusNew": "GNWL",
            "BookingStatusIndex": "0",
            "CurrentBerthNo": "4",
            "CurrentCoachId": "",
            "BookingBerthCode": null,
            "CurrentBerthCode": null,
            "CurrentStatusNew": "GNWL",
            "CurrentStatusIndex": "0"
        }
    ],
    "CacheTime": "0001-01-01T00:00:00",
    "Error": null,
    "ErrorCode": 0,
    "DepartureTime": "00:30",
    "ArrivalTime": "11:15",
    "ExpectedPlatformNo": "7",
    "BookingFare": "1935",
    "TicketFare": "1935",
    "CoachPosition": "L SLR UR UR UR UR UR UR S7 S6 S5 S4 S3 S2 S1 B6 B5 B4 B3 B2 B1 A1 VSKP",
    "Rating": 4.0,
    "FoodRating": 3.5,
    "PunctualityRating": 4.2,
    "CleanlinessRating": 4.2,
    "SourceName": "BENGALURU",
    "DestinationName": "Ranchi",
    "Duration": "34:45",
    "RatingCount": 364,
    "HasPantry": false,
    "BookedInConfirmtkt": false,
    "BookedByUser": false,
    "BookingId": "",
    "GroupingId": null,
    "OptVikalp": false,
    "VikalpData": "",
    "VikalpTransferred": false,
    "VikalpTransferredMessage": "",
    "FlightBannerUrl": "https://cdn.confirmtkt.com/img/banner/flight_banner_waitlist_cancellation_screen.png"
}

Wrong response JSON 

{
    "ShowBlaBlaAd": false,
    "ShowCab": false,
    "Ads": [],
    "WebsiteEvents": [],
    "PnrAlternativeAdPosition": 1,
    "WebsiteAds": null,
    "SponsoredButtons": [],
    "Pnr": "123123",
    "TrainNo": null,
    "TrainName": null,
    "InformationMessage": null,
    "Doj": null,
    "BookingDate": null,
    "Quota": null,
    "DestinationDoj": null,
    "SourceDoj": null,
    "From": null,
    "To": null,
    "ReservationUpto": null,
    "BoardingPoint": null,
    "Class": null,
    "ChartPrepared": false,
    "BoardingStationName": null,
    "TrainStatus": null,
    "TrainCancelledFlag": false,
    "ReservationUptoName": null,
    "PassengerCount": 0,
    "PassengerStatus": null,
    "CacheTime": "0001-01-01T00:00:00",
    "Error": "Invalid PNR number. Please enter valid 10 digit PNR",
    "ErrorCode": 301,
    "DepartureTime": null,
    "ArrivalTime": null,
    "ExpectedPlatformNo": null,
    "BookingFare": null,
    "TicketFare": null,
    "CoachPosition": null,
    "Rating": 0.0,
    "FoodRating": 0.0,
    "PunctualityRating": 0.0,
    "CleanlinessRating": 0.0,
    "SourceName": null,
    "DestinationName": null,
    "Duration": null,
    "RatingCount": 0,
    "HasPantry": false,
    "BookedInConfirmtkt": false,
    "BookedByUser": false,
    "BookingId": null,
    "GroupingId": null,
    "OptVikalp": false,
    "VikalpData": "",
    "VikalpTransferred": false,
    "VikalpTransferredMessage": "",
    "FlightBannerUrl": "https://cdn.confirmtkt.com/img/banner/home_screen_flight_banner.png"
}
