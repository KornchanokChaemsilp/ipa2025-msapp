from consumer import consume

rab = "rabbitmq"


def worker():

    consume(rab)


if __name__ == "__main__":
    worker()
