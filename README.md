# timew-report

An interface for [Timewarrior](https://timewarrior.net) report data.

## Installation

Use `pip` to install the package:

    pip install timew-report

## Usage

Create an executable python script and place it in your `Timewarrior` extension folder.
`Timewarrior` will send its data to the script when called with the extension's name:

    timew [report] <extension_name>

See [Timewarrior documentation](https://timewarrior.net/docs/api/) for more details about this.

## Details

This package consists of three classes which aid processing the `Timewarrior` data:
* `TimeWarriorParser`
* `TimeWarriorConfig`
* `TimeWarriorInterval`

The classes are explained in detail below.
You find some usage examples at the bottom of this README.

### Class `TimeWarriorParser`

You can pass an input stream with Timewarrior data to constructor of `TimeWarriorParser`:

    parser = TimeWarriorParser(sys.stdin)

Retrieve configuration (as `TimeWarriorConfig` object) and intervals (array of `TimeWarriorInterval` objects):

    tw_config = parser.get_config()
    tw_intervals = parser.get_intervals()

### Class `TimeWarriorConfig`

The object `TimeWarriorConfig` encapsulates the configuration dictionary and provides an interface to retrieve values:
 
    value = tw_config.get_value(key, default)
    
There is a specialized getter for boolean values which returns `True` for the given `key` if the respective `value` is `on`, `1`, `yes`, `y`, or `true`:

    bool = tw_config.get_boolean(key, default)

There is a specialized getter for integer values:

    int_val = tw_config.get_int(key, default)
    
In case of a non-parsable string, this function raises a `ValueError` exception.

There are specialized getters for the `debug`, `verbose`, and `confirmation` flag:

    debug = tw_config.get_debug()
    verbose = tw_config.get_verbose()
    confirmation = tw_config.get_confirmation()

### Class `TimeWarriorInterval`

The `TimeWarriorInterval` encapsulates the time interval data and provides an interface to retrieve values:

    start = tw_interval.get_start()
    end = tw_interval.get_end()
    tags = tw_interval.get_tags()
    annotation = tw_interval.get_annotation()
    
`start` and `end` are `datetime` objects and given in local time (`end` is equal to `None` if the interval is open).
`tags` is a list of zero or more strings, `annotation` is a single string or `None`.

An interval can be queried whether it is open:

    is_open = tw_interval.is_open()

There are methods which return the interval's start or end date (day, month, year) respectively.

    start_date = tw_interval.get_start_date()
    end_date = tw_interval.get_end_date()

**Note:** The function `TimeWarriorInterval.get_date()` has been deprecated in favour of `TimeWarriorInterval.get_start_date()`.

## Examples

A simple CSV report:

    import sys
    from timewreport.parser import TimeWarriorParser
    
    parser = TimeWarriorParser(sys.stdin)
    
    for interval in parser.get_intervals():
        line = '"{}"'.format(interval.get_start())
        line += ',"{}"'.format(interval.get_end()) if not interval.is_open() else ''
    
        for tag in interval.get_tags():
            line += ',"{}"'.format(tag)
    
        print(line)

Summing up totals by tag:

    import sys
    from timewreport.parser import TimeWarriorParser
    
    parser = TimeWarriorParser(sys.stdin)
    
    totals = dict()
    
    for interval in parser.get_intervals():
        tracked = interval.get_duration()
        
        for tag in interval.get_tags():
            if tag in totals:
                totals[tag] += tracked
            else:
                totals[tag] = tracked
    
    # Determine largest tag width.
    max_width = len('Total')
    
    for tag in totals:
        if len(tag) > max_width:
            max_width = len(tag)
    
    # Compose report header.
    print('Total by Tag')
    print('')
    
    # Compose table header.
    print('{:{width}} {:>10}'.format('Tag', 'Total', width=max_width))
    print('{} {}'.format('-' * max_width, '----------'))
    
    # Compose table rows.
    grand_total = 0
    for tag in sorted(totals):
        formatted = totals[tag].seconds
        grand_total += totals[tag].seconds
        print('{:{width}} {:10}'.format(tag, formatted, width=max_width))
    
    # Compose total.
    print('{} {}'.format(' ' * max_width, '----------'))
    print('{:{width}} {:10}'.format('Total', grand_total, width=max_width))
