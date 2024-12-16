from utils import read, write


def match_pattern_dp(pattern: str, string: str) -> bool:
    n = len(pattern)
    m = len(string)

    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for ind_in_pat in range(1, n + 1):
        if pattern[ind_in_pat - 1] == '*':
            dp[ind_in_pat][0] = dp[ind_in_pat - 1][0]

    for ind_in_pat in range(1, n + 1):
        for ind_in_str in range(1, m + 1):
            if pattern[ind_in_pat - 1] == string[ind_in_str - 1] or pattern[ind_in_pat - 1] == '?':
                dp[ind_in_pat][ind_in_str] = dp[ind_in_pat - 1][ind_in_str - 1]
            elif pattern[ind_in_pat - 1] == '*':
                dp[ind_in_pat][ind_in_str] = dp[ind_in_pat - 1][ind_in_str] or dp[ind_in_pat][ind_in_str - 1]

    return dp[n][m]


def main():
    pattern, string, = read(type_convert=str)
    ans = match_pattern_dp(pattern[0], string[0])
    if ans:
        write("YES")
    else:
        write("NO")


if __name__ == '__main__':
    main()
