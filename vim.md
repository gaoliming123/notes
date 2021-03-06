# vim使用方法

## 移动命令

* 基本
   * 上下左右移动: `k`, `j`, `l`, `h`
* 行内
   * 移动到行末: `$`
   * 移动到行首: `^` 
   * 下一个单词: `w`, 上一个单词: `b`
   * 输入`f + 字母`, 行内移动到相应字母, 继续输入`;`是继续移动到下一处, 继续输入`,`是移动到上一处
* 一屏内移动
   * 屏幕的头部: `H`, 屏幕的尾部: `L`, 屏幕的中间: `M`
   * 上一段 `{`, 下一段 `}` vim中段落的区分使用空格来区分的
   * 括号匹配 `%`
* 文件内移动
   * 移动到文件的第一行:`gg`, 移动到文件的最后一行:`G`
   * 移动到文件的任意一行: `输入行号 + gg`
   * 快速回到上次编辑的位置: `ctrl + o`

## 选择命令

**选择命令一般配合移动命令使用(vim的快捷键是可以组合的)**

* 选中当前光标所在的单词: `viw`, 选中光标所在''里的内容: `vi'`, 选中光标所在()里的内容: `vib`
* 选中单个字母: `v`, 选中一行 `V`, 块选中 `ctrl + v`(配合插入命令使用)

## 插入命令
* 光标所在字母插入:`i`, 光标所在字母后面插入:`a` 
* 行首插入:`I`, 行末插入:`A`, 另起新的下一行插入:`o`, 另起新的上一行并插入:`O`
* 删除光标所在字符并插入: `s`, 删除整行并插入: `S`

## 编辑命令
* `dd` 删除一行
* `d` 删除命令(结合其他快捷键使用), 例如:
    * `dw`, `db` 删除一个单词
* 删除光标位置到行末`D`
* `yy` 复制一行
* `y` 配合移动命令和选中命令使用
* `J` 合并两行

## 打开文件
* 打开文件的时候固定到某行 `vi filename +line`

## 末行命令
* `:e .` 打开当前目录文件
* `:n newfile` 新建文件并编辑
* `:sp filename` 横向分屏编辑同一个(两个)文件, 窗口操作 `ctrl + w`
* `:open filename` 编辑文件的时候打开新的文件
* `/` 全文查找, `n`下一处, `N`上一处
* `:s/train/test/g` 替换命令, 将本行的 `train` 替换成 `test`
* `:%s/train/test/g` 替换命令, 将每一行的 `train` 替换成 `test`
