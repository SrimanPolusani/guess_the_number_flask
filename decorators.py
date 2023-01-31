def bold_decorator(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def h1_decorator(function):
    def wrapper():
        return "<h1>" + function() + "</h1>"

    return wrapper


def italian_decorator(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def underline_decorator(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper
