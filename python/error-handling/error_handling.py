def handle_error_by_throwing_exception():
    raise Exception('Exception raised')


def handle_error_by_returning_none(input_data):
        try:
            input_data = int(input_data)
            return input_data
        except TypeError:
            return None


def handle_error_by_returning_tuple(input_data):
    try:
        input_data = int(input_data)
        return True, input_data
    except:
        return False, None


def filelike_objects_are_closed_on_exception(filelike_object):
    with filelike_object:
        filelike_object.do_something()
    return filelike_object