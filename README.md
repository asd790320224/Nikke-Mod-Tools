# Nikke-Tools

```
一套用于NIKKE Mod的实用工具集合
1.Nikke Mod Manager (for main)：
	①直接在github下载，位于该仓库/download/NMMv0.3.2.zip；
	②作者给的地址：https://gofile.io/d/utsJPe（v0.3.1，缺少mod分类），v0.3.2的升级包需在discord服务器中下载
2.Nikke Modeling (for Lobby/Burst)
	网站：https://kxdekxde.github.io/nikke/
3.Nikke File Finder (for anything)
	网站：https://a1ter00.github.io/nikke-file-finder/
4.Nikke Mod Repack (for old mod)
	①直接在github下载，位于该仓库/download/Mod Repack Script.zip
	②作者给的地址：https://mega.nz/folder/uIl1GKRC
5.Guide to Everything Related to NIKKE Mods (for skillful man)
	网站：https://docs.google.com/document/d/1DIhn_XsvG9qBpTln7WoaRolq7VdFoDFKR5R103P_FkM/edit?tab=t.0#heading=h.p3n8pwhprphm
6.Nikke Mod 制作者推荐 (for you)

```

![](https://i0.hdslb.com/bfs/new_dyn/fd76c1d00bfd41feb296c0c7006037df19505257.png)



## 1. Nikke Mod Manager (main)（by Danieru & Na0h & ...）

### 工具介绍

​	放入mod一键激活，几乎**支持除了爆裂动画mod以外的一切mod的一键自动应用**。当前NMM版本为v0.3.2，由**alkhdaniel（Danieru）**负责主体开发，**na0h.（Na0h）**负责精修（如加入mod分类和mod预览功能），因此该mod目前支持：

​	①**形体mod的自动激活**；

​	②**头像icons的自动激活**；

​	③**爆裂动画的文件路径的自动获取**（需手动激活）。

​	已经能够完全使用nikke的所有类型的mod了。

### 使用方法

#### NMM文件夹布局

NMM/**📁mods/**	 *# 放置形体mod的部分*

NMM/mods/**📁icons/**	# 放置头像mod，如没有该文件夹需自行创建

NMM/mods/**📁lobby/**	# 放置爆裂动画mod，如没有该文件夹需自行创建

NMM/**📁resources/**	# 存放有NAU、catalog等文件，NMM小版本升级到零件变化也存放于此

NMM/deps/nkab/**📁NKAB/dist/📄 hi_shiftup_dont_mind_me.js**	# 把NKAB文件夹移至nikke.exe目录下进行覆盖

NMM/**📄 settings.json**	# 存储个人数据、NMMmod启用情况

其他文件夹和文件作用可忽略不计。

#### mods文件夹中的命名格式

**{角色编号}** _ **{服装编号}** _ **{形体状态}** _ {作者} _ {其他}

形体mod可以采用TestMod中的命名格式：

- c511_01_standing_Na0h_辛德瑞拉
- c194_00_aim_Seireiko_T1-圣鲁
- c015_00_cover_117il3_泳装阿妮斯(去武器)

其他则不建议修改，按作者给的mod名称用即可：

- favoriteitemscene_c352_00（为海伦珍藏品动画）
- icons-char-mi(hd)_assets_mi_c225_01_s（为红莲：莲花的头像）



#### icons文件夹中的命名格式

如不想将icons放置到mods文件夹中，可以移至mods/icons文件夹中，需将mod重命名为：

**{角色编号}** _ **{服装编号}** _ **icons** _ {作者} _ {其他}

如将上述提到的红莲莲花的mod文件名改为：

- c225_01_icons_yuk11sh1d4_红莲：莲花



#### lobby文件夹中的命名格式

**{角色编号}** _ **{服装编号}** _ **{lobby/burst}** _ {作者} _ {其他}

- c330_01_lobby_Na0h_皇冠的新衣-Topless 

- c330_01_burst_Na0h_皇冠的新衣-Topless

------



## 2. Nikke Modeling（by KXDƎ）

### 工具介绍

​	由**kxdekxde（KXDƎ）**提供，用于**检索lobby或burst动画对应的parent folder**（动画文件的存储路径为：com_proximabeta_NIKKE /parents /child /__data）

​	因为com_proximabeta_NIKKE目录下有很多个parent folder，而每个parent folder下只有一个child folder，所以只需要定位好parent folder便可锁定到data的具体位置。

### 网站

​	**https://kxdekxde.github.io/nikke/** （可能会出现网页加载错误的情况，但不影响正常使用）

------



## 3. Nikke File Finder（by A1teri）

### 工具介绍

​	由**A1teri（a1ter0）**提供，用于**检索nikke中绝大部分的文件**（包括HD和SD的，甚至包括声音的）。用法：

1. 创建一个新文件夹，把catalog_131.10.2K、catalog_c70e7a9.json、physics-catalog_c70e7a9.db.dec.json三个文件放入其中（文件名是举例说明）
2. 点击网页左侧的Finders部分（比如点击Common Files(HD)），点击”UPLOAD FOLDER“，上传刚刚的文件夹。
3. 之后便可以开始搜索了。

​	json文件获取方式：

1. 加入dc的discord：**Destiny Child International**（[邀请链接](https://discord.gg/destiny-child-international-241679077658984448)）
2. 进入到/Nikke/nikke-no-mobile-modding-chat中可以找到上述三类json文件，**注意只用新不用旧**。（可以结合关键词”catalog“进行搜索）

### 网站

​	**https://a1ter00.github.io/nikke-file-finder/**

------



## 4. Nikke Mod Repack（by gjopin）

### 工具介绍

​	由**gjopin**提供，用于**将适用于NMMv0.2及之前的mod进行repack**。说明已置于/Mod Repack Script/README中。

------



## 5. Guide to Everything Related to NIKKE Mods（by Nikke Mod Lovers）

### 工具介绍

​	由**discord里的mod lovers**所编辑而成，内容下至用mod修mod、上至改mod建mod。

### 网站

​	[**Guide to Everything Related to NIKKE Mods**](https://docs.google.com/document/d/1DIhn_XsvG9qBpTln7WoaRolq7VdFoDFKR5R103P_FkM/edit?tab=t.0#heading=h.p3n8pwhprphm)

------



## 6. Nikke Mod

### 介绍

#### T0：Mr.Miagi（MM）

​	总结：伟大，无需多言。

​	优点：**①Mod质量极高**；**②有free mod提供**；③完全没有架子

​	缺点：①订阅路径过于偏僻（要DM他，然后才告诉你订阅途径）；②已停做nikke的mod了（转战bd2了）

​	免费mod：[Mr.Miagi Free Mods](https://mega.nz/folder/hO0AGR7J#0jsXQowsICRA_5EVJbTN0A)

#### T1：Na0h

​	总结：开创了lobby/burst动画mod的新时代（那个皇冠的就是他做的free mod）。

​	优点：①产能集中于nikke；**②有free mod提供**；**③有爆裂动画mod提供**；④开始逐步提供icons mod

​	缺点：①订阅要求严苛（无按月订购，一次消费过大）；②mod质量水平起伏较大；③部分细节处理不太好

​	免费mod：[Na0h的discord](https://discord.com/invite/wBJQ6gXz2U)

#### T1：Yuk11sh1d4

​	总结：开创了AI辅助创mod的新时代。

​	优点：**①利用AI辅助，具备超高产能**；②Mod质量稳定；③有爆裂动画mod提供；④有icons mod提供；**⑤可以按月订购Patreon**

​	缺点：①mod有明显AI痕迹（但妮游本身就...）；②部分mod的XP较重口；③业务太多；④无免费mod

​	免费mod：无

#### T1：117il3

​	总结：新秀，实力很够，但实例不够。

​	优点：**①Mod质量几乎可以比肩Miagi**；②XP正常；**③提供的mod都是免费的**

​	缺点：①产能严重不足（毕竟免费的，还能苛责人家啥呢）；

​	免费mod：[NIKKE Community](https://discord.gg/nikke) （核心大群，里面包含很多其他的免费mod / mod预览 / mod交流）

#### T2：Seireiko

​	总结：很早就开始做nikke mod了，但我对他的作画风格不是很感兴趣~

#### T3：gjopin & El-Caudillo & KXDƎ

​	总结：这类大概率是不做mod本身的创作的，而是进行Spine服饰分解或者做Swap Mod、Effect Remove相关的~

​	免费mod：

​		gjopin：https://mega.nz/folder/bN8iTIBS#6yy4SaNXuTJcqA2Ow17omA

​		El-Caudillo：https://mega.nz/folder/0UkkXTLS#dA0jwnVihdUnS4nfcXaajw

​		KXDƎ：https://www.mediafire.com/folder/4jzzho4lkcltq/NIKKE_MODS

#### T？：Housou

​	总结：这位的画风和色彩...怎么说呢，完全踩我雷点上了...不做评价。

------



## 未完待续

​	TestMod中有现版本可用的mod，可以试一下（我自用的，大部分是free mod）
