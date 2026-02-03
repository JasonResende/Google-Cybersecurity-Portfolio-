# Python script to remove prohibited IP addresses from an allow list
# This mimics the logic used in the Google Cybersecurity Professional Certificate labs

def update_file(import_file, remove_list):
    # 1. Open the file and read its contents
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # 2. Convert the string into a list for easier manipulation
    ip_addresses = ip_addresses.split()

    # 3. Iterate through the remove_list
    for element in remove_list:
        # If the IP is in our list, remove it
        if element in ip_addresses:
            ip_addresses.remove(element)

    # 4. Rejoin the list into a string to write back to the file
    ip_addresses = "\n".join(ip_addresses)

    # 5. Write the updated list back to the file
    with open(import_file, "w") as file:
        file.write(ip_addresses)
    
    print("Allow list successfully updated.")

# Example usage:
# update_file("allow_list.txt", ["192.168.1.1", "10.0.0.5"])