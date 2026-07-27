unit = {}
unit["Chalkley"] = {"rank": "CW2", "Years of service": "14"}
unit["Smith"] = {"rank": "SSG", "Years of service": "15"}
unit["TheRock"] = {"rank": "LTCOL", "Years of service": "16"}
unit["Al"] = {"rank": "SGT", "Years of service": "17"}
unit["Shazzam"] = {"rank": "CW5", "Years of service": "33"}


def lookup_soldier(unit, last_name):
    if last_name in unit:
          rank = unit[last_name]["rank"]
          years_service = unit[last_name]["Years of service"]
          print(f"Found Soldier {last_name},\nRank {rank},\n{years_service} years of service.")
    else:
        print("Could not find this Soldier")

user_input = input("Which Soldier would you like to look up?\n")
lookup_soldier(unit, user_input.strip().capitalize())

