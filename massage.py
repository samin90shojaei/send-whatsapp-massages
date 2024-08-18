import pywhatkit

while True:
    try:
        phone_number = str(input('Enter phone number that want to send massage to with your country code : '))
        massage = str(input('Enter massage you want to send : '))
        print('WARNING: please Enter a time that minimumly have 16 seconds distance from now')
        hour = int(input('Enter the hour you want to send massage : '))
        minute = int(input('Enter the minute you want to send massage : '))
        pywhatkit.sendwhatmsg( phone_number, massage, hour, minute)
        print("massage will send in some seconds!")
        break
    except:
        print('you done something wrong')
