# Data Dictionary

This document contains the definitions for the features in the dataset. It is a listing of the data objects (names and definitions) in the provided dataset.

## Definitions

This section covers some terminology to remove ambiguity from the document.

- A *dataset* refers to the collection of row records organized by column features (eg. there are ~30k rows in the dataset).
- A *field* refers to a column feature in the original dataset (eg. there are k = 14 fields in the dataset).
- A field *identifier* refers to the machine-readable name assigned to a particular field in the original dataset (eg. the 10th field has the identifier `Gtin`).
- A field *name* refers to the human-readable display name assigned to a field (eg. `"Lot Number"` refers to the field with identifier `Gtin`).
- A field *description* refers to the explanatory text describing that field.
- A field *type* refers to the representation format the underlying data in a field takes.
  - A *text* field contains a character sequence.
  - A *integer* field contains whole numbers.
  - A *double* field contains floating-point numeric values.
  - A *boolean* field contains a binary category that can either be `True` or `False` (or equivalent proxies).
  - A *datetime* field contains a timestamp, date, or both.
  - A *category* field contains a limited set of possible *values*.
- A field *format* refers to an (optional) format constraint on how the data is presented in the dataset.

## Content

[PromptCloud](https://www.promptcloud.com/) extracted a sample of 30,000 records from Walmart's website, cultivating datasets on product reviews, pricing, and product categories. This dataset is specifically concerned with product pricing.

According to the dataset maintainers:

> We saw that there was a large need for datasets of different types of Products across the largest eCommerce websites around the globe. Although Amazon is the largest in the world and is the most searched in the globe. Walmart makes a strong case for itself in the field of eCommerce as it has been around for years now catering to the average American families daily. We thought that this data and information could be helpful to customers, clients and various other people interested in data of different types to use this to come up with a case study or an article or anything that can be used by the common man and competitors to position themselves strongly in the market. Data is wealth in today's modern era and data is the forefront of the world helping in machine learning and NLP. This is the reason why we wanted to come up with this particular dataset.

The raw dataset is provided in a compressed format as `walmart-product-data-2019.zip` and can be downloaded from the [Kaggle dataset page](https://www.kaggle.com/promptcloud/walmart-product-data-2019). A single `*.csv` containing all 30,000 records can be extracted from the `*.zip` file (`home/sdf/marketing_sample_for_walmart_com-ecommerce__20191201_20191231__30k_data.csv`).

## Field Glossary

Field | Identifier        | Name            | Type       | Description                                   | Format
------|-------------------|-----------------|------------|-----------------------------------------------|-----------------------------------------------------------
1     | `Uniq Id`         | Unique ID       | `text`     | The unique ID given to a product by Walmart.  | `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` (36 letters/digits)
2     | `Crawl Timestamp` | Timestamp       | `datetime` | The date at which the data was crawled.       | `YYYY-MM-DD HH:MM:SS +TTTT`
3     | `Product Url`     | URL             | `text`     | Link to product on Walmart website.           | `https://www.walmart.com/ip/<Product Name>/<Lot Number>`
4     | `Product Name`    | Name            | `text`     | Plaintext listed name of the product.         | `<Product Name>`
5     | `Description`     | Description     | `text`     | Plaintext description of the product.         | `<Disclaimer>, <Description>`
6     | `List Price`      | Price           | `double`   | Listed price of the product.                  | `#0.00` (Currency in USD 2019)
7     | `Sale Price`      | Discount        | `double`   | Discounted price of the product.              | `#0.00` (Currency in USD 2019)
8     | `Brand`           | Brand           | `text`     | Name of product brand                         | `<Brand Name>`
9     | `Item Number`     | Item Number     | `integer`  | Unique product number assigned by Walmart.    | `xxxxxxxxx` (9 digits)
10    | `Gtin`            | Lot Number      | `integer`  | Walmart lot number using a GTIN.              | `xxxxxxxxx` (9 digits)
11    | `Package Size`    | Size            | `null`     | Size of the package when the product arrived. | No values supplied.
12    | `Category`        | Category        | `text`     | Product category as classified by Walmart.    | `<Primary Category>, <Secondary Category>...`
13    | `Postal Code`     | Postal Code     | `null`     | Postal code of the country or region.         | No values supplied.
14    | `Available`       | Is Purchasable? | `boolean`  | If the product is currently purchaseable.     | `[true, false]`

Read more about the [GTIN](https://www.barcode.graphics/attention-walmart-suppliers-cleanup-needed-in-the-gtin-aisle/).
