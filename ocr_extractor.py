# ocr_extractor.py

def parse_ocr_to_soc(ocr_text, order=1):
    """
    Example input: THAI-P1234567-MR-JOHN-DOE-15JAN1990-10JUL2020-09JUL2030
    Output: SOC formatted string
    """
    parts = ocr_text.strip().split("-")
    nationality, passport_no, title, firstname, lastname, dob, doi, doe = parts
    full_name = f"{lastname}-{firstname}"
    age = calculate_age(dob)
    valid = "VALID" if is_valid(doe) else "EXPIRED"

    return f"{order:02d}-{full_name.upper()}-{title.upper()}--{nationality}-{passport_no}-{dob}-{doi}-{doe}-{valid}-{age} YRS"

def calculate_age(dob):
    from datetime import datetime
    dob_dt = datetime.strptime(dob, "%d%b%Y")
    today = datetime.today()
    return today.year - dob_dt.year - ((today.month, today.day) < (dob_dt.month, dob_dt.day))

def is_valid(doe):
    from datetime import datetime
    doe_dt = datetime.strptime(doe, "%d%b%Y")
    return doe_dt >= datetime.today()

# Example usage
if __name__ == "__main__":
    example = "THAI-P1234567-MR-JOHN-DOE-15JAN1990-10JUL2020-09JUL2030"
    print(parse_ocr_to_soc(example, 1))
