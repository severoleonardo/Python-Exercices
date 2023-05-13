def get_user_info():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email_adress = input("What is your email address? ")
    phone_number = input("What is your phone number? ")
    job_title = input("What is your job title? ")
    id_number = input("What is your ID number? ")
    
    return (first_name, last_name, email_adress, phone_number, job_title, id_number)

def format_id_card(first_name, last_name, email_adress, phone_number, job_title, id_number):
    return f"The ID Card is: \n_______________________________\n{last_name.upper()}, {first_name.title()} \n{job_title.title()} \nID: {id_number} \n\n{email_adress} \n{phone_number}\n_______________________________\n"

# solicita informações do usuário
user_info = get_user_info()

# formata o cartão de identificação
id_card = format_id_card(*user_info)

# exibe o cartão de identificação
print(id_card)



hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month = input("Mont: ")