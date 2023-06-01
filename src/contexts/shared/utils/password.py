from password_strength import PasswordPolicy, PasswordStats

import bcrypt

class password():
    
    def check_policies(password):
        policy = PasswordPolicy.from_names(
            length=8,  # min length: 8
            uppercase=1,  # need min. 2 uppercase letters
            numbers=1,  # need min. 2 digits
            #special=1,  # need min. 2 special characters
            #nonletters=1,  # need min. 2 non-letter characters (digits, specials, anything)
        )
        return policy.test(password)
    
    def check_stats(password):
        
        stats=PasswordStats(password)
        return stats.strength()
    
    def bcrypt_password(password):
        salt=bcrypt.gensalt(10)
        new_password=bcrypt.hash(password,salt)
        return new_password
    
    
    def generate(password):
        
        salt=bcrypt.gensalt()
        #print(salt)
        hashed=bcrypt.hashpw(password.encode(),salt)
        print(hashed)
        return hashed

