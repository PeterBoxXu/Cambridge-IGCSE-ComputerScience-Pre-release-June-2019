#Written by Peter Xu, for Cambridge IGCSE Computer Science exam in June 2019.
#This code illustrates one solution to the Pre-release material associated with the exam,
#feel free to amend the program with the purpose of learning only.
#The Pre-Release Material is a property that belongs to the Cambridge International Examinations Office,
#And the original version of this specific program code is a property that belongs to the individual Xu Haoran himself.

#@@@@@@@@@ Some notes for anyone to examine this code:
#---a.
#In this code, 10 function in total are declared. 
#---b.
#the least number of item recorded is declared to be 3 in the program,
#rather than 10 in the original question.
#This is only for easier testing,
#you can go to *line 93* to alter 4 into 11, in order to make the original question.
#---c.
#On *line 32*, buyer numbers are in a list that is previously stored.
#Since the question do not ask for buyer number recording process,
#I assume that they are previously recorded, so I set up a list on my own.
#---d.
#I know that this code is not perfect, it has some small flaws.
#For example some of the parameters of the functions are not even used in the functions.
#Maybe I can set up some user inputs to use these parameters.
#However the code still works, it is therefore not in urgent need to improve :D
#Another reason is that I don't really have a clear idea on how to use the parameters so...
#@@@@@@@@@

item_numbers = []
descriptions = []
number_of_bids = []
reserve_prices = []
highest_bid_prices = []
buyer_numbers = [1,2,3,4,5]

#These are the lists needed in the identification process
indexes_of_items_over_reserve_prices = []
indexes_of_items_below_reserve_prices = []
total_fees_for_sold_items = []
indexes_of_items_with_no_bids = []

bid_price = 0


def set_up_items(a):
    counter_1 = a

    while True:
        item_number = input('''Insert the item number for item %d
(Enter\'End\' if finished) >>> \n''' % counter_1)
        while True:
            while True:
                try:
                    item_number == 'End' or int(item_number)
                    break
                except ValueError:
                    item_number = input('Not an integer. Numbers must be whole numbers.')
            if item_number == 'End':
                break
            if int(item_number) in item_numbers:
                item_number = input('\nInvalid input. The item with number %r already exists.' % item_number)
            else:
                item_numbers.append(int(item_number))
                break
        if item_number == 'End':
            break

        description = input('Insert the description for the item %r \n' % counter_1)
        descriptions.append(description)

        number_of_bid = 0
        number_of_bids.append(number_of_bid)

        highest_bid_prices.append(bid_price)

        reserve_price = input('Insert the reserve price for the item %r \n' % counter_1)
        while True:
            try:
                float(reserve_price)
                break
            except ValueError:
                reserve_price = input('Not a real number.Prices must be real numbers!')
        reserve_prices.append(reserve_price)

        # To count the items
        counter_1 += 1

#Remember I have changed the number of items to 3 instead of 10, just for easier testing
#however the condition here is 4, it is because counter_1 increments by 1
#after the number of items successfully stored is the previous value of counter_1,
#therefore the boundary should also increments by 1.
#Also it is well worth to note that the condition statement should not be a loop,
#otherwise the register of items would never be terminated, although every item is
#successfully stored/
    if counter_1 < 4 :
        print('***Items not enough. Please enter more.***\n')
        set_up_items(counter_1)


def buyer_identity_confirming(h):
    buyer_number_input = input('Please enter your buyer number >>> ')
    while True:
        if buyer_number_input == 'Cancel':
            print('You have canceled identity confirming.')
            print('^'*20)
            break
        while True:
            try:
                buyer_number_input == 'Cancel' or int(buyer_number_input)
                break
            except ValueError:
                buyer_number_input = input('Remember that numbers must be integers.\n'
                                           'or if you no longer want to bid, insert \'Cancel\'.'
                                           '>>> \n')

        if int(buyer_number_input) in buyer_numbers:
            print('_'*20)
            print('Buyer identity confirmed.\n')
            print('_'*20)
            search_item_input = input('Please enter the item number of the item.\n'
                                      'or if you no longer want to bid, insert \'Cancel\'.\n')
            while search_item_input != 'Cancel':
                while True:
                    try:
                        int(search_item_input)
                        break
                    except ValueError:
                        search_item_input = input('Please enter an integer.\n'
                                                  'or if you no longer want to bid, insert\'Cancel\'.\n'
                                                  '>>>')

                if int(search_item_input) in item_numbers:
                    print('****Item searched.****')
                    k = item_numbers.index(int(search_item_input))
                    display_during_auction(k)
                    buyer_bidding(k)
                    search_item_input = input('\nPlease enter the item number of the item.\n'
                                              'or if you no longer want to bid, insert\'Cancal\'.\n'
                                              '>>>')
                else:
                    search_item_input = input('\nItem not found. Enter the a valid number of the item >>>\n')
            if search_item_input == 'Cancel':
                break
        else:
            buyer_number_input = input('Invalid number. Please enter again.\n'
                                       'or if you no longer want to bid, insert \'Cancel\'.\n'
                                       '>>> ')


def buyer_bidding(m):
    buyers_bid = input('\nWhat is your bid for this item? >>>'
                       'Or insert \'Cancel\' if you want to cancel this bid.\n')
    while True:
        if buyers_bid == 'Cancel':
            print('\nYou have canceled your bidding for this item.\n')
            break
        while True:
            try:
                float(buyers_bid)
                break
            except ValueError:
                buyers_bid = input('\nYour price must be a number.\n'
                                   'or if you do not want to bid, insert \"Cancel\".\n'
                                   '>>>\n ')
        while float(buyers_bid) <= float(highest_bid_prices[m]) :
            buyers_bid = input('Your bid is lower than the current highest bid.'
                               'Please give a higher bid >>> ')
        if float(buyers_bid) > float(highest_bid_prices[m]) :
            highest_bid_prices[m] = buyers_bid
            number_of_bids[m] = number_of_bids[m] + 1
            print('Your bid has been saved! Your bid : %r' %buyers_bid)
            break


def display_during_auction(i):
    print('\n----Item %d ----' %(i+1))
    print('Item number :', item_numbers[i])
    print('Description :', descriptions[i])
    print('Current highest bid :', highest_bid_prices[i],'\n')


def identifying_items_sold(b):
    for b in range(0,len(item_numbers)):
        if number_of_bids[b] == 0:
            indexes_of_items_with_no_bids.append(b)
        else:
            if reserve_prices[b] <= highest_bid_prices[b]:
                indexes_of_items_over_reserve_prices.append(b)

            else:
                indexes_of_items_below_reserve_prices.append(b)


def calculating_total_fees(c):
    for c in range (len(indexes_of_items_over_reserve_prices)):
        total_fee_for_sold_item = 1.1 * float(highest_bid_prices[indexes_of_items_over_reserve_prices[c]])
        total_fees_for_sold_items.append(total_fee_for_sold_item)

#In this function, the parameter i should be indexes_of_items_over_reserve_prices[i],
#and a for loop is needed.
def display_items_sold(d):
    print('\n----Sold item %d ----' %(d+1) )
    print('Item number :', item_numbers[indexes_of_items_over_reserve_prices[d]])
    print('Total fee :', total_fees_for_sold_items[d])


def display_items_with_no_bids(e):
    print('\n----Item %d ----'%(e+1))
    print('Item number :', item_numbers[indexes_of_items_with_no_bids[e]])


def display_items_below_reserved_prices(f):
    print('\n----Item %d' %(f+1))
    print('Item number :', item_numbers[indexes_of_items_below_reserve_prices[f]])
    print('Final bid :',highest_bid_prices[indexes_of_items_below_reserve_prices[f]])


def final_display(g):
    print('~'*20)
    print('\nAt the end of the auction')
    print('~'*20)
    print('\nNumber of items sold :\n', len(indexes_of_items_over_reserve_prices))
    if len(indexes_of_items_over_reserve_prices) != 0:
        print('These are the items sold :')
        for i in range(0,len(indexes_of_items_over_reserve_prices)):
            display_items_sold(i)
    print('~'*20)
    print('\nNumber of items that did not meet the reserve prices :\n', len(indexes_of_items_below_reserve_prices))
    if len(indexes_of_items_below_reserve_prices) != 0:
        print('These are the items that did not meet the reserve prices :')
        for j in range(0,len(indexes_of_items_below_reserve_prices)):
            display_items_below_reserved_prices(j)
    print('~'*20)
    print('\nNumber of items with no bids :\n', len(indexes_of_items_with_no_bids))
    if len(indexes_of_items_with_no_bids) != 0:
        print('These are the items with no bids :\n')
        for k in range(0,len(indexes_of_items_with_no_bids)):
            display_items_with_no_bids(k)
    print('~'*20)



set_up_items(1)
for i in range(0,len(item_numbers)):
    display_during_auction(i)

bidding = True

while bidding:
    buyer_identity_confirming(1)
    bidding = input('\nDo you want to continue bidding? \n'
                    'Insert Any key to continue,\n'
                    '       or\"False\" to stop the whole bidding section.\n')
    if bidding == 'False':
        break
identifying_items_sold(1)
calculating_total_fees(1)
final_display(1)
print('-'*20)
exit_message = input('\n\n\nThat is the end of the auction.')