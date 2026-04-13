import torch
import torch.distributed as dist
def init_process(rank, size):
    dist.init_process_group('gloo', rank=rank, world_size=size)
