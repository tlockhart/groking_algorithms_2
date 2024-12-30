# Global variable defined
voted = {}
def check_voter(name):
    if name in voted:
        print("kick them out!")
    else:
        # Add Todd to the voted Hash
        voted[name] = True
        print("let them vote!")
        
check_voter("Tod")
print(voted)