class Package:
    def __init__(self, name, price, options):
        self.name = name
        self.price = price
        self.options = options
    
    def toDict(self):
        return {
            "name": self.name,
            "price": self.price,
            "options": self.options
        }

packages = [
    Package("Basic", "100$", ["3 pages", "Web hosting assistance", "2 revisions"]),
    Package("Advanced", "200$", ["5 pages", "Web hosting assistance", "4 revisions", "Simple backend"]),
    Package("Buiness", "350$", ["10 pages", "Web hosting assistance", "6 revisions", "Advanced backend", "Database"])
]
