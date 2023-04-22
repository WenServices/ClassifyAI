test_cases = [
    # Question - Product
    {
        "name": "question_product_case",
        "input": {
            "model": "ecommerce",
            "input": "What are the features of the new phone model?",
            "reference_id": "ProductQuery1",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "ProductQuery1",
            "request_type": "Question",
            "requestScope": "Product",
        },
        "repeat": 1,
    },
    # Question - Order
    {
        "name": "question_order_case",
        "input": {
            "model": "ecommerce",
            "input": "Where is my order?",
            "reference_id": "OrderQuery1",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "OrderQuery1",
            "request_type": "Question",
            "requestScope": "Order",
        },
        "repeat": 1,
    },
    # Statement - Product
    {
        "name": "statement_product_case",
        "input": {
            "model": "ecommerce",
            "input": "The new phone model has a larger screen.",
            "reference_id": "ProductQuery2",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "ProductQuery2",
            "request_type": "Statement",
            "requestScope": "Product",
        },
        "repeat": 1,
    },
    # Statement - Order
    {
        "name": "statement_order_case",
        "input": {
            "model": "ecommerce",
            "input": "I received my order today.",
            "reference_id": "OrderQuery2",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "OrderQuery2",
            "request_type": "Statement",
            "requestScope": "Order",
        },
        "repeat": 1,
    },
    # Question - Other
    {
        "name": "question_other_case",
        "input": {
            "model": "ecommerce",
            "input": "What is the meaning of life?",
            "reference_id": "OtherQuery1",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "OtherQuery1",
            "request_type": "Question",
            "requestScope": "Other",
        },
        "repeat": 1,
    },
]
