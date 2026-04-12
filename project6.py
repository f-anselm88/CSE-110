# Extra features: Allow user to enter a country name to see its min, max, and average
# life expectancy: Find the country with the largest single-year drop in life expectancy.

def load_data(filename):
    data = []
    with open(filename, "r") as file:
        first_line = True
        for line in file:
            if first_line:
                first_line = False
                continue
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            if len(parts) < 4:
                continue
            try:
                country = parts[0].strip()
                year = int(parts[2].strip())
                life_exp = float(parts[3].strip())
                data.append((country, year, life_exp))
            except ValueError:
                continue
    return data


def find_overall_min_max(data):
    min_entry = data[0]
    max_entry = data[0]
    for entry in data:
        if entry[2] < min_entry[2]:
            min_entry = entry
        if entry[2] > max_entry[2]:
            max_entry = entry
    return min_entry, max_entry


def analyze_year(data, target_year):
    year_data = [entry for entry in data if entry[1] == target_year]
    if not year_data:
        return None

    total = 0
    min_entry = year_data[0]
    max_entry = year_data[0]

    for entry in year_data:
        total += entry[2]
        if entry[2] < min_entry[2]:
            min_entry = entry
        if entry[2] > max_entry[2]:
            max_entry = entry

    average = total / len(year_data)
    return average, min_entry, max_entry


def analyze_country(data, target_country):
    country_data = [entry for entry in data if entry[0].lower() == target_country.lower()]
    if not country_data:
        return None

    total = 0
    min_entry = country_data[0]
    max_entry = country_data[0]

    for entry in country_data:
        total += entry[2]
        if entry[2] < min_entry[2]:
            min_entry = entry
        if entry[2] > max_entry[2]:
            max_entry = entry

    average = total / len(country_data)
    return average, min_entry, max_entry


def find_largest_drop(data):
    # Group by country
    country_years = {}
    for country, year, life_exp in data:
        if country not in country_years:
            country_years[country] = []
        country_years[country].append((year, life_exp))

    biggest_drop = 0
    drop_country = ""
    drop_from_year = 0
    drop_to_year = 0
    drop_from_val = 0
    drop_to_val = 0

    for country, entries in country_years.items():
        entries.sort(key=lambda x: x[0])
        for i in range(1, len(entries)):
            prev_year, prev_val = entries[i - 1]
            curr_year, curr_val = entries[i]
            if curr_year == prev_year + 1:
                drop = prev_val - curr_val
                if drop > biggest_drop:
                    biggest_drop = drop
                    drop_country = country
                    drop_from_year = prev_year
                    drop_to_year = curr_year
                    drop_from_val = prev_val
                    drop_to_val = curr_val

    return drop_country, drop_from_year, drop_to_year, drop_from_val, drop_to_val, biggest_drop


def main():
    filename = "life-expectancy.csv"

    print("Loading data...")
    data = load_data(filename)
    print(f"Loaded {len(data)} records.\n")

    # Overall min and max
    min_entry, max_entry = find_overall_min_max(data)
    print(f"The overall max life expectancy is: {max_entry[2]} from {max_entry[0]} in {max_entry[1]}")
    print(f"The overall min life expectancy is: {min_entry[2]} from {min_entry[0]} in {min_entry[1]}")
    print()

    # Year analysis
    year_input = input("Enter the year of interest: ").strip()
    try:
        target_year = int(year_input)
    except ValueError:
        print("Invalid year entered.")
        return

    result = analyze_year(data, target_year)
    if result is None:
        print(f"No data found for the year {target_year}.")
    else:
        average, year_min, year_max = result
        print(f"\nFor the year {target_year}:")
        print(f"  The average life expectancy across all countries was {round(average, 2)}")
        print(f"  The max life expectancy was in {year_max[0]} with {year_max[2]}")
        print(f"  The min life expectancy was in {year_min[0]} with {year_min[2]}")

    print()

    # Country analysis (extra feature #1)
    country_input = input("Enter a country name to analyze (or press Enter to skip): ").strip()
    if country_input:
        result = analyze_country(data, country_input)
        if result is None:
            print(f"No data found for '{country_input}'.")
        else:
            average, c_min, c_max = result
            print(f"\nFor {c_min[0]}:")
            print(f"  Average life expectancy: {round(average, 2)}")
            print(f"  Highest: {c_max[2]} in {c_max[1]}")
            print(f"  Lowest:  {c_min[2]} in {c_min[1]}")

    print()

    # Largest single-year drop (extra feature #2)
    print("Finding the largest single-year drop in life expectancy...")
    country, y1, y2, v1, v2, drop = find_largest_drop(data)
    print(f"  Largest drop: {country} dropped {round(drop, 3)} years")
    print(f"  From {round(v1, 3)} in {y1} to {round(v2, 3)} in {y2}")


main()