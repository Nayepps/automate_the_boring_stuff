
print('What would you like to see?, show_shoes / leave_store')

shoe_dic = {
  "Jordan1": "100",
  "Jordan3": "120",
  "Jordan5": "130",

}
customer_request = raw_input()
if customer_request == 'show_shoes':
    print(shoe_dic)
else:
    print('Have a nice day')

print('What would you like to order?')
order = raw_input()
price = shoe_dic[order]
print("Great choice, your total is $" + price + "how would you like to pay for that? Card or Cash")
total = raw_input()
print("Great I will take that")
