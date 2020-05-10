from hypothesis import strategies as st

digits = st.integers(min_value=0, max_value=9)
digit_tuples = st.builds(tuple, st.lists(digits, min_size=1))
# st.tuples does not mutate length, so must use st.lists
