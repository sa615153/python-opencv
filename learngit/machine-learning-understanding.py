N-N

So instead of being constrained by the original input features, 
    a neural network can learn its own features to feed into logistic regression

Depending on the Ɵ1 parameters you can learn some interesting things
    Flexibility to learn whatever features it wants to feed into the final logistic regression calculation
        So, if we compare this to previous logistic regression, you would have to calculate your own exciting features to define the best way to classify or describe something
        Here, we''re letting the hidden layers do that, so we feed the hidden layers our input values, and let them learn whatever gives the best final result to feed into the final output layer



in logistic regression, y is {1,2,3,4}, and显式的用多次多个h(x)，每次是训练one vs all，训练时用0 1 指代是否为当前label， 而成的参数
now y is [1;0;0;0], [0;1;0;0], [0;0;1;0], [0;0;0;1],是用一次h(x),直接得出类概率向量，当然，训练时也用[1;0;0;0], [0;1;0;0], [0;0;1;0], [0;0;0;1]训练
    感觉计算上不一定会减少很多，因为向量的每个元素都要从前走到后边，经过很多次g(theta'X)'

理解上，最后一层，output layer，每一个node都是sigmoid(theta'X)'得到的0-1之间的数字


'------------------'
   architecture
'------------------'

对于输入单元 和输出单元数目的选择 还是比较容易理解的
有一个默认的规则 那就是只使用单个隐藏层 所以最左边所示的 这种只有一个隐藏层的神经网络 一般来说是最普遍的
如果你使用 不止一个隐藏层的话 同样我们也有一个默认规则 那就是每一个隐藏层 通常都应有相同的单元数
对于隐藏单元的个数 通常情况下 隐藏单元越多越好 不过 我们需要注意的是 如果有大量隐藏单元 计算量一般会比较大 当然 一般来说隐藏单元还是越多越好 
每个隐藏层 所包含的单元数量 还应该和输入x 的维度相匹配 也要和特征的数目匹配 可能隐藏单元的数目 和输入特征的数量相同 或者是它的二倍 或者三倍 
四倍 因此 隐藏单元的数目需要和其他参数相匹配 一般来说 隐藏单元的数目取为稍大于 输入特征数目 都是可以接受的



'------------------'
   auto drive
'------------------'
输入：车前图片
输出：方向盘角度

将车前图片按照应有角度（人工标定）分类，最后新图片被划归为具体角度类




delta


[delta super(l)sub(j)] measures how much that node was responsible for any errors in our output.
影响力依权重流动，delta是由error依权重反流（theta'delta.*g'(z2)）的，所以得出以上结论


'--------------------------------'
'Visualizing the hidden layer'
'--------------------------------'
可视化单排theta，对应hidden layer的该排hidden unit，将400参数reshape成20*20图片显示出来，含义为：至少包含率（包含参数灰度形式）
given a particular hidden unit, one way to visualize what it computes is to find an
input x that will cause it to activate (that is, to have an activation value(a(l)i) close to 1)

one way to visualize the representation captured by the hidden unit is to reshape this 400 dimensional vector into a 20 * 20 image and
display it.

It turns out that this is equivalent to finding the input that gives the highest activation
for the hidden unit, given a norm constraint on the input