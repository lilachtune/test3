import random
import time

def generate_data():
    # Простой генератор
    return {
        "heart_rate": random.randint(60, 120),
        "steps": random.randint(0, 100)
    }


def piska():
    print()