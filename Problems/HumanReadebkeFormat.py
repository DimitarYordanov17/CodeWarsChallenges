def format_duration(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365

    elements = {}

    elements["seconds"] = seconds % 60
    elements["minutes"] = minutes
    elements["hours"] = hours
    elements["days"] = days
    elements["years"] = years


    elements = dict(filter(lambda a: a[1] > 0, elements.items()))


    if len(elements) >= 3:
        for k, v in reversed(list(elements.items())[:len(elements.items()) - 2]):
            if v == 1:
                print(f"{v} {k[:-1]}", end=", ")
            else:
                print(f"{v} {k}", end=", ")
        
        if list(elements.values())[-2] == 1:
            print("1 minute", end=" and ")
        else:
            print(f"{list(elements.values())[-2]} minutes", end=" and ")
        
        if list(elements.values())[-1] == 1:
            print("1 second")
        else:
            print(f"{list(elements.values())[-1]} seconds")

    elif len(elements) == 2:
        if list(elements.values())[-2] == 1:
            print("1 minute")
        else:
            print(f"{list(elements.values())[-2]} minutes", end=" and ")
        
        if list(elements.values())[-1] == 1:
            print("1 second")
        else:
            print(f"{list(elements.values())[-1]} seconds")

    elif len(elements) == 1:
        if list(elements.values())[0] == 1:
            print("1 second")
        else:
            print(f"{list(elements.values())[0]} seconds")
    else:
        print("now")



format_duration(3662)
format_duration(62)
format_duration(120)
format_duration(3600)





