def traffic_light_action(color):
    if color.lower() == 'red':
        return "Stop"
    elif color.lower() == 'yellow':
        return "Ready"
    elif color.lower() == 'green':
        return "Go"
    else:
        return "Error occured"

color = input("Enter the traffic light color (red, yellow, green): ")

action = traffic_light_action(color)

print(f"The action is: {action}")