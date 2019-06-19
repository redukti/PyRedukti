# DO NOT REMOVE COPYRIGHT NOTICES OR THIS HEADER.
#
# Contributor(s):
#
# The Original Software is OpenRedukti (https://github.com/redukti/OpenRedukti).
# The Initial Developer of the Original Software is REDUKTI LIMITED (http://redukti.com).
# Authors: Dibyendu Majumdar
#
# Copyright 2019 REDUKTI LIMITED. All Rights Reserved.
#
# The contents of this file are subject to the the GNU General Public License
# Version 3 (https://www.gnu.org/licenses/gpl.txt).

import redukti
import unittest
from redukti import enums_pb2 as enums
from redukti import schedule_pb2

class TestDate(unittest.TestCase):

    def test_date_basics(self):
        x = redukti.Date.from_dmy(18,6,2019)
        self.assertEqual(x.day(), 18)
        self.assertEqual(x.month(), 6)
        self.assertEqual(x.year(), 2019)
        self.assertEqual(x.serial(), 43634)

    def test_schedule_basics(self):
        x = schedule_pb2.ScheduleParameters()
        x.effective_date = redukti.Date.from_dmy(1,1,2016).serial()
        x.termination_date = redukti.Date.from_dmy(1,1,2017).serial()
        x.payment_frequency = enums.TENOR_3M
        x.payment_calendars.append(enums.GBLO)
        x.payment_calendars.append(enums.USNY)
        x.payment_convention = enums.MODIFIED_FOLLOWING
        y = redukti.generate_schedule(x)
        # TODO Check following
        #adjusted_start_dates: 42370
        #adjusted_start_dates: 42461
        #adjusted_start_dates: 42552
        #adjusted_start_dates: 42644
        #adjusted_end_dates: 42461
        #adjusted_end_dates: 42552
        #adjusted_end_dates: 42644
        #adjusted_end_dates: 42736
        #adjusted_payment_dates: 42461
        #adjusted_payment_dates: 42552
        #adjusted_payment_dates: 42646
        #adjusted_payment_dates: 42738

    def test_calendar_basics(self):
        calendar = redukti.Calendar([enums.GBLO])
        d = redukti.Date.from_dmy(16,6,2019)
        self.assertTrue(calendar.is_holiday(d))
        d2 = calendar.advance(d, 1, enums.DAYS)
        self.assertEqual(d.serial()+1, d2.serial())
        d3 = calendar.advance(d, -1, enums.DAYS)
        self.assertEqual(d3.serial(), redukti.Date.from_dmy(14,6,2019).serial())
        #d3 = calendar.advance(d, -1, 90)

    def test_daycountfraction_basics(self):
        dfc = redukti.DayFraction(enums.ACT_365_FIXED)
        d1 = redukti.Date.from_dmy(14,6,2019)
        d2 = redukti.Date.from_dmy(13,6,2020)
        fraction = dfc.year_fraction(d1, d2)
        self.assertEqual(fraction, 1.0)
    
    def test_interestrateindex_basics(self):
        idx = redukti.InterestRateIndex.get_index(enums.USD, enums.LIBOR, enums.TENOR_1W)
        dt = redukti.Date.from_dmy(23,10,2016)
        adjusted = idx.adjust_date(dt, 1)
        self.assertEqual(adjusted.serial(), redukti.Date.from_dmy(24,10,2016).serial())
        fixing_dt, value_dt, maturity_dt = idx.date_components(adjusted)
        self.assertEqual(maturity_dt.serial(), redukti.Date.from_dmy(31,10,2016).serial())
        self.assertEqual(value_dt.serial(), adjusted.serial())

if __name__ == '__main__':
    unittest.main()

