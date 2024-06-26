from uuid import uuid4
bookstore = {
    "books" : 
        [
    {
        "id": str(uuid4()),
        "name" : "La conquête de l'espace",
        "author" : "Elon Musk",
        "editor" : "Mc Donalds"
    },
    {
        "id": str(uuid4()),
        "name" : "Python pour les nuls",
        "author" : "Benois Frénay",
        "editor" : "Maison Frénay"
    },
    {
        "id": str(uuid4()),
        "name" : "Tchoupi à l'école",
        "author" : "Erwin",
        "editor" : "Kurtis Production"
    },
    {
        "id": str(uuid4()),
        "name" : "La poule et le lapin",
        "author" : "Jean de La Fontaine",
        "editor" : "Edition Hachette"
    },
    {
        "id": str(uuid4()),
        "name" : "Les bons, le con et le mouton",
        "author" : "Ryan, Ilias",
        "editor" : "Universal"
    },
    {
        "id": str(uuid4()),
        "name" : "100 recettes faciles maison",
        "author" : "Agnès Dupont",
        "editor" : "Test cuisine"
    },
    {
        "id": str(uuid4()),
        "name" : "Encyclopédie du football",
        "author" : "Kiki Mbappe",
        "editor" : "Le Football Il a Changé"
    }
    ],
    "users": [
        {
            "id": str(uuid4()),
            "username": "johndu77",
            "firstname" : "John",
            "name" : "Wick",
            "password": "john_password",    
            "email": "John.Wick@gmail.com",
            "admin": True,
            "blocked": False,
            "connected": False
        },
        {
            "id": str(uuid4()),
            "username": "stkiller6972",
            "firstname" : "Steve",
            "name" : "Jobs",
            "password": "steve_password",
            "email": "Steve.Jobs@gmail.com",
            "admin": False,
            "blocked": False,
            "connected": False
        },
    ]
}


