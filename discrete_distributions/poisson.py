import math
import random
import statistics


def formation_of_sequence(lambda_):
    p_list = [math.exp(-lambda_)]
    r = 1
    while True:
        p_next = p_list[-1] * (lambda_ / r)
        if p_next < 1e-6:
            break
        p_list.append(p_next)
        r += 1
    return p_list


def get_y_values_list(lambda_):
    return [i for i in range(len(formation_of_sequence(lambda_)))]


def y_sample(k, lambda_):
    return random.choices(get_y_values_list(lambda_), formation_of_sequence(lambda_), k=k)


def theoretical_mean(lambda_):
    return lambda_


def theoretical_variance(lambda_):
    return lambda_


def normal_approximation_sample(k, lambda_):
    return [random.normalvariate(lambda_, math.sqrt(lambda_)) for _ in range(k)]


def print_results(k, lambda_):

    sample = y_sample(k, lambda_)
    median = statistics.median(sample)
    variance = statistics.variance(sample)

    normal_approximation = normal_approximation_sample(k, lambda_)
    normal_median = statistics.median(normal_approximation)
    normal_variance = statistics.variance(normal_approximation)

    print(f"Оценка\t\t IRNPOI \t IRNPSN \tТеоретическое значение")
    print(f"Медиана\t\t  {median:<6} \t {normal_median:.3f} \t\t  {theoretical_mean(lambda_):.2f}")
    print(f"Дисперсия\t  {variance:.3f} \t {normal_variance:.3f} \t\t  {theoretical_variance(lambda_):.2f}")


def modeling_accuracy():
    print_results(10**4, 10)
    print('\n')
