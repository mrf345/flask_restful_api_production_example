def convert_safely(to, to_convert, default):
    '''Convert value to another type and failsafe.

    Parameters
    ----------
    to : any type.
        type to convert to.
    to_convert : any
        value to convert from a given type to another.
    default : any
        value to fallback to, if conversion failed.
    '''
    converted = default

    try:
        converted = to(to_convert)
    except Exception:
        pass

    return converted
