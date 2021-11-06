# preprocessing/__init__.py
import logging

def prepare_logger():
    # Prepare the logging format and level.
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

# Constant with fields.
FIELDS = {
    "id": "Uniq Id",
    "timestamp": "Crawl Timestamp",
    "url": "Product Url",
    "name": "Product Name",
    "description": "Description",
    "list.price": "List Price",
    "sale.price": "Sale Price",
    "brand": "Brand",
    "item.num": "Item Number",
    "gtin": "Gtin",
    "pkg.size": "Package Size",
    "category": "Category",
    "zipcode": "Postal Code",
    "available": "Available",    
}

# Filtering of the data frame.

# Walmart-specific fields to remove.
WALMART_FIELDS = [
    FIELDS.get("id"),
    FIELDS.get("url"),
    FIELDS.get("item.num"),
    FIELDS.get("gtin"),
    FIELDS.get("available")
]

# Empty fields to remove.
EMPTY_FIELDS = [
    FIELDS.get("pkg.size"),
    FIELDS.get("zipcode")
]