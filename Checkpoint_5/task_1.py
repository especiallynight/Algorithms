def generate_parentheses(pair_count: int) -> None:
    """Выводит правильные скобочные последовательности."""
    completed_sequences: list[str] = []
    sequence_states: list[tuple[str, int, int]] = [("", 0, 0)]

    while sequence_states:
        current_sequence, opened_count, closed_count = sequence_states.pop()

        if len(current_sequence) == 2 * pair_count:
            completed_sequences.append(current_sequence)
            continue

        if opened_count < pair_count:
            next_sequence = current_sequence + "("
            sequence_states.append(
                (next_sequence, opened_count + 1, closed_count)
            )

        if closed_count < opened_count:
            next_sequence = current_sequence + ")"
            sequence_states.append(
                (next_sequence, opened_count, closed_count + 1)
            )

    print("\n".join(sorted(completed_sequences)))


generate_parentheses(int(input()))

