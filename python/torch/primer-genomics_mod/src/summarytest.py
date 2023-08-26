#%%

import torchinfo
import torch.nn as nn
import torch
import torch.nn.functional as F


# %%

class LSTMNet(nn.Module):
    def __init__(self, vocab_size=20, embed_dim=300, hidden_dim=512, num_layers=2):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.encoder = nn.LSTM(embed_dim, hidden_dim, num_layers=num_layers, batch_first=True)
        self.decoder = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x):
        embed = self.embedding(x)
        out, hidden = self.encoder(embed)
        out = self.decoder(out)
        out = out.view(-1, out.size(2))
        return out, hidden

# %%
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv1d(4, 32, 12)
        self.pool = nn.MaxPool1d(4)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(288, 16)
        self.fc2 = nn.Linear(16, 2)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.flatten(x)
        x = F.relu(self.fc1(x))
        x = F.softmax(self.fc2(x), dim=1)

        return x

#%%
# Have to specify input dimensions because pytorch has dynamic computational graph 
# (unlike Keras).  So it doesn't know the dimensions until you tell it. 
torchinfo.summary(
    LSTMNet(),
    (1, 100),dtypes=[torch.long])
#    ,
#    dtypes=[torch.long],
#    verbose=1,
#    col_width=16,
#    col_names=["kernel_size", "output_size", "num_params", "mult_adds"],
#    row_settings=["var_names"],
#)


# %%

#torchinfo.summary(
#    Net(),
#    (4,20),dtypes=[torch.long])



# %%

print(Net())

# %%

repr(Net())

# %%

# From https://stackoverflow.com/questions/42480111/how-do-i-print-the-model-summary-in-pytorch
def printParams(net):
    modules = [module for module in net.modules()]
    params = [param.shape for param in net.parameters()]

    # Print Model Summary
    print(modules[0])
    total_params=0
    for i in range(1,len(modules)):
        j = 2*i
        if (j-1) < len(params):
            param = (params[j-2][1]*params[j-2][0])+params[j-1][0]
            total_params += param
            print("Layer",i,"->\t",end="")
            print("Weights:", params[j-2][0],"x",params[j-2][1],
            "\tBias: ",params[j-1][0], "\tParameters: ", param)

    print("\nTotal Params: ", total_params)



# %%

printParams(Net())


# %%

printParams(LSTMNet())


# %%
