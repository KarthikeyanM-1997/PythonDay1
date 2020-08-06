from functools import reduce

l1 = [3, 1, 4, 2, 5]

l1.sort()

print(l1)


def sqrFun(n):
    return n * n


x = map(sqrFun, l1)

print(x)

l = [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    }
]

print(l[1]['value'])

for x in l:
    print(x['value'])


py = {'Python': 'Rocks', 'inferior': ['fortran', 'cobol']}

print(py['inferior'])


junk = {
    "characters": {
        "Lonestar": {
            "id": 55923,
            "role": "renegade",
            "items": [
                "space winnebago",
                "leather jacket"
            ]
        },
        "Barfolomew": {
            "id": 55924,
            "role": "mawg",
            "items": [
                "peanut butter jar",
                "waggy tail"
            ]
        },
        "Dark Helmet": {
            "id": 99999,
            "role": "Good is dumb",
            "items": [
                "Shwartz",
                "helmet"
            ]
        },
        "Skroob": {
            "id": 12345,
            "role": "Spaceballs CEO",
            "items": [
                "luggage"
            ]
        }
    }
}


for x in junk['characters']:
    print(junk['characters'][x]['role'])


for x in junk['characters']:
    print(junk['characters'][x]['items'])


omg = {2: [1, 2, 3], 'a': {'b': {'c': {'d': {'e': [1, 2, 3]}}}}}


print(omg[2][0])
print(omg[2])

print(omg["a"])

print(omg["a"]['b'])

print(omg["a"]['b']['c'])

print(omg["a"]['b']['c']['d'])

print(omg["a"]['b']['c']['d']['e'])

omg["a"]['b']['c']['d']['e'] = ['Chera', 'Chola', 'Pandiya']

print(omg["a"]['b']['c']['d']['e'])


body = {
    'query': {
        'filtered': {
            'query': {
                'match': {'description': 'addictive'}
            },
            'filter': {
                'term': {'created_by': 'Mats'}
            }
        }
    }
}

print(body["query"]['filtered']['filter']['term']['created_by'])

movie_box = {
    "Robin Hood: Men in Tights": {
        "imdb_stars": 6.7,
        "length": 104,
        "stars": [{"name": "Cary Elwes", "imdb": "nm0000144", "role": "Robin Hood"},
                  {"name": "Richard Lewis", "imdb": "nm0507659", "role": "Prince John"}]
    }
}

print(movie_box["Robin Hood: Men in Tights"]['imdb_stars'])

print(movie_box["Robin Hood: Men in Tights"]['length'])


"""Task 2"""

numbers = [0, 1, 2, 3, 4]

flag = 0
if(all(numbers[i] <= numbers[i + 1] for i in range(len(numbers)-1))):
    flag = 1

if (flag):
    print("Yes, List is sorted.")
else:
    print("No, List is not sorted.")


def reverseWord(word):
    rev_word = word[::-1]
    return rev_word;


wordList = ["dcba", "apple", "elppa", "abcd", "abc"]

for word in wordList:
    if reverseWord(word) in wordList:
        print(word + " : " + reverseWord(word));   
