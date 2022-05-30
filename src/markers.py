import yaml

# Program Information Variables
# Variables should be lowercase with underscores between words
_program = "Dynmap Markers Editor"
_author = "Robert Jobe"
_version = 1.0
_startYear = 2022  # Do not change
_latestYear = 2022

#  Print program information to console
print("%s version %.1f" % (_program, _version))
print("Copyright %i-%i %s. All Rights Reserved\n" % (_startYear, _latestYear, _author))


def get_data():
    while True:
        try:
            markers_file = open(input("Enter the path of the markers.yml file: "), "r")
            markers_file_data = yaml.safe_load(markers_file)
            markers_file.close()
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")
            continue
        else:
            return markers_file_data


print(yaml.safe_dump(get_data()))
