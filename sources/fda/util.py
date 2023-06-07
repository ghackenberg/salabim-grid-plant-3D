import salabim as sim

def toString(state: sim.State):
    # Calculate total
    total = 0
    for value in state.value.values():
        duration = state.value.value_duration(value)
        total = total + duration
    # Calculate output
    output = ""
    for value in state.value.values():
        duration = state.value.value_duration(value)
        if total > 0:
            percentage = duration / total
        else:
            percentage = 1
        output = f"{output}{', ' if output != '' else ''}{value}={'{:.1f}'.format(percentage * 100)}%"
    # Return output
    return output
