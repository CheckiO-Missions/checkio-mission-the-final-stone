"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[3, 5, 1, 1, 9]],
            "answer": 1,
        },
        {
            "input": [[1,2,3]],
            "answer": 0,
        },
        {
            "input": [[1,2,3, 4]],
            "answer": 0,
        },
        {
            "input": [[1,2,3, 4, 5]],
            "answer": 1,
        },
        {
            "input": [[1, 1, 1, 1]],
            "answer": 0,
        },
        {
            "input": [[1, 1, 1]],
            "answer": 1,
        },
        {
            "input": [[1, 10, 1]],
            "answer": 8,
        },
        {
            "input": [[1, 10, 1, 8]],
            "answer": 0,
        },
        {
            "input": [[]],
            "answer": 0,
        },
        {
            "input": [[1]],
            "answer": 1,
        },
        {
            "input": [[10, 20, 30, 50, 100, 10, 20, 10]],
            "answer": 10,
        }
    ],
    "Extra": [
        {
            "input": [[5,3,8,34,45,35,7,54,7,23,5,6,2,3,2,97,5,67,5]],
            "answer": 1,
        },

        {
            "input": [[4,3,5,5,5,5,5,3,2,5,6,7,8,5,4,6,8,8,4,2,2,2]],
            "answer": 0,
        }
    ]
}
