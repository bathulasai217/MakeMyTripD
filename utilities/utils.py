import time
import json
from base.base_driver import BaseDriver


class Utils(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def flights_list(self,studentfareflights,flightname,flightduration,flightdepaturetime):
        count = 0
        result = {}
        result = {
            "rows": []
        }
        for i, j, k in zip(flightname, flightdepaturetime, flightduration):
            row = {}
            row = {
                'Flight': i.text,
                'Duration': j.text,
                'Departure_time': k.text
            }
            count += 1
            if count > len(studentfareflights):
                break
            else:
                result['rows'].append(row)
        print(json.dumps(result))

    def titleVerificaation(self):
        act_title = self.pagetitle()
        if act_title == "MakeMyTrip - #1 Travel Website 50% OFF on Hotels, Flights & Holiday":
            assert True

        else:
            self.screenshot(".\\screenshots\\" + "homePageTitle.png")



