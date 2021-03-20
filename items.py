#список всех снаряжений
allEquipment = {
        "defend" : [
                {
                        "name": "Шлем",
                        "type": "defend",
                        "pr": 20,
                        "defend": 32
                },
                {
                        "name": "Перчатки",
                        "type": "defend",
                        "pr": 20,
                        "defend": 20,
                        "attack": 20
                },
                {
                        "name": "Кольчуга",
                        "type": "defend",
                        "pr": 30,
                        "defend": 40
                },
        ],
        "magic": [
                {
                        "name": "Магическая палочка",
                        "type": "magic",
                        "pr": 5,
                        "attack": 70
                },
                {
                        "name": "Заклинание 'Огненный шар'",
                        "type": "magic",
                        "pr": 20,
                        "attack": 25
                },
                {
                        "name": "Кулон",
                        "type": "magic",
                        "pr": 20,
                        "defend": 22,
                        "attack": 20
                },
        ],
        "fisycAttack": [
                {
                        "name": "Меч",
                        "type": "fisycAttack",
                        "pr": 20,
                        "attack": 25
                },
                {
                        "name": "Кинжал",
                        "type": "fisycAttack",
                        "pr": 15,
                        "attack": 20
                },
                {
                        "name": "Топор",
                        "type": "fisycAttack",
                        "pr": 5,
                        "attack": 70
                },
        ],
        "item": [
                {
                        "name": "Тотем бессмертия",
                        "pr": 1,
                        "ability":"second_live"
                },
                {
                        "name": "Лечебные травы",
                        "ability":"health",
                        "pr": 10,
                        "health": 20
                }
        ]
}