class Enum:
    pass


from enums import Enum

# 枚举定义账户类型
AccountType = ["支付宝", "微信", "现金", "银行卡"]

BillType = ["支出", "收入"]

# 枚举定义一级类型
class CategoryLevel1(Enum):
    FOOD = "餐饮"
    TRANSPORTATION = "交通"
    HOUSING = "住房"
    ENTERTAINMENT = "娱乐"
    OTHER = "其他"


# 枚举定义二级类型
class CategoryLevel2(Enum):
    # 一级类型为"餐饮"的二级类型
    BREAKFAST = "早餐"
    LUNCH = "午餐"
    DINNER = "晚餐"

    # 一级类型为"交通"的二级类型
    BUS = "公交"
    SUBWAY = "地铁"
    TAXI = "出租车"

    # 一级类型为"住房"的二级类型
    RENT = "房租"
    UTILITIES = "水电费"

    # 一级类型为"娱乐"的二级类型
    MOVIES = "电影"
    CONCERTS = "音乐会"
    GAMES = "游戏"

    # 一级类型为"其他"的二级类型
    SHOPPING = "购物"
    MEDICAL = "医疗"
    DONATION = "捐赠"


# 构建 categories 的 JSON 数据
categories = [
    {
        "level": 1,
        "type": CategoryLevel1.FOOD,
        "name": CategoryLevel1.FOOD,
        "sub": [
            {
                "level": 2,
                "type": CategoryLevel2.BREAKFAST,
                "name": CategoryLevel2.BREAKFAST
            },
            {
                "level": 2,
                "type": CategoryLevel2.LUNCH,
                "name": CategoryLevel2.LUNCH
            },
            {
                "level": 2,
                "type": CategoryLevel2.DINNER,
                "name": CategoryLevel2.DINNER
            }
        ]
    },
    {
        "level": 1,
        "type": CategoryLevel1.TRANSPORTATION,
        "name": CategoryLevel1.TRANSPORTATION,
        "sub": [
            {
                "level": 2,
                "type": CategoryLevel2.BUS,
                "name": CategoryLevel2.BUS
            },
            {
                "level": 2,
                "type": CategoryLevel2.SUBWAY,
                "name": CategoryLevel2.SUBWAY
            },
            {
                "level": 2,
                "type": CategoryLevel2.TAXI,
                "name": CategoryLevel2.TAXI
            }
        ]
    },
    {
        "level": 1,
        "type": CategoryLevel1.HOUSING,
        "name": CategoryLevel1.HOUSING,
        "sub": [
            {
                "level": 2,
                "type": CategoryLevel2.RENT,
                "name": CategoryLevel2.RENT
            },
            {
                "level": 2,
                "type": CategoryLevel2.UTILITIES,
                "name": CategoryLevel2.UTILITIES
            }
        ]
    },
    {
        "level": 1,
        "type": CategoryLevel1.ENTERTAINMENT,
        "name": CategoryLevel1.ENTERTAINMENT,
        "sub": [
            {
                "level": 2,
                "type": CategoryLevel2.MOVIES,
                "name": CategoryLevel2.MOVIES
            },
            {
                "level": 2,
                "type": CategoryLevel2.CONCERTS,
                "name": CategoryLevel2.CONCERTS
            },
            {
                "level": 2,
                "type": CategoryLevel2.GAMES,
                "name": CategoryLevel2.GAMES
            }
        ]
    },
    {
        "level": 1,
        "type": CategoryLevel1.OTHER,
        "name": CategoryLevel1.OTHER,
        "sub": [
            {
                "level": 2,
                "type": CategoryLevel2.SHOPPING,
                "name": CategoryLevel2.SHOPPING
            },
            {
                "level": 2,
                "type": CategoryLevel2.MEDICAL,
                "name": CategoryLevel2.MEDICAL
            },
            {
                "level": 2,
                "type": CategoryLevel2.DONATION,
                "name": CategoryLevel2.DONATION
            }
        ]
    },
]
