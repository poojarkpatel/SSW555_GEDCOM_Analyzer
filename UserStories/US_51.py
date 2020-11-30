from datetime import datetime

def US_51(family):
    """ List all marriage anniversaries in the next 2 months """

    warnings = list()

    today_date = int(datetime.today().strftime("%d"))
    today_month = int(datetime.today().strftime("%m"))

    for fam, value in family.items():
        marr = value._marriage_date
        if marr != "NA":
            marr_date = str(marr)
            curr_month = int(marr_date.split('-')[1])
            curr_day = int(marr_date.split('-')[2])

            day_diff = abs(curr_month - today_month) * 60 + (curr_day - today_date)
            if day_diff > 0 and day_diff <= 61:
                warnings.append(f"The family id {fam} have their marriage anniversary in the next 2 months. Line number: {value.get_line_numbers()['family_id']}")


    return warnings




