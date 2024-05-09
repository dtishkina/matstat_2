import random
import statistics


def generate_uniform(low, up, n):
    result = []
    n_values = up - low + 1
    for _ in range(n):
        u = random.random()
        r = int(n_values * u) + low
        result.append(r)
    return result


def theoretical_mean(low, up):
    return (low + up) / 2


def theoretical_variance(low, up):
    n = up - low + 1
    return (n**2 - 1) / 12


def print_results(low, up, n):
    sample = generate_uniform(low, up, n)

    median = statistics.median(sample)
    theor_mean = theoretical_mean(low, up)

    variance = statistics.variance(sample)
    theor_variance = theoretical_variance(low, up)

    print(f"Оценка\t\t IRNUNI \t Погрешность \tТеоретическое значение")
    print(f"Медиана\t\t  {median:<6}\t\t{median - theor_mean:.3f}"
          f" \t\t  {theoretical_mean(low, up):.2f}")
    print(f"Дисперсия\t  {variance:.3f} \t\t {variance - theor_variance:.3f}"
          f" \t\t{theoretical_variance(low, up):.2f}")


def modeling_accuracy():
    print_results(1, 100, 10 ** 4)
    print('\n')
