import pytest
import time
from pages.mkmtrip_launch_page import LaunchPage
from pages.search_results_page import SearchResults
from utilities.utils import Utils
# Launching travel website
@pytest.mark.usefixtures("setup")
class TestSearchFlights:

    def test_homePageTitleVerification(self):
        up = Utils(self.driver)
        up.titleVerificaation()
    def test_searchflights(self):
        lp = LaunchPage(self.driver)
        lp.searchFlights("ahamedabad","New delhi")
        lp.selectdate()
        lp.selectstudentfare()
        lp.clickonsearch()
        sp = SearchResults(self.driver)
        up = Utils(self.driver)
        up.flights_list(sp.studentfareflight(),sp.flightname(),sp.depaturetime(),sp.flightduration())
        time.sleep(5)
