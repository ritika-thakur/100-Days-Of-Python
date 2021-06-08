# This Project has been done on https://replit.com/@appbrewery/blind-auction-start

from replit import cleara
from art import logo

participants = dict()

def auction_winner(auction_participants):
  winner_name= max(auction_participants, key=auction_participants.get) 
  return print(f"The winner is {winner_name} with a bid of {auction_participants[winner_name]}")
      


bidders_left = True
while bidders_left:
  print(logo)
  name = input("What is your name? ")
  bid = int(input("How much would you like to bid? "))
  participants[name] = bid
  next_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
  clear()
  if next_bidder == 'no':
    bidders_left = False
    auction_winner(participants)