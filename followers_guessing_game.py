import random
data = [
{
    "name": "Priyanka Chopra",
    "followers": 93,
    "proffesion": "Actress"
},
{
    "name": "Shraddha Kapoor",
    "followers": 94,
    "proffesion": "Actress"
},
{
    "name": "Alia Bhatt",
    "followers": 86,
    "proffesion": "Actress"
},
{
    "name": "Deepika Padukone",
    "followers": 80,
    "proffesion": "Actress"
},
{
    "name": "Karan Aujla",
    "followers": 11,
    "proffesion": "Singer"
},
{
    "name": "Salman Khan",
    "followers": 71,
    "proffesion": "Actor"
},
{
    "name": "Akshay Kumar",
    "followers": 67,
    "proffesion": "Actor"
},
{
    "name": "Rohit Sharma",
    "followers": 44,
    "proffesion": "Actress"
},
{
    "name": "Ranveer Singh",
    "followers": 47,
    "proffesion": "Actor"
},
{
    "name": "Hrithik Roshan",
    "followers": 48,
    "proffesion": "Actor"
},
{
    "name": "CarryMinati",
    "followers": 21,
    "proffesion": "YouTuber/Content Creator"
},
{
    "name": "Bhuvan Bam",
    "followers": 21,
    "proffesion": "YouTuber/Content Creator"
},
{
    "name": "Ashish Chanchlani",
    "followers": 18,
    "proffesion": "YouTuber/Content Creator"
}
]

print("You have to guess who have the highest followers, you have 10 attempts for that")
attempts = 10





a = 0
b = 10

while a is not True:
    random_celevrity = random.choice(data)
    random_celebrity = random.choice(data)
    if random_celebrity == random_celevrity:
        random_celevrity = random.choice(data)



    print(f"A : Name: {random_celebrity['name']}, Profession: {random_celebrity['proffesion']}")
    print("VS")
    print(f"B : Name: {random_celevrity['name']}, Profession: {random_celevrity['proffesion']}")

    guess_celebrity = input("Who Have More Instagram Followers Guess Celebrity? ")
    if guess_celebrity == "A":
        if random_celebrity["followers"] > random_celevrity["followers"]:
            print("Right")
            a += 1
            if a == 10:
                print("Congratulations, You Won With 10 Points")
                a= True


        elif random_celebrity['followers'] < random_celevrity['followers']:
                print("Wrong")
                a += 0
                print(a)
                a = True

    if guess_celebrity == "B":

        if random_celebrity["followers"] < random_celevrity["followers"]:
            print("Right")
            a += 1
            if a == 10:
                print("Congratulations, You Won With 10 Points")
                a = True

        elif random_celebrity['followers'] > random_celevrity['followers']:
            print("Wrong")
            a += 0
            print(a)
            a = True


















