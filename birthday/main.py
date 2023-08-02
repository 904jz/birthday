import smtplib
import datetime as dt
import random
import pandas

# Set Current Day
today = dt.datetime.today()
my_email = 'YOUR EMAIL HERE'

# Make dataframe from birthday file
df = pandas.read_csv('birthdays.csv')


for index, row in df.iterrows():
    if row['month'] == today.month and row['day'] == today.day:
        name = row['name']
        email = row['email']

        # Choose random letter from templates
        letter = str(random.choice([1,2,3]))

        #Check to see if milestone birthday

        if (today.year - row['year']) %5 == 0:
            letter = 'milestone'
            age = today.year - row['year']

        with open(f'letter_templates/letter_{letter}.txt', 'r') as to_send:
            # Store letter and replace placeholder with name of birthday person
            output = to_send.read()
            if letter == 'milestone':
                output.replace('[YEAR]',f'{age}th')
            final = output.replace('[NAME]', f'{name}')
        
        # use smtp protocol to send letter as email
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password='YOUR PASSWORD HERE')
            connection.sendmail(from_addr=my_email, to_addrs=f'{email}',
                                msg=f'Subject:Happy Birthday\n\n{final}')
            connection.close()


            
