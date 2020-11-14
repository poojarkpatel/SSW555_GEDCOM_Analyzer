from datetime import datetime

def US_39(family):
    """ List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days """

    warnings = list()

    today_date = int(datetime.today().strftime("%d"))
    today_month = int(datetime.today().strftime("%m"))

    for fam, value in family.items():
        marr = value._marriage_date
        if marr != "NA":
            marr_date = str(marr)
            curr_month = int(marr_date.split('-')[1])
            curr_day = int(marr_date.split('-')[2])

            day_diff = abs(curr_month - today_month) * 30 + (curr_day - today_date)
            if day_diff > 0 and day_diff <= 31:
                warnings.append(f"The family id {fam} have their marriage anniversary in the next 30 days. Line number: {value.get_line_numbers()['family_id']}")


    return warnings




