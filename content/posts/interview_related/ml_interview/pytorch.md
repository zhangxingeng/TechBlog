### Overall Information

- Revers-mode automatic differentiation
  - store intermediate values in the forward pass, use them at backprop 
  - This is why you do zero_grad() before each new batch (more accurately after each backprop).
- Tensorflow vs Pytorch
  - before 2.0 static (compile-then-run) vs eager execution (define-by-run)
  - TF less community.
  - TF less intuitive.
  - pytorch less performance but easier to maintain(which is better for companies).
  - Data Parallelism
    - pytorch: 
      - `DataParallel` for multi-GPUs, directly usable to any `nn.Module`
      - DistributedDataParallel (DDP) for multi-nodes
      - rely on external tools to manage nodes (simple code base)
    - TF:
      - more config, more code change, just not good.

### Code Specific
- get grad: set param of a nn.module `requires_grad=True`, `backward()`


### Components of Pytorch
- Tensor: multi-dimensional array. e.g.: `torch.IntTesnor`, `torch.FloatTensor`
- (Deprecated)Variable: wrapper around tensor for gradient stuff. `torch.autograd.Variable`
  - new pytorch variable's functions are migrated into Tensor itself, no more Variable, just use `requires_grad=True` in `Tensor` creation
- Parameters: the parameter of the model, have gradients. `torch.nn.Parameter`??? need more info
  - parameters are registered to a model, so that `model.parameters()` can return all parameters
  - follow up question: is it that simple? parameters are just tensors with gradients? or there is more to it?
- Functions: stateless , just do some task. `torch.nn.functional.*`, `F.relu`, `torch.sum`, `torch.optim.SGD` etc
- Modules: 
  - define the architecture of the model, can contain `Modules`, `Parameters`, and method definitions like `forward`. 
  - all layers (like `Linear`, `Conv2d`, `RNN`, etc.) are subclasses of `torch.nn.Module`
  - Modules like `Linear` can contain `Parameters` like `weight` and `bias` (which are `Tensor`s)
  
### Custom Layer (no Modules)
```python
class CustomLayer(nn.Module):
    def __init__(self, input_size, output_size):
        super(CustomLayer, self).__init__()
        self.weights = nn.Parameter(torch.randn(input_size, output_size))
        self.bias = nn.Parameter(torch.randn(output_size))

    def forward(self, X):
        linear = torch.matmul(X, self.weight.data) + self.bias.data
        return linear
```