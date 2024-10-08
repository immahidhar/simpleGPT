import dataclasses

@dataclasses.dataclass
class SimpleGPTConfig():
    """ A convenient config class to hold all the hyperparameters """
    vocab_size = None
    device = 'cpu'
    batch_size = 16 # how many independent sequences will we process in parallel?
    block_size = 32 # what is the maximum context length for predictions?
    max_iters = 5000
    eval_interval = 100
    learning_rate = 1e-3
    eval_iters = 200
    n_embd = 64
    n_head = 4
    n_layer = 4
    dropout = 0.0

    def __repr__(self):
        """Returns a string containing only the non-default field values."""
        s = ', '.join(f'{field.name}={getattr(self, field.name)!r}'
                    for field in dataclasses.fields(self)
                    if getattr(self, field.name) != field.default)
        return f'{type(self).__name__}({s})'