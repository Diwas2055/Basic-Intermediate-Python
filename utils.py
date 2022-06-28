# Dictionary excluding specified keys

my_dict = {
     "keyA": 1,
     "keyB": 2,
     "keyC": 3
 }
invalid = {"keyA", "keyB"}

def without_keys(d, keys):
     return {x: d[x] for x in d if x not in keys}

without_keys(my_dict, invalid)


def convert_string_into_datetime(string=None):
    """
    It takes a string as an input and returns a datetime object
    
    :param string: The string to be converted into datetime
    :return: the converted datetime value.
    """
 
    if string:
        import dateutil.parser
        string_value = dateutil.parser.parse(string)
        converted_datetime=string_value.strftime('%m/%d/%Y %H:%M:%S')
        return converted_datetime
    else:
        return None

    
def convert_datetime_into_timestamp(get_datetime=None):
    """
    It converts a string into a datetime object, and then converts that datetime object into a timestamp
    
    :param get_datetime: The datetime value that you want to convert into a timestamp
    """
    import datetime
    import time

    datetime_value=convert_string_into_datetime(get_datetime)
    if datetime_value:
        date = datetime.datetime.strptime(datetime_value,"%m/%d/%Y %H:%M:%S")
        date_timestamp = int(time.mktime(date.timetuple()))        
        return date_timestamp
    else:
        return None

# Convert List into string

def convert_list_to_string(field_name,list=None):
    status=list
    sts_query: list = []
    for s in status:
        sts_query.append(f'{field_name} = {s}')
    return sts_query
