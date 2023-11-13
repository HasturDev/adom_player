def calculate_reward(state, next_state):
    reward = 0

    # Example checks - these will depend on the actual structure of 'state' and 'next_state'
    # Movement: Check if the position has changed
    if next_state['position'] != state['position']:
        reward += 1

    # Maintaining Max Health: Check if current health is at max
    if next_state['current_health'] == next_state['max_health']:
        reward += 1

    # Gaining Gold: Check if the gold count has increased
    if next_state['gold'] > state['gold']:
        reward += 1

    return reward
