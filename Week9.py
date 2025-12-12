
def filter_alerts(alerts, min_severity):
    final_alerts = []

    if min_severity == "ADVISORY":
        min_level = 1
    elif min_severity == "WATCH":
        min_level = 2
    elif min_severity == "WARNING":
        min_level = 3
    else:
        return final_alerts
    for alert in alerts:
        if alert==" ":
            continue
    if not alert==" ":
        alert=alerts.split("]")
#I don't know










