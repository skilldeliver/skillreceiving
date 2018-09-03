def tower_builder(n_floors):
    return [ " " * (((n_floors * 2 - 1) - (i * 2 - 1)) // 2) + "*" * (i * 2 - 1) + " " * (((n_floors * 2 - 1) - (i * 2 - 1)) // 2) for i in range(1, n_floors + 1)]