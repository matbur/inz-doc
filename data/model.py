class Model:
    def __init__(self, network: Layer):
        ...

    def fit(self, X_inputs: np.ndarray, Y_targets: np.ndarray,
            validation_set: Tuple[np.ndarray, np.ndarray] = None,
            learning_rate=None, n_epoch=10,
            shuffle=False, train_file='train.json'):
        ...

    def predict(self, x: np.ndarray) -> np.ndarray:
        ...

    def predict_label(self, x: np.ndarray) -> int:
        ...

    def load(self, model_file: str):
        ...

    def save(self, model_file: str):
        ...
