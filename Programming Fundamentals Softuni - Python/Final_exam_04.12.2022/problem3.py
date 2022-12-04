def message(current_messages: dict, sender_name: str, received_name: str):
    if sender_name in current_messages and received_name in current_messages:
        current_messages[sender_name]['sent'] += 1
        current_messages[received_name]['received'] += 1
        if current_messages[sender_name]['sent'] + current_messages[sender_name]['received'] >= capacity:
            print(f"{sender_name} reached the capacity!")
            del current_messages[sender_name]
        if current_messages[received_name]['received'] + current_messages[received_name]['sent'] >= capacity:
            print(f"{received_name} reached the capacity!")
            del current_messages[received_name]

    return current_messages


def add(current_messages: dict, user_to_add: str, count_of_sent: int, count_of_received: int):
    if user_to_add in current_messages:
        return current_messages
    else:
        current_messages[user_to_add] = {'sent': count_of_sent, 'received': count_of_received}
    return current_messages


def empty(current_messages: dict, user_to_remove: str):
    if user_to_remove == "All":
        current_messages = {}
    elif user_to_remove in current_messages:
        del current_messages[user_to_remove]
    return current_messages


capacity = int(input())
messages = {}
data = input()

while data != "Statistics":
    data = data.split('=')
    if data[0] == "Add":
        messages = add(messages, data[1], int(data[2]), int(data[3]))
    elif data[0] == "Message":
        messages = message(messages, data[1], data[2])
    elif data[0] == "Empty":
        messages = empty(messages, data[1])
    data = input()

print(f"Users count: {len(messages)}")
[print(f"{user} - {stats['sent'] + stats['received']}") for user, stats in messages.items()]
