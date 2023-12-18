import random

def interpret():

    gender_code = random.randint(1, 6)
    year_code = random.randint(0, 99)
    month = random.randint(1,12)
    day = random.randint(1,31)
    region_code = random.randint(1,52)
    unique_code = str(random.randint(0, 999)).zfill(3)

    month_str = str(month).zfill(2)
    day_str = str(day).zfill(2)
    year_str = str(year_code).zfill(2)
    region_str = str(region_code).zfill(2)

    id_number = f"{gender_code}{year_str}{month_str}{day_str}{region_str}{unique_code}"

    control_constant = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    total = sum(int(id_number[i]) * int(control_constant[i]) for i in range(len(control_constant)))
    control_code = total % 11
    if control_code == 10:
        control_digit = 1
    else:
        control_digit = control_code

    id_number += f"{control_digit}"

    print("ID number: " + id_number)

    if gender_code == 1 or  gender_code == 3 or gender_code == 5:
        gender = "Male"
    else:
        gender = "Female"

    if gender_code == 1 or gender_code == 2:
        year = 1900 + year_code
    elif gender_code == 3 or gender_code == 4:
        year = 1800 + year_code
    else:
        year = 2000 + year_code

    if gender_code == 5 or gender_code == 6 and year_code > 23:
        raise ValueError("Invalid year of birth")

    if month == 2 and day > 29:
        raise  ValueError("Invalid day of birth")
    elif month in [4, 6, 9, 11] and day > 30:
        raise ValueError("Invalid day of birth")

    region_codes = {
        1 :"Alba", 2: "Arad", 3 : "Arges", 4: "Bacau", 5 : "Bihor", 6 : "Bistrita-Nasaud", 7 : "Botosani", 8 : "Brasov",
        9 : "Braila", 10 : "Buzau", 11 : "Caras-Severin", 12 : "Cluj", 13 : "Constanta", 14 : "Covasna", 15 : "Dambovita",
        16 : "Dolj", 17 : "Galati", 18 : "Gorj", 19 : "Harghita", 20 : "Hunedoara", 21 : "Ialomita", 22 : "Iasi", 23 : "Ilfov",
        24 : "Maramures", 25 : "Mehedinti", 26 : "Mures", 27 : "Neamt", 28 : "Olt", 29 : "Prahova", 30 : "Satu Mare", 31 : "Salaj",
        32 : "Sibiu", 33 : "Suceava", 34 : "Teleorman", 35 : "Timis", 36 : "Tulcea", 37 : "Vaslui", 38 : "Valcea", 39 : "Vrancea",
        40 : "Bucuresti", 41 : "Bucuresti - Sector 1", 42 : "Bucuresti - Sector 2", 43 : "Bucuresti - Sector 3", 44 : "Bucuresti - Sector 4",
        45 : "Bucuresti - Sector 5", 46 : "Bucuresti - Sector 6", 51 : "Calarasi", 52 : "Giurgiu"
    }

    region = region_codes.get(region_code)

    if region_code not in region_codes.keys():
        raise ValueError("Invalid region")

    return {
        "Gender" : gender,
        "Year of Birth" : year,
        "Month of Birth" : month_str,
        "Day of Birth" : day_str,
        "Region" : region
    }

if __name__ == '__main__':
    try:
        result =  interpret()
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")