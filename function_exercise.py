# 1
def display_message():
    print("In this chapter,i have learned about Python functions.")
display_message()

#2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("change your thinking")

#3

def makeshirt(size, message):
    print(f"A {size} shirt will be made with the message: {message}")

makeshirt("medium", "Hello, World!")
makeshirt(size="large", message="I <3 Python")

#4
def makeshirt(size="large", message="I love Python"):
    print(f"A {size} shirt will be made with the message: {message}")
makeshirt()
makeshirt("medium")
makeshirt("small", "Python is cool")

#5
def describecity(city, country='Nigeria'):
    print(f"{city} is in {country}.")

describecity("Kaduna")
describecity("Toronto", "Canada")
describecity("London", "UK")


#6
def citycountry(city, country):
    return f"{city.title()}, {country.title()}"
print(citycountry("Nigeria", "Kaduna"))
print(citycountry("England","London"))
print(citycountry("Mumbai", "India"))


#7
def makealbum(artist, title, num_songs=None):
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

album1 = makealbum('The Beatles', 'Sgt. Pepper\'s Lonely Hearts Club Band', 13)
print(album1) 


album2 = makealbum('Pink Floyd', 'The Wall')
print(album2) 

#8

def makealbum(artist, title, num_songs=None):
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

while True:
    artist = input("Enter the album's artist (or 'q' to quit): ")
    if artist == 'q':
        break
    
    title = input("Enter the album's title (or 'q' to quit): ")
    if title == 'q':
        break
    
    num_songs = input("Enter the number of songs on the album (or leave blank if unknown): ")
    
    if num_songs:
        album = makealbum(artist, title, int(num_songs))
    else:
        album = makealbum(artist, title)
    
    print(album)

#9
def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Hello!", "How are you?", "What's up?", "Nice to meet you."]


show_messages(messages)

#10
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
        
messages = ['hello', 'how are you?', 'goodbye']
sent_messages = []

send_messages(messages, sent_messages)

print("Messages:")
print(messages)

print("Sent Messages:")
print(sent_messages)

#11
 messages
messages = ['Hello!', 'How are you?', 'What are you up to?']

# Function to print and move messages
def send_messages(messages):
    sent_messages = []
    while messages:
        message = messages.pop(0)
        print(message)
        sent_messages.append(message)

    return sent_messages

messages_copy = messages.copy()
sent_messages = send_messages(messages)
print("Original messages:", messages_copy)
print("Sent messages:", sent_messages)

#12
def make_sandwich(*items):
    print(f"Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!\n")
    

make_sandwich('ham')
make_sandwich('turkey', 'lettuce', 'mayo')
make_sandwich()

#13
def buildprofile(first, last, **userinfo):
    userinfo['first_name'] = first
    userinfo['last_name'] = last
    return userinfo

user_profile = buildprofile('John', 'Doe', age=30, occupation='Software Engineer', hobby='Reading')
print(user_profile)
user_profile = buildprofile('Alamin','musa')
print(user_profile)

#14
def make_car(manufacturer, model, **car_info):
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car[key] = value
    return car
 
def make_car(manufacturer, model, **car_info):
 
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car[key] = value
    return car
    
car = make_car('Subaru', 'Outback', color='blue', tow_package=True)
print(car)

#15
