# var-7

from discrete_distributions import binomial as x, poisson as y


def sign_test(sample_X, sample_Y):
    sign_differences = [1 if x > y else -1 if x < y else 0 for x, y in zip(sample_X, sample_Y)]
    positive_count = sum(1 for sign in sign_differences if sign == 1)
    negative_count = sum(1 for sign in sign_differences if sign == -1)
    statistic = min(positive_count, negative_count)

    return statistic


def significance_test(statistic):
    critical_value = 21
    return statistic <= critical_value


N = 20
p = 0.25
k = 50
lambda_ = 4

sample_X = x.x_sample(k, N, p)
sample_Y = y.y_sample(k, lambda_)

statistic = sign_test(sample_X, sample_Y)
significant = significance_test(statistic)

print(f"Статистика критерия: {statistic}")

if significant:
    print("Гипотеза H0 о совпадении функций распределения принимается.")
else:
    print("Гипотеза H0 о совпадении функций распределения отвергается.")
