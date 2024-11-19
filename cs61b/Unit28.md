# 归并排序_插入排序_快速排序
 
* [归并排序](#归并排序)
  * [合并](#合并)
  * [归并](#归并)
  * [时间复杂度](#时间复杂度)
* [插入排序](#插入排序)
* [原地插入排序](#原地插入排序)
  * [时间复杂度](#时间复杂度)
* [快速排序](#快速排序)
  * [分区](#分区)
  * [重复分区](#重复分区)
  * [时间复杂度](#时间复杂度)
  * [快速排序就是二叉搜索树排序](#快速排序就是二叉搜索树排序)
  * [避免最坏情况](#避免最坏情况)
 
## 归并排序

### 合并

我们有两个排过序的数组 希望将其合成一个更大的排序数组

![](img/42d3bc44.png)

逐一比较最前的元素，放置较小的，移动指针

![](img/a401dc43.png)

直到某一个数组的指针移动到末尾

![](img/0d0ba12e.png)

之后逐个复制另一个数组的剩余元素

![](img/223f2e80.png)

复杂度为O(N)

### 归并

我们有64个元素的数组 如果对其进行简单的选择排序会花费N^2，也就是4096个时间单位

![](img/e5273de6.png)

我们不对较大的数组排序，而是分为两个小数组**分别排序**

之后进行**合并**

32\*32\*2 + 64 = ~2112 个时间单位

由于我们的这种策略，时间几乎下降一半

但是复杂度仍然在θ(N^2)

![](img/457c59e9.png)

继续在此基础改进，重复上述的过程呢？？

![](img/56ee90e5.png)

在进行刚刚的32小数组排序时，将其分为两个16的小小数组，分别排序，而后合并 完成小32数组的排序

两层下降低为 1152个时间单位（有近乎下降一半！）

不过在有限次归并下，仍然是θ(N^2)的复杂度

我们再分、再分...

当我拆分到1时，只需要返回其。这就是基本情况

### 时间复杂度

![](img/a50413c1.png)

在每层，我们主要的工作是花费N的时间进行合并

1=2^0 2^1 2^2 ... 2^k = N 共有 k = logN 层

因此总体的复杂度进化为θ(Nlog N)

![](img/fad1b85d.png)

(堆排序实际用的很少，可能比其他排序慢)

## 插入排序

![](img/d9857804.png)

1. 首先将目前第一个元素放入输出
2. 查看下一个元素应该放在输出的哪个位置
3. 进行插入

![](img/8bed61c8.png)

重复插入

## 原地插入排序

在Java中，数组不能进行直接元素的插入，我们需要对细节进行处理

不再需要输出数组

![](img/cf893837.png)

对于每个元素，在已排序部分找到合适位置，前进的过程每次交换遇到元素的位置

第一个元素不动

![](img/a906aafd.png)

排序第二个元素

![](img/00bb643c.png)

第三个元素逐个比较，重复交换，知道左侧元素比它大，或者到达最左

![](img/a9e0a02f.png)

![](img/62c67805.png)

完成排序

![](img/63c3cce4.png)

这里有一个不变量：**每个将开始旅行的元素，其左侧元素都是排序好的**

### 时间复杂度

Ω(N) O(N^2)

最好只需要 查看每个元素并比较其和其左侧

最坏情况 我们要把每个元素旅行到最左侧 （0+1+2+..+N)

![](img/3a5d62e8.png)

![](img/ed24eb47.png)

**当我们改变了一个有序数组的一个元素，重新排序 插入排序是最优解** 只需要N的时间 而其他排序都需要更长时间

![](img/9cc67971.png)

因此插入排序非常适合只有部分（尤其有限项）无序的情况 只需要O(N)

另一种情况 **当数组非常小时，插入排序会比其他排序更快** N < 15 （Java内置的归并排序不会一直归并到1,而是当数组比较小时采用插入排序）

![](img/532a90b2.png)

区分各排序的关键是 **思考使其其作用的关键操作**

## 快速排序

关键想法是**分区** 

![](img/7193bbfc.png)

* 任意选择一个元素
* 重新排列数组 使得选择元素左侧的数字都小于等于其，右侧的元素都大于等于其

这样一次分区之后，**被选元素就在正确的位置！**

### 分区

一种想法是扫描一遍数组，把小于的放在新数组前面，大于的放在新数组后面，之后放入被选元素

### 重复分区

我们可以重复利用分区的想法来重复

对分区后两个无需的部分分别再次快速排序

![](img/e955699c.png)

两层快速排序后 现在我们有三个元素落在正确的位置

![](img/26e7fe9d.png)

**最快的已知排序**

### 时间复杂度

**如果每次主元都正好落在中间**

![](img/ebdbbf5b.png)

每层需要N的时间，大约有log N 层，因此最优情况下复杂度为θ(N logN)

而最坏情况下 每次我们选择的主元落在了两侧 **已经排序好的数组 或者 倒序的数组** 

所以每次仅仅只排序好一个元素

![](img/d3d09335.png)

因此退化为θ(N^2)

那么为什么快速排序是最快的排序？？

事实证明 对于世界上几乎所有数组，快速排序的期望运行时间都是Nlog N

主元每次都落在左侧10%位置 这种情况的复杂度仍然是 Nlog N

### 快速排序就是二叉搜索树排序

**快速排序实质上是搜索二叉树排序**

* 我们逐个取出数组中元素插入二叉树
* 之后中序遍历 得到排序数组

![](img/68d273eb.png)

**完全相同**意味着二者的比较序列完全一致，其考虑的是完全相同的事情

*  **快速排序中** 在选定主元5后，我们依次比较其后所有元素
* **BST** 中，每个元素都需要和根节点5比较

对于产生的两个子问题

* **快速排序中** 我们对于左子问题的所有元素`2` `1` `4`和`3`比较
* **BST中** 同样的元素和左子节点比较

...

只是顺序不同

**而随机二叉树的插入时间正是Nlog N**

最坏情况也对应BST的细长树

一个证明快速排序通常很好的实验

1000元素的数组

![](img/00148bd2.png)

实验证明 **快速排序比归并排序更快**

### 避免最坏情况

* 打乱数组
* 查看是否已经有序
* 扫描数组，换一个更好的基准值（扫描前几个，取中间值）