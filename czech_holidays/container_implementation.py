from dateutil.easter import easter as calculate_easter
import datetime

class CzechHoliday:
    def __init__(self, date, names):
        self.date = date
        self.czech_name, self.english_name = names

REGULAR_HOLIDAYS = {
    (1, 1): ("Nový rok", "New Year's Day"),
    (5, 1): ("Svátek práce", "Labour Day"),
    (5, 8): ("Den vítězství", "Liberation Day"),
    (7, 5): ("Den slovanských věrozvěstů Cyrila a Metoděje",
             "Saints Cyril and Methodius Day"),
    (7, 6): ("Den upálení mistra Jana Husa", "Jan Hus Day"),
    (9, 28): ("Den české státnosti",
              "St. Wenceslas Day (Czech Statehood Day)"),
    (10, 28): ("Den vzniku samostatného československého státu",
                "Independent Czechoslovak State Day"),
    (11, 17): ("Den boje za svobodu a demokracii",
               "Struggle for Freedom and Democracy Day"),
    (12, 24): ("Štědrý den", "Christmas Eve"),
    (12, 25): ("1. svátek vánoční", "Christmas Day"),
    (12, 26): ("2. svátek vánoční",
               "St. Stephen's Day (The Second Christmas Day)"),
}

EXTRA_NEWYEAR = ("Den obnovy samostatného českého státu",
                 "Restoration Day of the Independent Czech State")
EASTER_MONDAY = ("Velikonoční pondělí", "Easter Monday")
EASTER_FRIDAY = ("Velký pátek", "Good Friday")

def _easter_days(year):
    easter_sunday = calculate_easter(date.year)
    return (easter_sunday - datetime.timedelta(3)),
            easter_sunday + datetime.timedelta(1))

class CzechHolidays:
    def get(self, date):
        date = datetime.date(date)
        regular = REGULAR_HOLIDAYS.get((date.month, date.day))
        if regular:
            return CzechHoliday(date, regular)
        if 3 <= date.month <= 4:
            friday, monday = _easter_days(date.year)
            if date == friday:
                return CzechHoliday(date, EASTER_FRIDAY)
            if date == monday:
                return CzechHoliday(date, EASTER_MONDAY)
        return None

    def __contains__(self, date):
        return self.get(date) is not None

    def generate(self, start_year, end_year=None):
        year = start_year
        while end_year is None or year <= end_year:
            monday, friday = _easter_days(year)
            holidays = (
                (datetime.date(year, 1, 1), EXTRA_NEWYEAR),
                (monday, EASTER_MONDAY),
                (friday, EASTER_FRIDAY),
            ) + ((datetime.date(year, m, d), n)
                 for (m, d), n in REGULAR_HOLIDAYS.items())
            for date, names in holidays:
                yield CzechHoliday(date, names)
            start_year += 1
