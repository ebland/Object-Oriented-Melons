# """Classes for melon orders."""

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        if self.species == "Christmas melon":
            base_price = 7.5
        else:
            base_price = 5
        total = ((1 + self.tax) * self.qty * base_price)
        return total
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

        if qty < 10:
            self.total = get_total() + 3 

    def get_country_code(self):
        """Return the country code."""

        return self.country_code