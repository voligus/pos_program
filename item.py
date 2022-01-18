class Item:
    def __init__(self, num: str, name: str, cost: str, amount: int = 0):
        self.item_id = num
        self.item_name = name
        self.item_cost = cost
        self.item_amount = amount