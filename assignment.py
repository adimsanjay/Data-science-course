# Make it dynamic: means take inputs from user
temp = float(input("Enter the patient's temperature: "))
rtpcr = input("Is the patient's RTPCR test result positive? (Enter 'True' or 'False'): ")

if rtpcr == 'true':

    if temp > 80:
        print('Admit the patient')
    else:
        print('Home Isolation')
else:
    print('Go Home')
