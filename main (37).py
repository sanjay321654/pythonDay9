from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
total_bidders = {}
def find_highbid(bidding_record):
  high_bid = 0
  for bidder in bidding_record:
    bid_money = bidding_record[bidder]
    if bid_money > high_bid:
      high_bid = bid_money
      winner = bidder
  print(f"The winner is {winner} with a bid of ${high_bid}")

def bidding():
  print("Welcome to the secret auction program.")
  name = input("what is your name?: ")
  bid_amount = int(input("What's your bid?: $"))
  total_bidders[name] = bid_amount
bidding()
def extra_bidders():
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_bidders == "yes":
    clear()
    bidding()
    extra_bidders()
  else:
    find_highbid(bidding_record=total_bidders)
extra_bidders()

  
  