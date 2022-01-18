class Order:
    def __init__(self, list_stock):
        self.list_stock = list_stock
        self.list_order = []

    def insert_item(self, item):
        self.list_order.append(item)

    def delete_item(self, num_item):
        item = self.list_order[int(num_item)]
        self.list_order.remove(item)