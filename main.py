import random

lover_case = "qwertyuopğasdfghjkizxcvbnm"
upper_case = "QWERTYUOPĞASDFGHJKIZXCVBNM"
numbers = "123456789"
symblos = "!'^+%&/()=?_;>£#${}[]|"

password = lover_case + upper_case + numbers + symblos
length = 24

generate = "".join(random.sample(password,length))

print(generate)
