import numpy as np


def minimal(message: str) -> int:
    length = len(message)
    length **= 0.5
    if abs(length - int(length)) < 1e-9:
        res = int(length)
    else:
        res = int(length) + 1
    if res % 2 == 1:
        res += 1
    return res // 2


def rotate_grid(grid):
    return np.rot90(grid, k=-1)


def generate_cardan_grid(n):
    grid = np.zeros((n, n), dtype=int)
    used = set()

    for i in range(n):
        for j in range(n):
            if (i, j) in used:
                continue
            positions = [
                (i, j),
                (j, n - 1 - i),
                (n - 1 - i, n - 1 - j),
                (n - 1 - j, i)
            ]
            if all(pos not in used for pos in positions):
                import random
                chosen = random.choice(positions)
                grid[chosen] = 1
                for pos in positions:
                    used.add(pos)

    return grid


def encrypt_cardan(message, grid):
    n = grid.shape[0]
    result = np.full((n, n), ' ')
    msg_idx = 0
    current_grid = grid.copy()

    for _ in range(4):
        for i in range(n):
            for j in range(n):
                if current_grid[i, j] == 1 and msg_idx < len(message):
                    result[i, j] = message[msg_idx]
                    msg_idx += 1
        current_grid = rotate_grid(current_grid)

    return '\n'.join([''.join(row) for row in result])


def decrypt_cardan(encrypted_grid_str, grid):
    n = grid.shape[0]
    grid_lines = encrypted_grid_str.splitlines()
    encrypted_grid = np.array([list(row.ljust(n)) for row in grid_lines])

    message = []
    current_grid = grid.copy()

    for _ in range(4):
        for i in range(n):
            for j in range(n):
                if current_grid[i, j] == 1:
                    message.append(encrypted_grid[i, j])
        current_grid = rotate_grid(current_grid)

    return ''.join(message).strip()


if __name__ == "__main__":
    message = input("Введите сообщение для шифрования: ")
    n = minimal(message) * 2
    grid = generate_cardan_grid(n)
    print("Решетка Кардано:")
    print(grid)

    print("\nСообщение:", message)

    encrypted = encrypt_cardan(message, grid)
    print("\nЗашифрованное сообщение:")
    print(encrypted)

    decrypted = decrypt_cardan(encrypted, grid)
    print("\nРасшифрованное сообщение:")
    print(decrypted)