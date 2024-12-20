class Item:
    def __init__(
        self,
        title,
        original_price,
        discounted_price,
        image,
        link,
        discount
    ):
        self.title = title
        self.price = {
            "original": original_price,
            "discounted": discounted_price
        }
        self.image = image
        self.link = link
        self.discount = discount

    def __str__(self):
        return (
            f"{self.title}: Original Price: ${self.price['original']:.2f}, "
            f"Discounted Price: ${self.price['discounted']:.2f}"
        )