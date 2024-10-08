/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
	if (n === 0) return 0;
	if (n === 1) return 1;

	const dp = Array.from({ length: n + 1 }).fill(0);
    // 공간 복잡도 줄이는 방법
    // const dp = [0, 0]

	dp[0] = 0;
	dp[1] = 1;
	for (let i = 2; i < n + 1; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
	}

	return dp[n];
};
