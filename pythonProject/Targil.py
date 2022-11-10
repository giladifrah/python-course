user = [{'admin': False, 'active': False, 'name': "Gilad"},
        {'admin': True, 'active': False, 'name': "Mikey"},
        {'admin': False, 'active': True, 'name': "Avi"},
        {'admin': True, 'active': True, 'name': "Lidor"},
        ]

for name in user:
    if name['admin']:
        print(f"Admin {name['name']}")
    else:
        print("not admin")

    if name['active']:
        print(f"Active {name['name']}")
    else:
        print("not active")

    if name['admin'] and name['active']:
        print(f"Admin Active {name['name']}")

    if not name['admin'] and not name['active']:
        print(f"{name['name']}")

    print("")
    print("end of iteration")
    print("")
