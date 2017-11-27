def input_data(shape: Tuple[Optional[int], int]) -> Layer:
    ...


def fully_connected(incoming: Layer, n_units: int,
                    activation='sigmoid') -> Layer:
    ...


net = input_data(shape=(None, 30))
net = fully_connected(net, 24, activation='sigmoid')
net = fully_connected(net, 16, activation='sigmoid')
net = fully_connected(net, 12, activation='sigmoid')
net = fully_connected(net, 8, activation='sigmoid')
