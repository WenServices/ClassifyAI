test_cases = [
    # Buy - Stocks - Question
    {
        "name": "buy_stocks_question_case",
        "input": {
            "model": "finance",
            "input": "Should I buy more stocks now?",
            "reference_id": "FinanceQuery1",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "FinanceQuery1",
            "input_type": "Question",
            "asset_class": "Stocks",
            "financial_action": "Buy",
        },
        "repeat": 1,
    },
    # Sell - Bonds - Statement
    {
        "name": "sell_bonds_statement_case",
        "input": {
            "model": "finance",
            "input": "I sold my bonds today.",
            "reference_id": "FinanceQuery2",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "FinanceQuery2",
            "input_type": "Statement",
            "asset_class": "Bonds",
            "financial_action": "Sell",
        },
        "repeat": 1,
    },
    # Research - Real Estate - Question
    {
        "name": "research_real_estate_question_case",
        "input": {
            "model": "finance",
            "input": "How do I research real estate investment opportunities?",
            "reference_id": "FinanceQuery3",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "FinanceQuery3",
            "input_type": "Question",
            "asset_class": "RealEstate",
            "financial_action": "Research",
        },
        "repeat": 1,
    },
    # Hold - Other - Question
    {
        "name": "hold_other_question_case",
        "input": {
            "model": "finance",
            "input": "Should I hold onto my other investments?",
            "reference_id": "FinanceQuery5",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "FinanceQuery5",
            "input_type": "Question",
            "asset_class": "Other",
            "financial_action": "Hold",
        },
        "repeat": 1,
    },
]
