from hypothesis import strategies as st

digits = st.integers(min_value=0, max_value=9)
digit_tuples = st.builds(tuple, st.lists(digits, min_size=1))
# st.tuples does not mutate length, so must use st.lists

normalized_digit_tuples = st.builds(
    tuple,
    st.lists(st.integers(min_value=2, max_value=9), min_size=1)
)

