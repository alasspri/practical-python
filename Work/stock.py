from typedproperty import String, Integer, Float


class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, number):
        self.shares -= number

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
