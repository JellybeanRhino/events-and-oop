from dataclasses import dataclass
from PySide6.QtWidgets import *


@dataclass
class Product:
    """Represents a product, with an associated name and price"""

    _name: str
    _price: float
    _has_sugar: bool

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        # Only allow non-empty names
        if new_name:
            self._name = new_name
        else:
            raise ValueError()

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float):
        # Only allow a price above 1 cent
        if new_price >= 0.01:
            self._price = new_price
        else:
            raise ValueError()

    @property
    def has_sugar(self) -> bool:
        return self._has_sugar
    
    @has_sugar.setter
    def has_sugar(self, sugar: bool):
        if sugar == True:
            self._has_sugar = True
        
        else:
            self._has_sugar = False
    
# List of drink products
products = [
    Product("Long Black", 2.00),
    Product("Flat White", 3.50),
    Product("Orange Juice", 3.00),
    Product("Coke", 1.00),
    Product("Fanta", 1.00),
    Product("Water", 4.00)
]

# Set app and main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle("Shop")

# Set main widget and layout
main_widget = QWidget()
right_widget = QWidget()
main_window.setCentralWidget(main_widget)
vbox = QVBoxLayout()
hbox = QHBoxLayout()
right_widget.setLayout(vbox)
main_widget.setLayout(hbox)

# Set up three product widgets
product_combo = QListWidget()
# Adds the names of the products to the combo box
product_combo.addItems([x.name for x in products])
name_label = QLabel("Product name")
price_label = QLabel("Product price")

# Add widgets to vbox layout
hbox.addWidget(product_combo)
vbox.addWidget(name_label)
vbox.addWidget(price_label)
hbox.addWidget(right_widget)

def product_combo_currentRowChanged(index: int):
    """
    Updates the product labels based on the new index
    that was selected.
    """
    # Get the single product from the list using the
    # index passed in as a parameter
    product = products[index]

    # Update the labels
    name_label.setText(product.name)
    price_label.setText(f"${product.price:.2f}")


# Connect the function to the combo box's signal
product_combo.currentRowChanged.connect(product_combo_currentRowChanged)

# Update the labels manually to the 0th item, Long Black
product_combo_currentRowChanged(0)

# Show the window
main_window.show()
app.exec()
