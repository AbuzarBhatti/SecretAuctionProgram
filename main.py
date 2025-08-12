more_bidders = 'yes'
bids_data = {}
while more_bidders == 'yes':
    name = input("Enter your name? : ")
    bid  = int(input("Enter your bid? : $ "))
    bids_data[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. : ").lower()
    if more_bidders == 'yes':
        print('\n' * 100)
maximum_bid = 0
winner_person = 'null'
for person in bids_data:
    if bids_data[person] > maximum_bid:
        maximum_bid = bids_data[person]
        winner_person = person
        
print(f'The winner is {winner_person} with a bid of {maximum_bid}')
