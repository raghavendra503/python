data = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

print(type(data))

print(data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["GlossDef"]["GlossSeeAlso"][1])



info = {
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}

for key, value in info.items():
    if isinstance(value,str):
        print(key.upper().ljust(15), ":" , value)

    elif isinstance(value,dict):
        for skey, svalue in value.items():
            print(key.upper()+" "+ skey.upper().ljust(15)+": ",svalue)


        
# print("ID : " + info["id"])
# print(info["type"])
# print(info["name"])
# print(info["image"]["url"][0])
# sample output:

# ID              : 0001
# TYPE            : donut
# NAME            : Cake
# IMAGE URL       :"images/0001.jpg
# IMAGE WIDTH     : 200
# IMAGE HEIGHT    : 200
# THUMBNAIL URL   : "images/thumbnails/0001.jpg"
# THUMBNAIL WIDTH : 32
# THUMBNAIL HEIGHT:  32


# -----------

listData= [
  {
    "login": "mojombo",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://avatars0.githubusercontent.com/u/1?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/mojombo",
    "html_url": "https://github.com/mojombo",
    "followers_url": "https://api.github.com/users/mojombo/followers",
    "following_url": "https://api.github.com/users/mojombo/following{/other_user}",
    "gists_url": "https://api.github.com/users/mojombo/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/mojombo/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/mojombo/subscriptions",
    "organizations_url": "https://api.github.com/users/mojombo/orgs",
    "repos_url": "https://api.github.com/users/mojombo/repos",
    "events_url": "https://api.github.com/users/mojombo/events{/privacy}",
    "received_events_url": "https://api.github.com/users/mojombo/received_events",
    "type": "User",
    "site_admin": False
  },
  {
    "login": "defunkt",
    "id": 2,
    "node_id": "MDQ6VXNlcjI=",
    "avatar_url": "https://avatars0.githubusercontent.com/u/2?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/defunkt",
    "html_url": "https://github.com/defunkt",
    "followers_url": "https://api.github.com/users/defunkt/followers",
    "following_url": "https://api.github.com/users/defunkt/following{/other_user}",
    "gists_url": "https://api.github.com/users/defunkt/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/defunkt/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/defunkt/subscriptions",
    "organizations_url": "https://api.github.com/users/defunkt/orgs",
    "repos_url": "https://api.github.com/users/defunkt/repos",
    "events_url": "https://api.github.com/users/defunkt/events{/privacy}",
    "received_events_url": "https://api.github.com/users/defunkt/received_events",
    "type": "User",
    "site_admin": False
  }
]
  # program to write keys and values
for value in listData:
    for key,values in value.items():
        print(key.ljust(15),":",values)

colors = [
{
"colors": "red",
"values": "#f00"
},
{
"colors": "green",
"values": "#0f0"
},
{
"colors": "blue",
"values": "#00f"
},
{
"colors": "cyan",
"values": "#0ff"
},
{
"colors": "magenta",
"values": "#f0f"
},
{
"colors": "yellow",
"values": "#ff0"
},
{
"colors": "black",
"values": "#000"
}
]

for value in colors:
    print (value["colors"].ljust(10), value["values"])


# write a program to display all the colors and its values.

# sample output :

# red #f00
# green #0f0
# yellow  #ff0
# magenta #f0f
# ..
# ..
# ..

####################################################



data1 = {
    'Sales': {
        'North': {
            'Alice': 'Manager',
            'Bob': 'Sales Executive',
            'Eve': 'Sales Coordinator',
            'John': 'Account Manager'
        },
        'South': {
            'Charlie': 'Sales Executive',
            'Grace': 'Regional Sales Manager',
            'Mallory': 'Business Development Associate'
        },
        'West': {
            'Oscar': 'Sales Executive',
            'Peggy': 'Account Executive',
            'Victor': 'Territory Sales Manager'
        }
    },
    'Marketing': {
        'Digital': {
            'David': 'SEO Specialist',
            'Hannah': 'Content Strategist',
            'Irene': 'Social Media Manager'
        },
        'Offline': {
            'Eve': 'Event Coordinator',
            'Jake': 'Brand Manager',
            'Liam': 'Public Relations Specialist'
        },
        'Research': {
            'Mia': 'Market Research Analyst',
            'Noah': 'Customer Insights Manager'
        }
    },
    'IT': {
        'Infrastructure': {
            'Quinn': 'Network Engineer',
            'Riley': 'System Administrator',
            'Sam': 'Cloud Architect'
        },
        'Development': {
            'Tina': 'Software Engineer',
            'Uma': 'Backend Developer',
            'Walter': 'Full Stack Developer'
        }
    },
    'HR': {
        'Recruitment': {
            'Yara': 'Recruitment Specialist',
            'Zane': 'Talent Acquisition Manager',
            'Nina': 'HR Coordinator'
        },
        'Employee Relations': {
            'Oliver': 'Employee Relations Specialist',
            'Sophia': 'HR Business Partner'
        }
    },
    'Finance': {
        'Accounting': {
            'Xander': 'Accountant',
            'Yvette': 'Accounts Payable Specialist',
            'Zara': 'Financial Analyst'
        },
        'Audit': {
            'Luna': 'Internal Auditor',
            'Mason': 'Compliance Officer'
        }
    }
}

for dept in data1:
        print(dept)
        print("------")
        for subdept in data1[dept]:
            print(subdept)

# write a program to display the below output:


# Sales
# -----
# North
# South
# West



#######################################################
# write a program to display the below output


# 192.168.0.1
# 192.168.0.2
# 192.168.0.3
# ..
# ..
# ..
# 192.168.0.100


value ="192.168.0"
for i in range(1,101):
   print(value  +"." + str(i))


# write a program to display the below output


# 192.168.0.1
# 192.168.0.2
# 192.168.0.3
# ..
# ..
# ..
# 192.168.0.100
# 192.168.1.1
# 192.168.1.2
# 192.168.1.3
# ..
# ..
# ..
# 192.168.1.100

value ="192.168.{}.{}"
for val in range(0,2):
    for subval in range(0,101):
        print(value.format(val, subval))
