import configparser

# function to read properties.ini file and return value for required key


def get(key):
    config = configparser.ConfigParser()
    config.read("properties.ini")
    for section_in_ini in config.sections():
        for key_in_section in config[section_in_ini]:
            if key == key_in_section:
                return config[section_in_ini][key]
