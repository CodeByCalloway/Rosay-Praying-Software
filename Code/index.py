#made by collin calloway
days = ["Monday", "Tuesday", "Wednesday", "thursday", "Friday", "Saturday", "Sunday"]
#Mysteries of the Rosary
joyful_mysteries = ["First Joyful Mystery – The Annunciation of Gabriel to Mary: 'I Desire the Love Of Humility The humility of the Blessed Virgin when the Angel Gabriel greeted her with these words.' Luke 1:26", "Second Joyful Mystery - The Visitation of Mary to Elizabeth: 'I Desire Charity Toward My Neighbor Mary's charity in visiting her cousin Elizabeth and remaining with her for three months before the birth of John the Baptist.' Luke 1:39", "Third Joyful Mystery - The Birth of Jesus: 'I Desire the Love of God The poverty, so lovingly accepted by Mary when she placed the Infant Jesus, our God and Redeemer, in a manger in the stable of Bethlehem.' Luke 2:1", "Fifth Joyful Mystery – Finding Jesus in the Temple: 'I desire Zeal For The Glory Of God The deep sorrow with which Mary sought the Child Jesus for three days, and the joy with which she found Him in the midst of the Teachers of the Temple.' Luke 2:41",]

luminous_mysteries = ["First Luminous Mystery – The Baptism of Jesus in the River Jordan: 'And a voice came from the heavens saying, “This is my beloved Son, with whom I am well pleased.” ' Matthew 3:17","The Second Luminous Mystery – The Wedding at Cana, Christ Manifested: 'Jesus did this as the beginning of his signs in Cana in Galilee and so revealed his glory, and his disciples began to believe in him.' John 2:11","The Third Luminous Mystery – The Proclamation of the Kingdom of God: 'Jesus came to Galilee proclaiming the gospel of God: “This is the time of fulfillment. The kingdom of God is at hand. Repent, and believe in the gospel.” ' Mark 1:15","The Fourth Luminous Mystery – The Transfiguration of Jesus: 'And he was transfigured before them; his face shone like the sun and his clothes became white as light.' Matthew 17:2","The Fifth Luminous Mystery – The Last Supper, the Holy Eucharist: While they were eating, Jesus took bread, said the blessing, broke it, and giving it to his disciples said, “Take and eat; this is my body.” Then he took a cup, gave thanks, and gave it to them, saying, “Drink from it, all of you, for this is my blood of the covenant, which will be shed on behalf of many for the forgiveness of sins. Matthew 26:26"]

sorrow_mysteries = ["First Sorrowful Mystery – Agony of Jesus in the Garden: 'I Desire True Repentance for My Sins Our Lord Jesus in the garden of Gethsemani, suffering a bitter agony for our sins.' Matthew 26:36","Second Sorrowful Mystery – Jesus is Scourged at the Pillar: 'I Desire a Spirit of Mortification The cruel scourging at the pillar that our Lord suffered; the heavy blows that tore His flesh.' Matthew 27:26","Third Sorrowful Mystery – Jesus is Crowned With Thorns: 'I Desire Moral Courage The crown of sharp thorns that was forced upon our Lord’s Head and the patience with which He endured the pain for our sins.' Matthew 27:27","Fourth Sorrowful Mystery – Jesus Carries His Cross: 'I Desire the Virtue of Patience The heavy Cross, so willingly carried by our Lord, and ask Him to help you to carry your crosses without complaint.' Matthew 27:32","Fifth Sorrowful Mystery – The Crucifixion of Jesus: I Desire the Grace of Final Perseverance The love which filled Christ’s Sacred Heart during His three hours’ agony on the Cross, and ask Him to be with you at the hour of death.' Matthew 27:33"]

glorious_mysteries = ["First Glorious Mystery – The Resurrection of Jesus: 'I Desire a Strong Faith Christ’s glorious triumph when, on the third day after His death, He arose from the tomb and for forty days appeared to His Blessed Mother and to His disciples.' John 20:1","Second Glorious Mystery – The Ascension of Jesus: 'I Desire the Virtue of Hope The Ascension of Jesus Christ, forty days after His glorious Resurrection, in the presence of Mary and His disciples.' Luke 24:36","Third Glorious Mystery – The Descent of the Holy Spirit at Pentecost: I Desire Zeal for the Glory of God The descent of the Holy Spirit upon Mary and the Apostles, under the form of tongues of fire, in fulfillment of Christ’s promise.' Acts 2:1","Fourth Glorious Mystery – The Assumption of Mary into Heaven: I Desire the Grace of a Holy Death The glorious Assumption of Mary into Heaven, when she was united with her Divine Son.' ","Fifth Glorious Mystery – The Coronation of Mary as Queen of Heaven and Earth: 'I Desire a Greater Love for the Blessed Virgin Mary The glorious crowning of Mary as Queen of Heaven by her Divine Son, to the great joy of all the Saints.' "]

def monday():
    #askes the question and is where you input
    instruction_input = input("do you want instructions on praying?").strip().lower()
    #checks responses
    if instruction_input == 'yes':
        print("you selected yes")
    elif instruction_input == 'no':
        print("you selected no")
    else:
        print("please answer with a yes or no.")



def run_command(day):
    day = day.lower()  # Convert input to lowercase for easier comparison
    if day == "monday":
        print("Monday, The day of Joyful Mysteries.")
        monday()
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