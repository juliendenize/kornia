from typing import Union

from kornia.core import Tensor


class AverageMeter:
    """Computes and stores the average and current value.

    Example:
        >>> stats = AverageMeter()
        >>> acc1 = torch.tensor(0.99) # coming from K.metrics.accuracy
        >>> stats.update(acc1, n=1)  # where n is batch size usually
        >>> stats.avg
        tensor(0.9900)
    """

    val: Union[int, float, bool, Tensor]
    avg: Union[int, float, Tensor]
    sum: Union[int, float, Tensor]
    count: int

    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val: Union[int, float, bool, Tensor], n: int = 1) -> None:
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count
