import math
import random
import statistics


def formation_of_sequence(N, p):
    p_list = [((1 - p) ** N)]
    for r in range(1, N + 1):
        p_next = p_list[-1] * (((N - r) / (r + 1)) * (p / (1 - p)))
        p_list.append(p_next)
    return p_list


def get_x_values_list(N):
    return [i for i in range(N + 1)]


def x_sample(k, N, p):
    return random.choices(get_x_values_list(N), formation_of_sequence(N, p), k=k)


def theoretical_mean(N, p):
    return N * p


def theoretical_variance(N, p):
    return N * p * (1 - p)


def normal_approximation_sample(k, N, p):
    mu = N * p
    sigma = math.sqrt(N * p * (1 - p))
    return [random.normalvariate(mu, sigma) for _ in range(k)]


def print_results(k, N, p):
    sample = x_sample(k, N, p)
    median = statistics.median(sample)
    variance = statistics.variance(sample)

    normal_approximation = normal_approximation_sample(k, N, p)
    normal_median = statistics.median(normal_approximation)
    normal_variance = statistics.variance(normal_approximation)

    print(f"Оценка\t\t IRNBIN \t IRNBNL \tТеоретическое значение")
    print(f"Медиана\t\t  {median:<6} \t {normal_median:.3f} \t\t  {theoretical_mean(N, p):.2f}")
    print(f"Дисперсия\t  {variance:.3f} \t {normal_variance:.3f} \t\t  {theoretical_variance(N, p):.2f}")


def modeling_accuracy():
    print_results(10**4, 10, 0.5)
    print('\n')
