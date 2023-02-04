from configparser import ConfigParser


def read_db_config(filename='db.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    config = ConfigParser()
    config.read(filename)

    # get section, default to mysql
    db = {}
    
    params = config.items(section)
    for param in params:
        db[param[0]] = param[1]
    return db
