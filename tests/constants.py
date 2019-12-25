BAD_TYPES = (
    1.0,
    (5.0, ),
    (2, 5.0),
    (5.0, 2),

    "test",
    ("test", ),
    ("test", 5),
    (5, "test"),

    None,
    (None, ),
    (None, 5),
    (5, None),

    True,
    (True, ),
    (True, 5),
    (5, True)
)
