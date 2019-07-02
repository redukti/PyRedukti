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
import array

class TestDate(unittest.TestCase):

    def test_date_basics(self):
        x = redukti.Date.dmy(18,6,2019)
        self.assertEqual(x.day(), 18)
        self.assertEqual(x.month(), 6)
        self.assertEqual(x.year(), 2019)
        self.assertEqual(x.serial(), 43634)

    def test_schedule_basics(self):
        x = schedule_pb2.ScheduleParameters()
        x.effective_date = redukti.Date.dmy(1,1,2016).serial()
        x.termination_date = redukti.Date.dmy(1,1,2017).serial()
        x.payment_frequency = enums.TENOR_3M
        x.payment_calendars.append(enums.GBLO)
        x.payment_calendars.append(enums.USNY)
        x.payment_convention = enums.MODIFIED_FOLLOWING
        y = redukti.ScheduleGenerator.generate_schedule(x)
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
        d = redukti.Date.dmy(16,6,2019)
        self.assertTrue(calendar.is_holiday(d))
        d2 = calendar.advance(d, 1, enums.DAYS)
        self.assertEqual(d.serial()+1, d2.serial())
        d3 = calendar.advance(d, -1, enums.DAYS)
        self.assertEqual(d3.serial(), redukti.Date.dmy(14,6,2019).serial())
        #d3 = calendar.advance(d, -1, 90)
        result = redukti.Calendar.register_calendar(enums.CATO, [redukti.Date.dmy(14,6,2019)])
        self.assertTrue(result)
        calendar = redukti.Calendar([enums.CATO])
        self.assertTrue(calendar.is_holiday(d))
        self.assertTrue(calendar.is_holiday(d3))
        self.assertFalse(calendar.is_holiday(redukti.Date(d3.serial()-1)))

    def test_daycountfraction_basics(self):
        dfc = redukti.DayFraction(enums.ACT_365_FIXED)
        d1 = redukti.Date.dmy(14,6,2019)
        d2 = redukti.Date.dmy(13,6,2020)
        fraction = dfc.year_fraction(d1, d2)
        self.assertEqual(fraction, 1.0)
    
    def test_interestrateindex_basics(self):
        idx = redukti.InterestRateIndex.get_index(enums.USD, enums.LIBOR, enums.TENOR_1W)
        dt = redukti.Date.dmy(23,10,2016)
        adjusted = idx.adjust_date(dt, 1)
        self.assertEqual(adjusted.serial(), redukti.Date.dmy(24,10,2016).serial())
        fixing_dt, value_dt, maturity_dt = idx.date_components(adjusted)
        self.assertEqual(maturity_dt.serial(), redukti.Date.dmy(31,10,2016).serial())
        self.assertEqual(value_dt.serial(), adjusted.serial())

    def test_interpolator_basics(self):
        x = array.array('d', [0.01,0.02,0.03,0.04,0.05])
        y = array.array('d', [1000000.0,20004.0,300000.5,4000000.0,900000.0])
        interp = redukti.Interpolator(enums.CUBIC_SPLINE_NATURAL, x, y, 2)
        print(interp.interpolate(0.035))
        print(interp.interpolate_with_sensitivities(0.035).value())
        print(interp.interpolate_with_sensitivities(0.035).gradient())

    def test_curve_basics(self):
        maturities = [ redukti.Date.dmy(14,12,2012),
            redukti.Date.dmy(15,12,2012),
            redukti.Date.dmy(20,12,2012),
            redukti.Date.dmy(27,12,2012),
            redukti.Date.dmy(3,1,2013),
            redukti.Date.dmy(13,1,2013),
            redukti.Date.dmy(13,2,2013),
            redukti.Date.dmy(13,3,2013),
            redukti.Date.dmy(13,4,2013),
            redukti.Date.dmy(13,5,2013),
            redukti.Date.dmy(13,6,2013),
            redukti.Date.dmy(13,7,2013),
            redukti.Date.dmy(13,8,2013),
            redukti.Date.dmy(13,9,2013),
            redukti.Date.dmy(13,10,2013),
            redukti.Date.dmy(13,11,2013),
            redukti.Date.dmy(13,12,2013),
            redukti.Date.dmy(13,3,2014),
            redukti.Date.dmy(13,6,2014),
            redukti.Date.dmy(13,9,2014),
            redukti.Date.dmy(13,12,2014),
            redukti.Date.dmy(13,12,2015),
            redukti.Date.dmy(13,12,2016),
            redukti.Date.dmy(13,12,2017),
            redukti.Date.dmy(13,12,2018),
            redukti.Date.dmy(13,12,2019),
            redukti.Date.dmy(13,12,2020),
            redukti.Date.dmy(13,12,2021),
            redukti.Date.dmy(13,12,2022),
            redukti.Date.dmy(13,12,2023),
            redukti.Date.dmy(13,12,2024),
            redukti.Date.dmy(13,12,2027),
            redukti.Date.dmy(13,12,2032),
            redukti.Date.dmy(13,12,2037),
            redukti.Date.dmy(13,12,2042)]

        values = [-0.000419352,
            0.000194959,
            0.00033674,
            0.000491042,
            0.000637816,
            0.000668809,
            0.000568842,
            0.000445083,
            0.000318814,
            0.000227478,
            0.000169979,
            0.000122747,
            8.26E-05,
            4.33E-05,
            2.40E-05,
            4.33E-06,
            -5.28E-06,
            1.59E-05,
            7.73E-05,
            0.000209899,
            0.000362351,
            0.00128521,
            0.002777481,
            0.004634955,
            0.006597457,
            0.008461993,
            0.010232294,
            0.011823099,
            0.013240863,
            0.014577768,
            0.015798443,
            0.018541807,
            0.020446036,
            0.021078048,
            0.021398632]
        curve = redukti.InterpolatedYieldCurve(0, redukti.Date.dmy(11,12,2012), maturities, values, enums.LINEAR, enums.ZERO_RATE, 2, enums.ACT_365_FIXED)

if __name__ == '__main__':
    unittest.main()

