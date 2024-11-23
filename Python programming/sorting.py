def insertion_sort_contacts(contacts):
    for i in range(1, len(contacts)):
        current_contact = contacts[i]
        j = i - 1
        while j >= 0 and current_contact['first_name'] < contacts[j]['first_name']:
            contacts[j + 1] = contacts[j]
            j -= 1
        contacts[j + 1] = current_contact

# Example usage:
if __name__ == "__main__":
    contacts = [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Alice', 'last_name': 'Smith'},
        {'first_name': 'Bob', 'last_name': 'Johnson'},
        {'first_name': 'Eve', 'last_name': 'Williams'}
    ]

    print("Before sorting:")
    for contact in contacts:
        print(contact)

    insertion_sort_contacts(contacts)

    print("\nAfter sorting:")
    for contact in contacts:
        print(contact)
