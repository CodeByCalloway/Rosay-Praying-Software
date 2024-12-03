#made by collin calloway
days = ["Monday", "Tuesday", "Wednesday", "thursday", "Friday", "Saturday", "Sunday"]
#Mysteries of the Rosary
joyful_mysteries = ["First Joyful Mystery – The Annunciation of Gabriel to Mary: 'I Desire the Love Of Humility The humility of the Blessed Virgin when the Angel Gabriel greeted her with these words.' Luke 1:26", "Second Joyful Mystery - The Visitation of Mary to Elizabeth: 'I Desire Charity Toward My Neighbor Mary's charity in visiting her cousin Elizabeth and remaining with her for three months before the birth of John the Baptist.' Luke 1:39", "Third Joyful Mystery - The Birth of Jesus: 'I Desire the Love of God The poverty, so lovingly accepted by Mary when she placed the Infant Jesus, our God and Redeemer, in a manger in the stable of Bethlehem.' Luke 2:1", "Fifth Joyful Mystery – Finding Jesus in the Temple: 'I desire Zeal For The Glory Of God The deep sorrow with which Mary sought the Child Jesus for three days, and the joy with which she found Him in the midst of the Teachers of the Temple.' Luke 2:41",]


def run_command(day):
    day = day.lower()  # Convert input to lowercase for easier comparison
    if day == "monday":
        print("You selected Monday!")
        # Add code for Monday
    elif day == "tuesday":
        print("You selected Tuesday!")
        # Add code for Tuesday
    elif day == "wednesday":
        print("You selected Wednesday!")
        # Add code for Wednesday
    elif day == "thursday":
        print("You selected Thursday!")
        # Add code for Thursday
    elif day == "friday":
        print("You selected Friday!")
        # Add code for Friday
    elif day == "saturday":
        print("You selected Saturday!")
        # Add code for Saturday
    elif day == "sunday":
        print("You selected Sunday!")
        # Add code for Sunday
    else:
        print("Invalid input! Please enter a valid day of the week.")

# Ask for input
user_input = input("Enter a day of the week: ").strip()  # Remove any extra spaces
run_command(user_input)
