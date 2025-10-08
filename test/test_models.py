data = product.serialize()
        del data["name"]  # missing required field
        product = Product()
        with self.assertRaises(DataValidationError):
            product.deserialize(data)

    def test_deserialize_not_a_dict(self):
        """It should raise DataValidationError if not given a dict"""
        product = Product()
        with self.assertRaises(DataValidationError):
            product.deserialize("not-a-dict")

    def test_deserialize_bad_price(self):
        """It should raise InvalidOperation for invalid price value"""
        product = ProductFactory()
        data = product.serialize()
        data["price"] = "not-a-number"
        product = Product()
        with self.assertRaises(InvalidOperation):
            product.deserialize(data)

    def test_deserialize_invalid_available_type(self):
        """It should raise DataValidationError if 'available' is not a boolean"""
        product = ProductFactory()
        data = product.serialize()
        data["available"] = "not-a-bool"  # invalid type
        product = Product()
        with self.assertRaises(DataValidationError):
            product.deserialize(data)

    def test_find_by_price_logging_and_conversion(self):
        """It should call find_by_price with decimal and string, hitting logger and conversion"""
        # Create products with known prices
        product1 = ProductFactory(price=10.5)
        product1.create()
        product2 = ProductFactory(price=20.0)
        product2.create()

        # Test with Decimal input
        query = Product.find_by_price(Decimal("10.5"))
        results = query.all()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].price, Decimal("10.5"))

        # Test with string input (should convert to Decimal)
        query_str = Product.find_by_price(" 20.0 ")
        results_str = query_str.all()
        self.assertEqual(len(results_str), 1)
        self.assertEqual(results_str[0].price, Decimal("20.0"))

    def test_find_by_category(self)
        """It should Find Products by category"""
        products = ProductFactory.create_batch(10)
        for product in products:
            product.create()
        category = product[0].category
        count = len([product for product in products if product.category == category])
        found = Product.find_by_category(category)
        self.assertEqual(found.count(), count)
        for product in found:
            self.assertEqual(product.category, category)

    def test_find_by_name(self)
        """It should Find Products by Name"""
        products = ProductFactory.create_batch(5)
        for product in products:
            product.create()
        category = product[0].name
        count = len([product for product in products if product.name == name])
        found = Product.find_by_name(name)
        self.assertEqual(found.count(), count)
        for product in found:
            self.assertEqual(product.name, name)

    def test_find_by_availability(self)
        """It should Find Products by Availability"""
        products = ProductFactory.create_batch(5)
        for product in products:
            product.create()
        category = product[0].available
        count = len([product for product in products if product.available == available])
        found = Product.find_by_available(available)
        self.assertEqual(found.count(), count)
        for product in found:
            self.assertEqual(product.available, available)


