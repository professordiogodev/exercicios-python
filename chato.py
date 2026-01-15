users = [
    {
        "id": 1,
        "name": "Ana Silva",
        "department": {
            "name": "Sales",
            "manager": "Carlos Almeida"
        },
        "performance": {
            "2020": {
                "Q1": 85,
                "Q2": 90,
                "Q3": 88,
                "Q4": 92
            },
            "2021": {
                "Q1": 91,
                "Q2": 89,
                "Q3": 87,
                "Q4": 93
            }
        }
    },
    {
        "id": 2,
        "name": "João Pereira",
        "department": {
            "name": "Marketing",
            "manager": "Maria Oliveira"
        },
        "performance": {
            "2020": {
                "Q1": 78,
                "Q2": 82,
                "Q3": 80,
                "Q4": 85
            },
            "2021": {
                "Q1": 83,
                "Q2": 84,
                "Q3": 86,
                "Q4": 88
            }
        }
    },
    {
        "id": 3,
        "name": "Sofia Costa",
        "department": {
            "name": "IT",
            "manager": "Paulo Sousa"
        },
        "performance": {
            "2020": {
                "Q1": 92,
                "Q2": 94,
                "Q3": 91,
                "Q4": 93
            },
            "2021": {
                "Q1": 95,
                "Q2": 96,
                "Q3": 94,
                "Q4": 97
            }
        }
    },
    {
        "id": 4,
        "name": "Miguel Martins",
        "department": {
            "name": "Finance",
            "manager": "Joana Figueiredo"
        },
        "performance": {
            "2020": {
                "Q1": 88,
                "Q2": 85,
                "Q3": 89,
                "Q4": 90
            },
            "2021": {
                "Q1": 87,
                "Q2": 88,
                "Q3": 86,
                "Q4": 89
            }
        }
    }
]

print(users[3]["department"]["manager"])