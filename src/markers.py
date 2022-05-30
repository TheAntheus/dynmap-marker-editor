import yaml
import logging

# Program Information Variables
# Variables should be lowercase with underscores between words
_program = "Dynmap Markers Editor"
_author = "Robert Jobe"
_version = 1.0
_start_year = 2022  # Do not change
_latest_year = 2022


# Setup logger
logger = logging.getLogger('Logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# Use logger.[debug/info/warning/error/critical] to log to the console.


#  Print program information to console
print("%s version %.1f" % (_program, _version))
print("Copyright %i-%i %s. All Rights Reserved\n" % (_start_year, _latest_year, _author))


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
