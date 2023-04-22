test_cases = [
    # Acute Symptom
    {
        "name": "acute_symptom_case",
        "input": {
            "model": "healthcare",
            "input": "I have a headache.",
            "reference_id": "AcuteSymptomQuery1",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "AcuteSymptomQuery1",
            "category": "Symptom",
            "subCategory": "Acute symptom",
        },
        "repeat": 1,
    },
    # Chronic Symptom
    {
        "name": "chronic_symptom_case",
        "input": {
            "model": "healthcare",
            "input": "I have been coughing for a month.",
            "reference_id": "ChronicSymptomQuery1",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "ChronicSymptomQuery1",
            "category": "Symptom",
            "subCategory": "Chronic symptom",
        },
        "repeat": 1,
    },
    # Local Symptom
    {
        "name": "local_symptom_case",
        "input": {
            "model": "healthcare",
            "input": "My left knee hurts when I climb stairs.",
            "reference_id": "LocalSymptomQuery1",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "LocalSymptomQuery1",
            "category": "Symptom",
            "subCategory": "Local symptom",
        },
        "repeat": 1,
    },
    # Negative Symptom
    {
        "name": "negative_symptom_case",
        "input": {
            "model": "healthcare",
            "input": "I cannot smell anything.",
            "reference_id": "NegativeSymptomQuery1",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "NegativeSymptomQuery1",
            "category": "Symptom",
            "subCategory": "Negative symptom",
        },
        "repeat": 1,
    },
    # Positive Symptom
    {
        "name": "positive_symptom_case",
        "input": {
            "model": "healthcare",
            "input": "I see things that are not there.",
            "reference_id": "PositiveSymptomQuery1",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "PositiveSymptomQuery1",
            "category": "Symptom",
            "subCategory": "Positive symptom",
        },
        "repeat": 1,
    },
    # Medication
    {
        "name": "medication_case",
        "input": {
            "model": "healthcare",
            "input": "I take aspirin for headaches.",
            "reference_id": "MedicationQuery1",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "MedicationQuery1",
            "category": "Medication",
            "subCategory": "Aspirin",
        },
        "repeat": 1,
    },{
        "name": "medication_case_1",
        "input": {
            "model": "healthcare",
            "input": "I take ibuprofen for my headache.",
            "reference_id": "MedicationQuery2",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "MedicationQuery2",
            "category": "Medication",
            "subCategory": "Ibuprofen",
        },
        "repeat": 1,
    },
    {
        "name": "medication_case_2",
        "input": {
            "model": "healthcare",
            "input": "I am allergic to penicillin.",
            "reference_id": "MedicationQuery3",
            "reference_id_name": "_id",
        },
        "expected_output": {
            "_id": "MedicationQuery3",
            "category": "Medication",
            "subCategory": "Penicillin",
        },
        "repeat": 1,
    }
]
