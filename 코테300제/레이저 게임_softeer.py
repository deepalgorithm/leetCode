def max_score_optimized(grid):
    rows, cols = len(grid), len(grid)
    max_result = float('-inf')

    # 2D 누적 합 계산
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            prefix_sum[r + 1][c + 1] = grid[r][c] + prefix_sum[r][c + 1] + prefix_sum[r + 1][c] - prefix_sum[r][c]

    def get_rectangle_sum(r1, c1, r2, c2):
        return prefix_sum[r2 + 1][c2 + 1] - prefix_sum[r1][c2 + 1] - prefix_sum[r2 + 1][c1] + prefix_sum[r1][c1]

    # A의 레이저 선택 (가로 방향으로 고정)
    for a_start in range(rows):
        for a_end in range(a_start + 1, rows + 1):
            temp_grid = [row[:] for row in grid]
            for r in range(a_start, a_end):
                temp_grid[r] = [1] * cols

            # B의 레이저 선택 (세로 방향으로 고정)
            for b_start in range(cols):
                for b_end in range(b_start + 1, cols + 1):
                    temp_grid_b = [row[:] for row in temp_grid]
                    for c in range(b_start, b_end):
                        for r in range(rows):
                            temp_grid_b[r][c] *= 2

                    # C의 직사각형 선택
                    for c_start_row in range(rows):
                        for c_end_row in range(c_start_row, rows):
                            for c_start_col in range(cols):
                                for c_end_col in range(c_start_col, cols):
                                    score = get_rectangle_sum(c_start_row, c_start_col, c_end_row, c_end_col)
                                    max_result = max(max_result, score)

    return max_result
