import datetime

def reminder():
    drugs = open('drugsList.txt')
    drug = input('enter the name of the drug: ')
    if drug in drugs:
        pass
    else:
        after_rem = input('after what time to reminder: ')      # через какое время напомнить
        today = datetime.datetime.now().date()                  # !!!

