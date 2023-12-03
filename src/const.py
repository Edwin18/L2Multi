# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#MOSCOW
DEFAULT_EVENT_TIME_ZONE = "Europe/Moscow"
DEFAULT_EVENT_SCHEDULED_TIME = 5000

# TODO: Добавить дефолтный меседж для тост уведомлений, на каждый ивент свое сообщение, что на этом ивенте ты можешь получить и количество ну и шуточка)
DEFAULT_EVENTS = {
    "HAPPY_HOUR": {
        "name": "Счастливые Полчаса (+10%)",
        "time": ["01:00", "04:00", "05:30", "07:00", "09:00", "12:00", "14:30", "17:30", "19:00", "22:00"],
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "win": 3,
        "los": 1,
        "msg": "",
    },
    "MAJESTIC_TVT": {
        "name": "Majestic TvT",
        "time": ["09:50", "12:50", "17:50"],
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    },
    "IMPERIAL_TVT": {
        "name": "Imperial TvT",
        "time": ["02:30", "04:30", "15:30", "20:30", "22:30"],
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    },
    "ROYAL_TVT": {
        "name": "Royal TvT",
        "time": ["19:30", "21:30", "23:30"],
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    },
    "LAST_HERO": {
        "name": "Последний Герой",
        "time": ["12:30", "18:30"],
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    },
    "MEAT_GRINDER": {
        "name": "Мясорубка",
        "time": ["07:50", "11:50", "19:50", "23:50"],
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    },
    "ELPY_INVASION": {
        "name": "Нашествие Эльпи",
        "time": ["02:20", "05:20", "10:20", "13:20", "17:20", "19:20", "21:20", "23:20"],
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    },
    "TOVUS_TREASURE": {
        "name": "Сокровище Тову",
        "time": ["00:20", "03:20", "07:20", "11:20", "14:20", "16:20", "20:20", "22:20"],
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    },
    "ALLIANCE_BASE_SIEGE": {
        "name": "Осада Базы Альянса",
        "time": ["19:00"],
        "day": ["Wednesday", "Saturday"],
    },
    "CHAOS_FESTIVAL": {
        "name": "Фестиваль Хаоса",
        "time": [
            "20:00",
            "20:15",
            "20:25",
            "20:35",
            "21:00",
            "21:15",
            "21:25",
            "21:35",
            "22:00",
            "22:15",
            "22:25",
            "22:35",
            "23:00",
            "23:15",
            "23:25",
            "23:35",
        ],
        "day": ["Monday", "Tuesday", "Wednesday", "Thursday"],
    },
}
