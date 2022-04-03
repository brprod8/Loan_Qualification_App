#  Here is conditonals statements from basic to complex

#              (Basic conditionals)


# 1. @TODO: Create two new variables to hold user data:
# Populate this variable with our first user, who is based in the United States
# and is already registered on the platform.
# YOUR CODE HERE!

location = "United States"
is_registered = True

# 2. @TODO: Write a conditional statement. If user is based in the U.S. and
# already registered, advertise the new service. Otherwise, give them
# notice that the feature is coming soon.
# YOUR CODE HERE!
if location == "United States" and is_registered:
    print("Now Available! Crypto Accepted!")

else:
    print("Crypto Payments - Coming Soon!")

# 3. @TODO: Change the user location to Japan and print the results again.
# Does your conditional statement program work as expected?
# YOUR CODE HERE!
location = "Japan"
is_registered = True

if location == "United States" and is_registered is True:
    print("Now Available! Crypto Accepted!")

else:
    print("Crypto Payments - Coming Soon!")

    #           (Complex conditionals)


issue_currency = "USD"
price = 30.0

# Check if price is not negative (greater than equal to 0)
if price >= 0:
    # If price is not negative and currency is `USD` (Dollar).
    if issue_currency == "USD":
        print("The currency is $", price)
    # If price is not negative and currency is `EUR` (Euro).
    elif issue_currency == "EUR":
        print("The currency is €", price)
    # If anything other than the above.
    else:
        print("The currency is not in USD or EUR.")
else:
    # If price is negative.
    print("Error, the price listed is a negative number")

#                (Nested Conditonals)
# @TODO: Create variables with the initial ad price and company type
# YOUR CODE HERE!
ad_price = 10
company_type = ("Startup".lower())
if ad_price < 20:
    print("buy it")

else:
    print("To expensive to buy")


# @TODO: Convert the following decision logic into valid Python code.

if ad_price < 20:
    if company_type == "startup":
        print('that the expected profit is 500')

    elif company_type == "existing":
        print('that the expected profit is 100')

    else:
        print('that the company type is not specified')

else:
    print('that the ad price is too expensive')
