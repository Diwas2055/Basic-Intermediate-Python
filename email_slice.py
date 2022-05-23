# Get the user's email address
print("Example : Demo@admin.com")
email = input("What is your email address?: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice out the domain name
# Finding the index of the "@" character in the email string.
domain_name = email[email.index("@")+1:]

# Format message
res = "Your username is '{}' and your domain name is '{}'".format(
    user_name, domain_name)

# Display the result message
print(res)
