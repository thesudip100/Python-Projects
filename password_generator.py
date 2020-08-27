import string
import random
password_len=int(input("Enter the length of the password you want"))
characters_for_password=string.ascii_letters + string.digits + string.punctuation
print("Your password is:","".join(random.choice(characters_for_password)for i in range(password_len)))

