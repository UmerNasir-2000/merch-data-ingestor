class Item:
    def __init__(self, title, price, image, link, discount):
        self.title = title
        self.price = price
        self.image = image
        self.link = link
        self.discount = discount

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"