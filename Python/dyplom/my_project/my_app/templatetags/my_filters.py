from django import template

register = template.Library()

@register.filter(name='time_to_milliseconds')
def time_to_milliseconds(value):
    if isinstance(value, str):
        value = float(value)
    minutes, seconds = divmod(value, 60)
    milliseconds = (seconds - int(seconds)) * 1000
    return '{:02d}:{:02d}.{:03d}'.format(int(minutes), int(seconds), int(milliseconds))
