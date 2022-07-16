# Create a program that helps the cafe staff remember which agent prefers which beverage:

# Agent J prefers coffee
# Agent Q prefers decaf coffee
# Agent S prefers coffee
# Agent M prefers tea
# Because coffee is a popular drink, the cafe sometimes runs out of regular coffee. If this happens, Agent S will drink decaf, but Agent J will have tea instead.

import time

agents = ["Jim", "Jack", "Jane", "Mike"]
drinks = {"coffee" : 2, "decaf coffee" : 2, "tea": 2, "water": 2, "orange juice": 2}
preference = {"Jim" : "coffee", "Jack" : "decaf coffee", "Jane" : "coffee", "Mike" : "tea"}
total = sum(drinks.values())

def main():
    total = 10
    while total > 0:
        drinks = order()
        total = sum(drinks.values()) 
#       print (total)
    print('We are closed...')
    # print_dict(drinks)
    # print_list(agents)
    # print_pref(preference)
    # print_agents(agents)
    # print_drinks(drinks)
    print (drinks)
    print (agents)
    print (preference)
    
# Customer order
def order():
    customer_name = input('What is your name? ')
    if customer_name.capitalize() in agents:
        print(f'Welcome {customer_name.capitalize()}')
        if customer_name.capitalize() in preference:
            print (f'Here is your {preference[customer_name.capitalize()]}')
            drinks[preference[customer_name.capitalize()]] -= 1   
            return drinks
    else:
        # Customer not in agents
        print(f'I don\'t know you {customer_name.capitalize()}')
        # add to agents
        agents.append(customer_name.capitalize())
        
        
        # Take order
        while True:
            drink_order = input('What would you like to drink? ')
            if drink_order.lower() in drinks.keys():
                print(f'Hooray! We have {drink_order.capitalize()} available')
                break
            else:
                print(f'We do not carry {drink_order.capitalize()}. \nPlease select from these wonderful options instead!\n')
                for k,v in drinks.items():
                    print(k)
                print()
        # Add key value to preferences
        preference[f'{customer_name.capitalize()}'] = f'{drink_order.lower()}' 
        # Subtract from drink list
        drinks[preference[customer_name.capitalize()]] -= -1
        return drinks

# Remember the customer orders and preferences in a dictionary
# Print the dictionary
# Print the total number of drinks left
# Print the list of agents
# Print the list of drinks
# Print the list of preferences

def print_dict(d):
    for k,v in d.items():
        print(f'{k} : {v}')
    print()
    
def print_list(l):
    for i in l:
        print(i)
    print()

def print_pref(d):
    for k,v in d.items():
        print(f'{k} : {v}')
    print()

def print_agents(l):
    for i in l:
        print(i)
    print()

def print_drinks(l):
    for i in l:
        print(i)
    print()


if __name__ == "__main__":
    main()
