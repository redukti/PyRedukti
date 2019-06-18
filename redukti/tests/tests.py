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
        x = redukti.make_date_from_dmy(18,6,2019)
        self.assertEqual(x.day(), 18)
        self.assertEqual(x.month(), 6)
        self.assertEqual(x.year(), 2019)
        self.assertEqual(x.serial(), 43634)

    def test_schedule_basics(self):
        x = schedule_pb2.ScheduleParameters()
        x.effective_date = redukti.make_date_from_dmy(1,1,2016).serial()
        x.termination_date = redukti.make_date_from_dmy(1,1,2017).serial()
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


if __name__ == '__main__':
    unittest.main()

