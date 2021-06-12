# DNA-Sequence-alignment
基于modeller官网脚本进行开发的序列比对脚本

前期准备：脚本文件model_mult.py(多模板文件用于拼接)、脚本文件 compareScripts4_0.py(用于产生用于拼接所用的ali文件)、脚本文件add_A.py（用于给pdb文件加氢）、EGFP-LINKER-SPYCATCHER.B99990001.pdb、model1.pdb、model2.pdb等pdb文件、序列（一大段字符串。）

序列内容为：MKTASAAACAAPWSSSSVYTGGKTASHNGHNWTAKWWTQNETPGRSDVWADADIDIMVSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKQHDFFKSAMPEGYVQERTIFFKDDGNYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNYNSHNVYIMADKQKNGIKVNFKIRHNIEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSALSKDPNEKRDHMVLLEFVTAAGITLGMDELYKGSSLVPRGSGGGGSSDPGSEFGGGGSGGGGSGAMVDTLSGLSSEQGQSGDMTIEEDSATHIKFSKRDEDGKELAGATMELRDSSGKTISTWISDGQVKDFYLYPGKYTFVETAAPDGYEVATAITFTVNEQGQVTVNGKATKGDAHIAAALEHHHHHH
 
 ![image](https://user-images.githubusercontent.com/54057111/117845716-634fdb00-b2b3-11eb-86bb-301de87fe3e4.png)

(所需文件如上)

# 使用方法
## 1、进行序列比对（用于获取xxx-mult.ali文件）
获取以上文件之后，我们需要进行序列比对。这是进行多模板拼接的必要前提。多模板拼接需要有xxx-mult.ali文件等一系列有效的pdb文件。

首先我们先编写csv文件，用于作为compareScripts4_0.py脚本文件的输入。
创建xlsx文件

![e9c7cb97976c26d04a55dff30b3bc3d](https://user-images.githubusercontent.com/54057111/117845832-78c50500-b2b3-11eb-97d3-b063b9993168.png)

打开新建的xlsx文件，开始编写

首先在第一行按照图上输入modelname与sequence
 
之后在第二行输入序列名称（不知道叫啥？那你就随便命名了）、与序列
 
输入后呈现这样。

![3eb55388cec39913f884f64f34ad80d](https://user-images.githubusercontent.com/54057111/117845900-87132100-b2b3-11eb-800a-9e8e2b211eba.png)


然后我们pdb文件有三个，我们首先在之后的行数，第一列、输入我们的pdb文件名称（注意末尾需要带.pdb），第二列就固定输入none

输入前：

![ec91bf2dcb45824eebcbb2f282f8a0d](https://user-images.githubusercontent.com/54057111/117845999-9d20e180-b2b3-11eb-8f58-9aa0be3a74d1.png)

输入后(输入的pdb文件其实是有先后顺序的，但是我们一开始是不知道顺序是什么，所以先不按顺序填写)：

![7c8d896e6833bf1509ab919abf370cc](https://user-images.githubusercontent.com/54057111/117846025-a3af5900-b2b3-11eb-8724-4f54126d0e30.png)

写完后另存为csv格式文件：

保存之后，目前你的文件夹应该是这样的(当然这个xlsx文件和csv文件是你随便命名的)：在这里，我命名为test

![41643ac72c2208a61faa20fbe3ba4c6](https://user-images.githubusercontent.com/54057111/117846101-b4f86580-b2b3-11eb-9718-3520f80f5b8a.png)


接下来我们进行初步的序列比对，使用compareScripts4_0.py脚本。
调用cmd窗口

输入这个命令：python compareScripts4_0.py test.csv

命令的语法是：python compareScripts4_0.py [csv文件]

弹出以下信息：

![e13b5990c32208e7d1b8020c2316e56](https://user-images.githubusercontent.com/54057111/117846222-cfcada00-b2b3-11eb-8d05-2c07ed932495.png)

我们注意到，实际上，这个命令是运行不成功的，它报错了。报错内容是：

Traceback (most recent call last):
  File "compareScripts4_0.py", line 158, in <module>
    initial_num = sequence_search(sequence, object_sequence)
  File "compareScripts4_0.py", line 83, in sequence_search
    return initial
UnboundLocalError: local variable 'initial' referenced before assignment

这里的意思就是，我们输入的pdb文件，转化的序列是与我们输入的序列是对不上号的。

接下来我们开始修复这个错误：

我们首先来看这个错误报告，我的脚本是会打印出pdb文件的序列出来的，以图为例：

![492b34f363c58207fb7fa723eef162c](https://user-images.githubusercontent.com/54057111/117846293-e1ac7d00-b2b3-11eb-9a5a-8682ac3593ca.png)

 
可以看到，脚本输出有以上信息，由于脚本报错内容是序列对不上号，所以我们首先整理以一下序列，看看哪里对不上号了。可能会有小朋友问了，这里不是只有2个pdb文件吗？那我们的model1.pdb去哪了？

答：由于脚本到某个步骤报错了，脚本自然是会因此中断了，model1.pdb文件自然是看不见。

接下来，我们查看model1.pdb的序列，首先在我们的csv文件上改动一下。
原来的csv文件：

![d16b32c51ac3c6046fd44d5292a7af5](https://user-images.githubusercontent.com/54057111/117846318-ea04b800-b2b3-11eb-89c3-80723db4f427.png)

改动后的csv文件：

![0dc8bb49a82e9c380f40ec30187633e](https://user-images.githubusercontent.com/54057111/117846351-effa9900-b2b3-11eb-8cd4-70cd550069bf.png)
 
可以看到，这里的顺序更改了，因为脚本必然会读csv文件最后一行的pdb文件序列，所以我们这样做，就是要看看model1.pdb文件的序列长什么样子。

保存csv文件后再次运行脚本：
得到：

![a276b2ffe69ce7e046caa67ae1ef8d0](https://user-images.githubusercontent.com/54057111/117846422-00127880-b2b4-11eb-9270-950394a50e3b.png)


在这里我们可以看到model1.pdb的序列了

![920c5d7638f726600237b5ec47986f0](https://user-images.githubusercontent.com/54057111/117846457-0acd0d80-b2b4-11eb-8a5e-f555ed43d02d.png)

之后我们就将这些pdb文件的序列整理一下，整理到txt文件里面，也就是复制粘贴序列到txt文件里面，对比一下，到底哪里序列对不上号。

这里排查的方法就按个人喜好来做

在这里我创建一个空的txt文件，使用editplus打开，然后整理成这样： 

![082df448aaffddb4e479881cae0104b](https://user-images.githubusercontent.com/54057111/117846535-1d474700-b2b4-11eb-8000-4dfa7026e59c.png)

好了，接下来我们检查下哪里对不上号的。对不上号的意思就是某个pdb的序列，不能完全包含在全序列里面。

首先，我们排查model2.pdb:

![ba5e6ec73f9503f3d5411e662d3d572](https://user-images.githubusercontent.com/54057111/117846569-26381880-b2b4-11eb-83b0-f1baffbd625f.png)
 
可以看出，model2.pdb的序列可以在全序列上对得上号，这里的model2.pdb没有问题。

接下来我们排查model1.pdb:

![d9bfe4a3e4a6831d2289743e8f2b534](https://user-images.githubusercontent.com/54057111/117846616-3223da80-b2b4-11eb-95c1-e205f6c5e464.png)
 
可以看出，在这里，model1.pdb可以和全序列对得上号。Model1.pdb没有问题。

接下来我们排查EGFP-LINKER-SPYCATCHER.B99990001.pdb 前两个没有问题，这个必有问题。

![3b50c147199923c3375c3f1aae8e88a](https://user-images.githubusercontent.com/54057111/117846680-3d770600-b2b4-11eb-83ec-61ab768fd615.png)

 
果然，我们在对它使用查找的时候，并没有搜索到全序列的一个片段，这时候我们得慢慢对比了，看看哪里有问题。这个得花点时间。

经过一轮对比之后，发现问题出现在前两个字符串，是和整个序列冲突的

![9bda244140f38cdfbe0a959893e125d](https://user-images.githubusercontent.com/54057111/117846717-4536aa80-b2b4-11eb-9002-c00128cfdc87.png)
 
当我们删掉这两个字符串之后，整体的序列就能对得上号了。 

![a1178e9a501c95702944eb621b55ced](https://user-images.githubusercontent.com/54057111/117846769-51226c80-b2b4-11eb-9dbb-6b86f24e5513.png)


删除之后就能对得上号了，问题就出在EGFP-LINKER-SPYCATCHER.B99990001.pdb这个pdb文件中。接下来我们直接对pdb文件进行操作。

用Editplus打开这个pdb文件。
 
![9a1a2d7beb35c37f07e5bb0e5de25ed](https://user-images.githubusercontent.com/54057111/117846798-597aa780-b2b4-11eb-9948-c3c028de674d.png)

首先把这个串串删掉，删掉这个串串对我们没有影响

![b1213522905bc8657485ead1ee3a7cf](https://user-images.githubusercontent.com/54057111/117846833-613a4c00-b2b4-11eb-9eb0-224e0738c0b8.png)
 
接下来因为出问题的序列是前两个字符串，因此，我们在pdb中，就删除前两个residue，就看中间那串数字就行：
 
![51d99f1afb987892c962399c07c5e88](https://user-images.githubusercontent.com/54057111/117846869-6b5c4a80-b2b4-11eb-9d9f-a903837d3a9b.png)

删除之后长这样，保存，退出
 
![3b1c63acc5ae27aa25cbb130285c7f1](https://user-images.githubusercontent.com/54057111/117846890-71eac200-b2b4-11eb-83c5-23ee218560c4.png)


接下来我们要更改csv文件的顺序，在刚刚的序列检查之后，我们要按先后顺序去排列，如图：
 
![564c2c19c53a0a85fb894909063d642](https://user-images.githubusercontent.com/54057111/117846943-7dd68400-b2b4-11eb-8fa0-fca3c0676382.png)

 
在对应的，我们在csv文件上，也要这样头部，身体，尾部这样排列先后顺序
原来csv： ![7086d8acf51bb5d232c02db6293de1f](https://user-images.githubusercontent.com/54057111/117846979-84fd9200-b2b4-11eb-89d6-96eb60bd0be6.png)

排列后的csv： ![0a6d02ac5e7566aefa208c8ddf3115a](https://user-images.githubusercontent.com/54057111/117846997-88911900-b2b4-11eb-9a17-7d27c7b886ce.png)

按照pdb顺序去修改。

接下来我们再次在cmd运行命令：

报错

![49f75904d706a04d78f41600d2bc4f2](https://user-images.githubusercontent.com/54057111/117847040-921a8100-b2b4-11eb-9580-0a9708d2e315.png)

是新类型的错误，这里的意思就是，三个pdb文件中，有一个文件的文件格式不对。
看看原来的文件夹：
 
可以看到，生成了三个新的pdb文件，其中reset_model1.pdb文件末尾是空的，0kb，因此判断这里必有问题。所以我们用editplus打开原来的pdb文件，也就是model1.pdb，并查看： 

![daa76463305db396ef7ff1364eaf763](https://user-images.githubusercontent.com/54057111/117847088-9f377000-b2b4-11eb-8d50-f4c33057c3dd.png)


可以看到，这里的pdb文件第一行有这个字符串，这个就是出bug的元凶，把它删掉保存，删掉后长这样：
 
![f12aa9d6f6fc53e81eae23c014b3c3b](https://user-images.githubusercontent.com/54057111/117847139-a8284180-b2b4-11eb-9881-cc8247badc63.png)

保存后，我们再次运行这个命令： 

得到这样的结果：

![779aba1d373a8db3a09ffd569d1458d](https://user-images.githubusercontent.com/54057111/117847182-b0807c80-b2b4-11eb-9465-cc2ce04d1a41.png)

在这里就大功告成了，没有出现任何的错误报告。第一步的比对完成。
这时候我们查看我们的文件夹应该是这样的：

![b731be598b9fd350641c96819314405](https://user-images.githubusercontent.com/54057111/117901552-2b21ba00-b2fe-11eb-8c09-24adf2be680f.png)

我们可以看到，程序生成了我们所需的一些文件，这些文件是用来做多模板拼接的。
 
接下来进入多模板拼接

## 2、进行多模板拼接（用于获取xxx.B99990001pdb文件）



打开我们的cmd窗口，在这里我们输入命令：

python model_mult.py test-mult0 chi_bind_spycatcher 3 reset_model2 reset_EGFP-LINKER-SPYCATCHER.B99990001 reset_model1
 
要注意的是，reset_*.pdb名字也有顺序的，按头部，身体，尾部的顺序输入。


这里是命令的语法：

python model_mult.py [*-mult0.ali文件名] [*.ali文件名] [pdb文件数量] [reset_pdb名字1] [reset_pdb名字2] [reset_pdb名字3] .........

输入命令后回车：
 
![362d3b4bd0ad04a2967366d4d285c2b](https://user-images.githubusercontent.com/54057111/117901613-455b9800-b2fe-11eb-9b26-7892500af300.png)

在这里，这里也有个错误产生：
 
意思是reset_EGFP-LINKER-SPYCATCHER.B99990001.pdb这个文件，缺少chain A，所以我们需要用脚本去修复，使用add_A.py脚本

我们接下来在cmd窗口输入python add_A.py reset_EGFP-LINKER-SPYCATCHER.B99990001.pdb
 
注意：在新版本我将add_A.py换成add_chain_v2.py 所以应该在cmd输入：
 
python add_chain_v2.py reset_EGFP-LINKER-SPYCATCHER.B99990001.pdb A
 
![image](https://user-images.githubusercontent.com/54057111/117901643-56a4a480-b2fe-11eb-9411-b6cab85e80c5.png)

回车
 
这个就是我们修复好的文件了

![image](https://user-images.githubusercontent.com/54057111/117901661-62906680-b2fe-11eb-9ccd-730fba18b467.png)


修复前是长这样的：

![image](https://user-images.githubusercontent.com/54057111/117901670-67551a80-b2fe-11eb-84b2-806909562182.png)

修复后是长这样的：
 
![image](https://user-images.githubusercontent.com/54057111/117901675-6a500b00-b2fe-11eb-855c-3fd755d8ff8b.png)


接下来我们把原来的reset_EGFP-LINKER-SPYCATCHER.B99990001.pdb删掉，把我们生成的reset_reset_EGFP-LINKER-SPYCATCHER.B99990001.pdb改名为reset_EGFP-LINKER-SPYCATCHER.B99990001.pdb。

修复好之后，我们调用cmd窗口，继续进行多模板拼接，继续输入命令： 
回车

弹出一大串东西

![image](https://user-images.githubusercontent.com/54057111/117901704-7c31ae00-b2fe-11eb-8077-da5e88f4455d.png)
 
表明我们这次运行得非常好，终于没有错误了。耐心等待。

 
看到这里，表明我们多模板拼接已经完成。

## 3、拿出pdb文件，并检查
运行完成后，此时我们的文件夹应该是这样的：
 
![image](https://user-images.githubusercontent.com/54057111/117901725-8d7aba80-b2fe-11eb-8af5-b916e025234d.png)
 
其中，这个文件是我们需要的：

![image](https://user-images.githubusercontent.com/54057111/117901719-8784d980-b2fe-11eb-8399-e3ff3bc009f9.png)

 
我们拿出这个pdb文件，打开pymol，加载这个pdb文件看看长啥样先。

![image](https://user-images.githubusercontent.com/54057111/117901740-97042280-b2fe-11eb-9a5f-594128c59bf8.png)

整体的结果看起来不错，没有出现一条羊肉串的样子，此时我们可以拿出这个文件出来了。
注意：拿出chi_bind_spycatcher.B99990001.pdb文件。

结束。
