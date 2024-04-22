 # get the # of books purchased from the user
books_purchased = int(input("Enter the number of books you have purchased this month: "))
    
# determine points awarded based on the # of books purchased
if books_purchased >= 8:
    points = 60
elif books_purchased >= 6:
    points = 30
elif books_purchased >= 4:
    points = 15
elif books_purchased >= 2:
    points = 5
else:
    points = 0

# display the # of points awarded
print(f"You have earned {points} points this month.")