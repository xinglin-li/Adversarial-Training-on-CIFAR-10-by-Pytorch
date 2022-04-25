import torch
import torch.nn.functional as F
import copy


class LinfPGDAttack(object):
    def __init__(self, model,epsilon,alpha,k):
        self.model = model
        self.epsilon = epsilon
        self.alpha = alpha
        self.k = k

    def perturb(self, x_natural, y):
        epsilon = self.epsilon
        alpha = self.alpha
        k = self.k
        x = x_natural.detach()
        x = x + torch.zeros_like(x).uniform_(-epsilon, epsilon)
        for i in range(k):
            x.requires_grad_()
            with torch.enable_grad():
                logits = self.model(x)
                loss = F.cross_entropy(logits, y)
            grad = torch.autograd.grad(loss, [x])[0]
            x = x.detach() + alpha * torch.sign(grad.detach())
            x = torch.min(torch.max(x, x_natural - epsilon), x_natural + epsilon)
            x = torch.clamp(x, 0, 1)
        return x

def attack(x, y, model, adversary):
    model_copied = copy.deepcopy(model)
    model_copied.eval()
    adversary.model = model_copied
    adv = adversary.perturb(x, y)
    return adv