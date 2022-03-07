import instaloader as load

# get instance
insta = load.Instaloader()


#login
insta.login(username, password)
print("[SUCCESS] logged in")

# alternative login method
# insta.interactive_login   # ask password on terminal

profile = insta
print(profile)